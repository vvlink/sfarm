# 实时监视物联网数据
# 将需要订阅的项目名称加入到project_list中，topic_list不用修改
# 每收到一条消息，将实时打印在界面上。程序关闭不影响物联网系统的正常运行。

import siot,time

SERVER = "192.168.3.122"        #MQTT服务器IP
CLIENT_ID = ""              #在SIoT上，CLIENT_ID可以留空
IOT_UserName ='scope'        #用户名
IOT_PassWord ='scope'     #密码
project_list  = ['af01','af02','af88']   #“topic”为“项目名称/设备名称”
topic_list= ['a0','a2','d4'] # 设备名称

msg_map={} # 存储接收到的数据

# 收到消息后存入字典，记录时间
def on_subscribe(client,userdata,msg):
    global msg_map
    t=time.asctime(time.localtime(time.time()))
    print("\nTopic:" + str(msg.topic) + " Message:" + str(msg.payload) + " Time:" + t)
    msg_map[str(msg.topic)]=[str(msg.payload.decode()),time.time()]

# 读取后不删除
def topic_read(topic):
    global msg_map
    result=msg_map.get(topic,None)
    if result:
        re = result[0]
    return re
def topic_read_time(topic):
    global msg_map
    result=msg_map.get(topic,None)
    if result:
        re = time.asctime(time.localtime(result[1]))
    return re

siot.init(CLIENT_ID, SERVER, user=IOT_UserName, password=IOT_PassWord)
siot.connect()
for item1 in project_list:
    for item2 in topic_list:
        siot.subscribe(item1 +'/'+ item2, on_subscribe)
siot.loop()
