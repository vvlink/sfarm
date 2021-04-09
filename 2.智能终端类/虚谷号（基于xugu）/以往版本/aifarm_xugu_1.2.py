import siot
from xugu import Pin
from time import sleep

iot_server = '127.0.0.1' # mqtt服务器地址
iot_user = 'scope'
iot_pwd = 'scope'
projectid = 'sf88' # 项目编号
t1=10 # 上传数据的间隔时间，单位秒
t2=5 # 电磁阀打开的保持时间，单位秒
soil=500 # 土壤湿度传感器数值阈值，建议大于500

a0 = None
a1 = None

_siot_connected=False

topic_msg_map={}
def on_topic_subscribe(client,userdata,msg):
    global topic_msg_map
    topic_msg_map[str(msg.topic)]=str(msg.payload.decode())

def on_topic_read(topic):
    global topic_msg_map
    result=topic_msg_map.get(topic,None)
    if result:
        del topic_msg_map[topic]
        return result

siot.init('',iot_server,user=iot_user,password=iot_pwd)
siot.connect()
_siot_connected=True
if _siot_connected:
    siot.subscribe(projectid + '/d2',on_topic_subscribe)
    siot.loop()
    while True:
        if '1' == on_topic_read(projectid + '/d2'):
            Pin(2, Pin.OUT).write_digital(1)
            sleep(t2)
        else:
            Pin(2, Pin.OUT).write_digital(0)
            a0 = Pin("A0", Pin.ANALOG).read_analog()
            siot.publish(projectid + '/a0',a0)
            sleep(0.01);
            a1 = Pin("A1", Pin.ANALOG).read_analog()
            siot.publish(projectid + '/a1',a1)
            if soil < a1:
                Pin(2, Pin.OUT).write_digital(1)
                sleep(t2);
                Pin(2, Pin.OUT).write_digital(0)
            sleep(t1)