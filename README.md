# 招聘数据分析可视化项目

## 一、项目概述：
本项目是一个基于大数据技术的招聘数据分析可视化预测与推荐系统。 该系统旨在通过对海量招聘数据的分析和挖掘，为企业和求职者提供更准确、高效的招聘信息服务。

！！！**代码来源说明：** ！！！  
本项目的部分代码学习自 B 站，参考**2024Python黑马大数据学习路线图**以及博主**基于大数据招聘数据分析预测推荐系统—免费完整实战教学视频**。感谢 B 站 作者和黑马提供的优质学习资源。  
**[跳转至视频地址](
https://www.bilibili.com/video/BV1nJp7eYEJK?spm_id_from=333.788.videopod.episodes&vd_source=6398974450381c414cb7f772fc9fd742)**
## 二、项目背景：
## 三、数据来源：
[chromedriver.exe](spider%2Fchromedriver.exe)软件爬取的网站：https://www.lagou.com/wn/
## 四、项目结构：
```
- diangoProject/ # diango项目初始化文件，自动生成
- myApp/
    - templates  # 前端Bootstrap模板 
- predict/
    - goPredict.py/  # 预测分析模型
- recommend/
    - goRecommend.py/  # 推荐分析模型
- spider/
    - charmedriver.exe # 爬取软件
    - spider.py/  # 爬虫程序
- static/
    - res/    # 大屏可视化样式
    - static/ # Bootstrap模版样式
- utils/  #数据库操作连接
    - getChartData.py/  
    - getPublicData.py/   
    - qureyhive.py/    
- README.md  # 项目说明文档
- jobData.csv # 数据集
```
## 五、安装与运行
1. **环境要求：**
**大数据集群虚拟机node1、node2、node3地址：** (通过网盘分享的文件：虚拟机
链接: https://pan.baidu.com/s/1hHGL8DA9NqsTNvp37YoRmA?pwd=h5e3 提取码: h5e3 --来自百度网盘超级会员v4的分享)  


2. **安装步骤：**
3. **运行项目：**
    + windows本机配置host修改： 
   ```
   192.168.73.131 node1
   192.168.73.132 node2
   192.168.73.133 node3
   ```
   Linux node1命令行：
   ```
   su hadoop
   启动 hdfs: `start-dfs.sh`
   启动 yarn: `start-yarn.sh`
   启动 hive: 
   cd /export/server
   cd hive
   nohup bin/hive --service metastore >> logs/metastore.log 2>&1 &
   nohup bin/hive --service hiveserver2 >> logs/hiveserver2.log 2>&1 &
   启动thriftserver：
   cd /export/server
   cd spark
   sbin/start-thriftserver.sh --hiveconf hive.server2.thrift.port=10000 --hiveconf hive.server2.thrift.bind.host=node1 --master local[*]
   ```
