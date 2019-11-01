# -*- coding: UTF-8 -*-
__author__ = 'zy'
__time__ = '2019/4/16 22:40'
import pandas as pd
import os

def file_name(file_dir):

    for root, dirs, files in os.walk(file_dir):
        print(root)  # 当前目录路径
        print(dirs)  # 当前路径下所有子目录
        print(files)  # 当前路径下所有非目录子文件

    print('---------')
    print(files)
    return files

def deal_with_download_file(root_source):
    #函数处理一下解压后的数据转换成out文件
    # root_source为解压后数据所在路径
    # path为java代码所在路径以及out文件输出路径

    file_list = file_name(root_source)

    # 修改当前工作目录
    os.chdir(root_source)
    # 查看修改后的工作目录
    retval = os.getcwd()
    print(retval)

    cmds = []
    for i in file_list:
        try:
                print(i)
                #判断是否为解压后的原始数据  i = root_source+ '\\' + i
                cmds.append('java -classpath . ishJava' + ' ' + i + ' ' + i + '.out')
        except:
            pass

    for cmd in cmds:
        os.system(cmd)
        print(cmd)
        print('处理一个')

def filter_time(root_source,start_time,end_time):
    #依据时间过滤文件
    #root_source out文件目录
    #start_time,end_time 需要开始结束时间，如201809180000，格式为整数
    rain_data_file_list=file_name(root_source)
    contents=[]
    for i in rain_data_file_list:
        try:
            if i.split('.')[1]=='out':
                #判断是否是输出文件
                temp_dir=root_source+'\\'+i
                for row in open(temp_dir):
                    print('处理一行')
                    try:
                        Time = int(row[13:25])
                        if (Time > start_time or Time ==start_time) and Time < end_time:#201809180000
                            contents.append(row)
                        #拿出符合时间筛选的内容
                    except ValueError:
                        pass
        except:
            pass

    with open('result.txt','w',encoding='utf-8') as f:
        for i in contents:
            f.write(i)

def find(root_source,select_station_excel):
    # 检索所有待处理的文件
    df = pd.read_excel(select_station_excel)
    print(df)
    sta = []
    lat = []
    lng = []
    rain_data_file_list=file_name(root_source)
    for i in rain_data_file_list:
        name = i[0:6]
        STATION_ID__num = int(name)
        # 检索处理后的数据、筛选想要的站点
        sta.append(STATION_ID__num)
        a=df[df.STA_ID == STATION_ID__num].LAT
        if a not in lat:
            lat.append(a)
        b=df[df.STA_ID == STATION_ID__num].LNG
        if a not in lat:
            lng.append(b)

    for j in range(len(sta)):
        print('站' + str(sta[j]) + 'lat' + str(lat[j]) + 'lng' + str(lng[j]))

if __name__=="__main__":
    #root_source=r'C:\Users\hp\Desktop\datadeal\气象数据\原始数据'
    # files=file_name(root_source)
    root_source=r'C:\Users\hp\Desktop\台风山竹广东示例\原始数据'
    #deal_with_download_file(root_source)


    select_station_excel='筛选工作站.xlsx'

    filter_time(root_source, 201809160000, 201809170000)
    #筛选出来我们想要的行列

    #find(root_source, select_station_excel)






