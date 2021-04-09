import siot
from xugu import Pin
from time import sleep

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
  del site[topic]
  return result

siot.init('','127.0.0.1',user='scope',password='scope')
siot.connect()
_siot_connected=True
if _siot_connected:
  siot.subscribe('af/d2',on_topic_subscribe)
  siot.loop()
  while True:
    a0 = Pin("A0", Pin.ANALOG).read_analog()
    siot.publish('af/a0',a0)
    sleep(0.01);
    a1 = Pin("A1", Pin.ANALOG).read_analog()
    siot.publish('af/a1',a1)
    sleep(5);
    if '1' == on_topic_read('af/d2'):
      Pin(2, Pin.OUT).write_digital(1)
      sleep(5);
    else:
      Pin(2, Pin.OUT).write_digital(0)
    if 380 > a1:
      Pin(2, Pin.OUT).write_digital(1)
      sleep(2);
      Pin(2, Pin.OUT).write_digital(0)
