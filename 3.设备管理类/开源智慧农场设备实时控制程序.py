# 开源智慧农场物联网设备实时控制
# 实时监视多个项目的物联网数据，并输出；
# 根据预设的阈值，对所有项目的设备进行控制。

import siot,time

SERVER = "192.168.3.41"        #MQTT服务器IP
CLIENT_ID = ""              #在SIoT上，CLIENT_ID可以留空
IOT_UserName ='scope'        #用户名
IOT_PassWord ='scope'     #密码

# 定义项目名称和数据阈值，不同的项目可以设置不同的阈值
project_dict={'sf01':500,'sf02':'500'\n'sf03':500\n'sf88':600}

# 设备名称，前面是要订阅的设备（传感器），后面是要控制的设备（电磁阀）
topic_list= ['a1','d2'] 

msg_map={} # 存储接收到的数据

# 收到消息后存入字典，记录时间
def on_subscribe(client,userdata,msg):
    global msg_map
    t=time.asctime(time.localtime(time.time()))
    print("\nTopic:" + str(msg.topic) + " Message:" + str(msg.payload) + " Time:" + t)
    msg_map[str(msg.topic)]=[str(msg.payload.decode()),time.time()]

# 读取后删除
def topic_read(topic):
    global msg_map
    result=msg_map.get(topic,None)
    if result:
        re = result[0]
        del msg_map[topic]
        return re
    return result

siot.init(CLIENT_ID, SERVER, user=IOT_UserName, password=IOT_PassWord)
siot.connect()

# 订阅消息
for item in project_dict.keys():
    siot.subscribe(item +"/"+ topic_list[0], on_subscribe)
siot.loop()

# 通过循环读出数值，和阈值比较后判断是否发送控制指令

temp_id = ''
while True:
    for item in project_dict.keys():
        temp_id = item +'/'+ topic_list[0]
        val = topic_read(temp_id)
        if val:
            default_val = project_dict.get(item,None)
            if int(val) > int(default_val):
                # 发送控制指令
                siot.publish(item +'/'+ topic_list[1],"1")
                print(('项目：%s的监测数据为%s，超过预设值%s，已经发送控制指令！')%(item,val,default_val))
    time.sleep(1) #等待1秒钟继续
