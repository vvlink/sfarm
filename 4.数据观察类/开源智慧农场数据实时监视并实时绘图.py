# 实时监视物联网数据(针对某一个项目的某个设备)
# 需要提供订阅的设备名称，如af88/a0(项目af88的光线传感器数据)
# 每收到一条消息，将实时打印在界面上，并实时绘图。

import siot,time

SERVER = "192.168.3.122"        #MQTT服务器IP
CLIENT_ID = ""              #在SIoT上，CLIENT_ID可以留空
IOT_UserName ='scope'        #用户名
IOT_PassWord ='scope'     #密码
topic_id= 'af88/a0' # 设备名称

w=20 #设置数据的长度,避免图表越来越小
x,y=[0],[0]
flag=False

# 收到消息后存入字典，记录时间
def on_subscribe(client,userdata,msg):
    global y,flag
    t=time.asctime(time.localtime(time.time()))
    print("\nTopic:" + str(msg.topic) + " Message:" + str(msg.payload) + " Time:" + t)
    y.append(int(msg.payload))
    flag=True

# 绘图
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
def draw():
    global x,y,flag,w
    plt.axis([0, 100, 0, 1])
    plt.ion()
    x.append(len(y))
    if len(x)>w:
        x.pop(0)
        y.pop(0)
    ax.cla() 
    plt.plot(x,y,'r--')
    plt.pause(0.0001)
    plt.show()
    flag=False

siot.init(CLIENT_ID, SERVER, user=IOT_UserName, password=IOT_PassWord)
siot.connect()
siot.subscribe(topic_id, on_subscribe)
siot.loop()

while True:
    if flag:
        draw()
    time.sleep(1)


