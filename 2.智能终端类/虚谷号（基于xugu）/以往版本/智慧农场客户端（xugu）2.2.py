#!/usr/bin/env python
# coding: utf-8

# # 智慧农场客户端（2.2）
# 
# 程序说明：
# 
# - 基于xugu库开发，定时上传光线、土壤湿度数据；
# - 能够根据土壤湿度（阈值在参数中设置）自行浇水；
# - 能够接收MQTT服务器发送的浇水指令浇水
# - 服务器重新启动后，能够自动重新连接。
# 
# 设备接线说明：
# 
# - 光线传感器接 A0；
# - 土壤湿度传感器接 A1；
# - 电磁阀接D2。
# 
# 其他说明：
# 
# - 不同的智能终端（虚谷号）需要设置不同的项目编号；
# - 支持任何一款MQTT服务器；
# - 能够实时响应服务器的浇水指令，但浇水时间会影响传感器上传数据的间隔时间。
# 


import siot
from xugu import Pin
import time

iot_server = '127.0.0.1' # mqtt服务器地址
iot_user = 'scope'
iot_pwd = 'scope'
projectid = 'sf107' # 项目编号
t1 = 60 # 上传数据的间隔时间，单位秒
t2 = 5 # 电磁阀打开的保持时间，单位秒
soil = 500 # 土壤湿度传感器数值阈值，建议大于500

is_close_unknown=False #非正常关闭siot连接标志

a0 = None
a1 = None
start_time = None
end_time = None
i = 0
topic_msg_map={}


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
    siot.subscribe(projectid + '/d2',on_topic_subscribe)

"""
SIoT的rc消息说明
0: 连接成功
1: 连接失败-不正确的协议版本
2: 连接失败-无效的客户端标识符
3: 连接失败-服务器不可用
4: 连接失败-错误的用户名或密码
5: 连接失败-未授权
6-255: 未定义.
"""
def on_connect(client, userdata, flags, rc):#siot连接时回调
    rc=int(rc)
    if(rc==0):#连接成功
        global is_close_unknown  #如果是未知原因关闭的话 订阅会丢失 重新订阅即可
        if(is_close_unknown):
          all_subscribe()
          is_close_unknown=False
          print("非正常关闭,所以需要重新初始化订阅相关代码")

def on_disconnect(client, userdata, rc): #siot关闭连接时回调
    rc=int(rc)
    if(rc!=0): #0是正常关闭 非0即表示非正常关闭
        print("说明连接已经关闭了....")
        global is_close_unknown
        is_close_unknown=True

siot.init('',iot_server,user=iot_user,password=iot_pwd)
siot.client.on_connect=on_connect
siot.client.on_disconnect=on_disconnect
siot.connect()
all_subscribe()
siot.loop()
start_time = time.time() - t1
water = False
while True:
    a0 = Pin("A0", Pin.ANALOG).read_analog()
    a1 = Pin("A1", Pin.ANALOG).read_analog()
    if soil < a1:
        water = True
        print("超出阈值，当前为：%d"%a1)
    getcmd = on_topic_read(projectid + '/d2')
    if getcmd:
        print("收到指令：内容为：%s"%getcmd)
        if getcmd == '1':
            water = True
    if water:
        Pin(2, Pin.OUT).write_digital(1)
        time.sleep(t2);
        Pin(2, Pin.OUT).write_digital(0)
        water = not water
        
    end_time = time.time()
    if end_time - start_time > t1:
        siot.publish(projectid + '/a0',a0)
        time.sleep(0.01);
        siot.publish(projectid + '/a1',a1)
        start_time = time.time()
        i=i+1
        print("发送数据：%d"%i)
            
