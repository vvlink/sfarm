# SIoT

### 简介

SIoT为一个为教育定制的跨平台的MQTT服务器程序，S指科学（Science）、简单（simple）的意思。SIoT支持Win10、Win7、Mac、Linux等操作系统，一键启动，无需注册即可使用。

SIoT为“虚谷物联”项目的核心软件，是为了帮助中小学生理解物联网原理，并且能够基于物联网技术开发各种创意应用，尤其是用于科学数据采集。

SIoT采用GO语言编写，最大的特点为跨平台，一键运行。只要启动这一程序，普通电脑就可以成为MQTT服务器。利用自定义的Topic，SIoT将自动建立项目名称和设备名称，方便管理。所有的物联网消息可以根据需要导出为各种格式，用于后期分析。

### 特性
1. 跨平台。支持Win10、Win7、Mac、Linux等操作系统。只要启动这一程序，普通计算机（包括拿铁熊猫、虚谷号和树莓派等微型计算机）就可以成为标准的MQTT服务器。
2. 一键运行。纯绿色软件，不需要安装，下载后解压就可以使用，对中小学的物联网技术教学尤其适合。
3. 使用简单。软件运行后，不需要任何设置就可以使用。利用特定的“Topic”的名称（“项目名称/设备名称”），就能自动在数据库中添加项目和设备的名称，并将消息数据存入数据库。
4. 支持数据导出。所有的物联网消息数据都可以在线导出，系统采用SQLite数据库，同时支持MySql数据库。
5. 支持WebAPI。系统系统了完善的WebAPI，方便各种软件以HTTP的方式调用，支持App inventor、Scratch、VB等默认不支持MQTT的中小学生常用编程软件调用。
6. 支持插件开发。
7. QoS级别为0。

### 最新版本

1.3

### 插件使用

解压后覆盖到siot的相应目录下。

### SIoT软件资源（最新）下载地址

- http://mindplus.dfrobot.com.cn/siot
- https://github.com/vvlink/SIoT/tree/master/software/
- https://gitee.com/vvlink/SIoT/tree/master/software/

### SIoT文档的阅读地址

  https://siot.readthedocs.io/
