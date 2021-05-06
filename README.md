# 开源智慧农场项目说明


开源智慧农场（Sfarm）是一个基于MQTT协议开发的，能实现数据采集和远程浇水控制的物联网种植系统。系统采用分布式设计理念，以无线的方式随时随处接入智能终端节点，部署方便，扩展性强。系统基于国产开源硬件设计，兼容创客空间中常见的电子模块，开放协议接口，支持二次开发。学生既可以利用各种数据进行科学探究，也可以自主编程，深度参与系统的功能设计。

Sfarm中的“s”，指科学、简单、学校、STEM等。

- 一个和科学（Science）教育相关的（数据采集、分析）的农场；
- 一个承载中小学STEAM教育的农场；
- 一个结合智慧教育（Smart）的农场；
- 一个小型（Small）的农场；
- 一个简易（Simple）的农场；
- 一个为学校（School）设计的农场；
- 一个基于虚谷物联平台（SIoT）应用的农场。

核心特色：一个学生可以深度参与的开源智慧农场项目

GitHub地址：https://github.com/vvlink/sfarm

码云地址：https://gitee.com/vvlink/sfarm

## 1.功能说明

- 能够实时上传环境数据（光线、土壤湿度等）到服务器；
- 能够根据土壤湿度阈值，自行打开电磁阀浇水；
- 能够实时接受来自物联网的“浇水”指令，打开电磁阀；
- 所有的数据可以导出为Excel格式，供后期分析；
- 采用标准协议，开放编程接口，支持二次开发；
- 支持无限扩容，可以随时接入新的智能终端。

## 2.搭建说明

### 2.1 准备工作

每一个终端接入的位置，留水电接口。其中水管留4分的内牙（可接三角阀），电源则留防水插座（或者提供航空插头）即可。基于安全考虑，所有的水电都有独立的电源开关（建议加带漏电保护的空气开关）和水阀门（三角阀）。

提供Wi-Fi环境。如果接入的智能终端较多，需要配置企业级的无线路由器。基于安全考虑，请采用独立的Wi-Fi环境。如果需要做互联网的应用，则需要能够访问外网。

### 2.2 涉及硬件

以虚谷计划中的硬件项目为主，如虚谷号、掌控板，采用Arduino兼容的各种传感器、执行器模块。

## 3.资源说明

开源智慧农场是一个完全开放的项目，程序都在不断增加迭代中。下面罗列的程序中，带*的为已经完成的代码。考虑到之前的学生都学过VB，部分代码用VB来编写。

### 3.1 核心软件类

1）服务器类

- SIoT管理软件*
- SIoT智慧农场插件*

2）工具类

- vvBlock
- Mind+
- mPython

### 3.2 智能终端类

- 虚谷号代码
- 掌控板代码

### 3.3 设备管理类

- 提供各种用Python、VB、App inventor、Mind+等软件编写的小程序，能够自动或者手动控制设备。

### 3.4 数据观察类

- 提供各种用Python、VB、App inventor、Mind+等软件编写的小程序，能够监视各种数据，做可视化处理。

### 3.5 创新应用类

- 提供各种用Python、VB、App inventor、Mind+等软件编写的小程序，实现各种有趣的物联网应用。如，数字孪生的花盆、语音管理手机端（App inventor）、数据仪表盘（Node-red）等。

## 4. 项目发起、维护人员

- 谢作如（浙江省温州中学）
- 夏青（上海蘑菇云）
- 钱旭鸯（杭州师范大学）
- 林屹立（温州博识创客STAEM公园）
- 卢华军（福州连江五中）
- ……

## 5.参考资料

1）SIoT使用手册

https://siot.readthedocs.io/

2）虚谷号使用文档

https://vvboard.readthedocs.io/

