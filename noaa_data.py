#本程序下载noaa气象数据，使用网址为国内镜像网站，编辑时间2019.03.14，LJX

import urllib.request  # url request
import os  # regular expression
import re  # dirs
import requests


# 根据网络地址和文件保存地址下载文件
def download(url, path):
    r = requests.get(url)
    print(path)
    with open(path, "wb") as f:
        f.write(r.content)
    f.close()


url = "https://www1.ncdc.noaa.gov/pub/data/noaa/"  # parent url
Station_ID = "580280"  # 站点号
year_start = "1993"  # 数据起始时间
year_end = "2001"
# 时间差，然后根据时间差建立年份数组
year_sub = int(year_end) - int(year_start) + 1

# 建立数据年份数组
years = []
for i in range(year_sub):
    years.append(str(i + int(year_start)).zfill(4))

for i in years:
    # file_names.append(Station_ID+"-99999-"+i+".gz")     #file_names = []
    # urls.append(url+i+"/"+file_names)                   #urls = []
    file_name = Station_ID + "-99999-" + i + ".gz"  # 文件名
    path = './xuzhou2/' + file_name  # 文件存储路径
    url2 = url + i + "/" + file_name  # 文件网络地址URL
    # 判断网页是否为空
    html = requests.get(url2)
    respon = html.status_code
    # 网页为空则跳过本次执行，否则下载文件
    if respon == 404:
        continue
    else:
        download(url2, path)  # 下载文件

'''
XUzHOU

      Period of Record: 1956-08-20 to 2019-03-06  Station ID: 58027099999

XUZHOU/ GUANYIN ARPT

      Period of Record: 1973-11-04 to 2003-10-01  Station ID: 58028099999

XUZHOU/ GUANYIN ARPT

      Period of Record: 1973-11-04 to 2003-10-01  Station ID: 58028099999


      #其它链接
#https://www.ncdc.noaa.gov/data-access
#https://globalweather.tamu.edu/
#ftp://ftp.ncdc.noaa.gov/pub/data/noaa    #另外一个数据库

'''


