# coding: utf-8
# 开源智慧农场终端代码，基于虚谷号（pinpong库）。
# 版本：1.1
# 功能：1)支持最基本功能，发送光线、土壤湿度，订阅浇水指令;2)支持发送空气温湿度。

from pinpong.board import *
import siot
import time

iot_server = '192.168.3.136' # mqtt服务器地址
iot_user = 'scope'
iot_pwd = 'scope'
projectid = 'sf88' # 项目编号，不同项目的id不能相同，否则进程会被踢出
t1 = 60 # 上传数据的间隔时间，单位秒
t2 = 5 # 电磁阀打开的保持时间，单位秒
soil = 500 # 土壤湿度传感器数值阈值，建议大于500

is_close_unknown = False #非正常关闭siot连接标志

a0 = None
a1 = None
start_time = None
end_time = None
i = 0
topic_msg_map = {}


def on_topic_subscribe(client,userdata,msg):
    global topic_msg_map
    topic_msg_map[str(msg.topic)]=str(msg.payload.decode())

def on_topic_read(topic):
    global topic_msg_map
    result=topic_msg_map.get(topic,None)
    if result:
        del topic_msg_map[topic]
        return str(result)

def all_subscribe(): #所有的订阅相关集合 
    siot.subscribe(projectid + '/relay',on_topic_subscribe)

def on_connect(client, userdata, flags, rc):#siot连接时回调
    rc = int(rc)
    if(rc == 0):#连接成功
        global is_close_unknown  #如果是未知原因关闭的话 订阅会丢失 重新订阅即可
        if(is_close_unknown):
          all_subscribe()
          is_close_unknown=False
          print("非正常关闭,所以需要重新初始化订阅相关代码")

def on_disconnect(client, userdata, rc): #siot关闭连接时回调
    rc = int(rc)
    if(rc != 0): #0是正常关闭 非0即表示非正常关闭
        print("说明连接已经关闭了....")
        global is_close_unknown
        is_close_unknown=True

siot.init(projectid,iot_server,user=iot_user,password=iot_pwd)
siot.client.on_connect=on_connect
siot.client.on_disconnect=on_disconnect
siot.connect()
all_subscribe()
siot.loop()
start_time = time.time() - t1
water = False

Board("xugu").begin()

while True:
    a0 = Pin(Pin.A0,Pin.ANALOG).read_analog()
    a1 = Pin(Pin.A1,Pin.ANALOG).read_analog()
    # print("a0：%d，a1：%d"%(a0,a1))
    if soil < a1:
        water = True
        print("超出阈值，当前为：%d"%a1)
    getcmd = on_topic_read(projectid + '/relay')
    if getcmd:
        print("收到浇水指令：内容为：%s"%getcmd)
        if getcmd == '1':
            water = True
    if water:
        Pin(Pin.D2,Pin.OUT).write_digital(1)
        time.sleep(t2);
        Pin(Pin.D2,Pin.OUT).write_digital(0)
        water = not water
        
    end_time = time.time()
    if end_time - start_time > t1:
        siot.publish(projectid + '/light',a0)
        time.sleep(0.01);
        siot.publish(projectid + '/soil',a1)
        time.sleep(0.01);
        d4 = [DHT11(Pin(Pin.D4)).temp_c(),DHT11(Pin(Pin.D4)).humidity()]
        siot.publish(projectid + '/air',str(d4))
        start_time = time.time()
        i = i + 1
        print("发送数据：%d"%i)
            
