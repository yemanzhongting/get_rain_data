# get_rain_data
论文中气象站数据获得与处理
http://bbs.06climate.com/forum.php?mod=viewthread&tid=50500
http://bbs.06climate.com/forum.php?mod=viewthread&tid=50500
参考资料
NOAA（美国海洋和大气管理局）提供GHCND（全球历史气候学网络）月度摘要数据库，可以满足全球陆地区域历史月度温度，降水和降雪记录的研究需求。
GHCND月度摘要数据库数据源自GHCN-Daily数据库，经过质量审查与二次加工制成，主要包含18个气象要素，包括温度（每月平均值和极端值），降水（每月总数，极端值和满足各种数量阈值的天数），降雪，最大雪深等。GHCND月度摘要数据库与它对应的每日数据库一样，包含分布在各大洲的40000多个站点的数十个观测值。
基于世界气象组织（WMO）第40号决议（Cg-12），世界气象组织（WMO）达成了世界天气监视计划协议，互相交换气象数据，GHCN-Daily数据库提供的数据即基于此计划。WMO成员国可以免费且不受限制的使用或导出数据用于研究，教育和其他非商业活动。
数据库镜像连接：https://www1.ncdc.noaa.gov/pub/data/noaa/。
本节以台风山竹期间获取广东省内数据绘制降雨情况为例。点击数据库连接会得到以下文件列表，提供从1901年至今的气象数据，操作步骤如下：

 ![Image text](https://github.com/yemanzhongting/get_rain_data/blob/master/%E5%9B%BE/1.png)
 
（1）	在文件列表中找到ish-history.csv文件，文件提供了29726个气象站点，包含站点ID，站点经纬度，站点高程，站点所在城市，站点所在国家（CH代表中国），站点数据起迄时间。根据需求在excel内进行查找，筛选出想要的数据站点。从中筛选出具有2018年9月16日至9月18日数据的38个广东省范围内数据站。
（2）	点进2018年份文件夹，将筛选后的数据站原始数据下载下来并解压。对解压后的文件进行处理，此时解压出来的文件名称格式如“578660-99999-2018”，579570代表站点ID，99999是统一的命名，2018代表数据年份。此时文件并不能直接使用，官方提供了解析脚本ishJava.java，需要安装JDK环境使用，并在同路径下添加ishJava.class类，cmd下执行命令java -classpath . ishJava 578660-99999-2019 578660-99999-2010.out。这里提供了编写好的脚本，调用deal_with_download_file(root_source)函数即可处理路径下所有文件，输出成.out格式。

![Image text2](https://github.com/yemanzhongting/get_rain_data/blob/master/%E5%9B%BE/2.png)

（3）	此时提供的数据是2018年一整年的数据，依据时间条件进行过滤，调用函数filter_time(root_source, 201809160000, 201809170000)筛选出三天的气象数据，得到筛选后的结果result.txt。
（4）	依据处理结果进行筛选，Arcgis处理后得到降雨插值图。
![Image text](https://github.com/yemanzhongting/get_rain_data/blob/master/%E5%9B%BE/3.jpg)
(5)持续至今的气象站点
![Image text](https://github.com/yemanzhongting/get_rain_data/blob/master/%E5%9B%BE/station.jpg)

Ref: 张岩,李英冰,郑翔.基于微博数据的台风“山竹”舆情演化时空分析[J].山东大学学报(工学版),2020,50(05):118-126.
