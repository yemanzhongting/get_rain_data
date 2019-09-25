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

if __name__=="__main__":
    dir=r'C:\Users\hp\Desktop\气象数据'
    files=file_name(dir)
    df=pd.read_excel('筛选工作站.xlsx')
    #df.set_index('STATION_ID')
    print(df)
    sta=[]
    lat=[]
    lng=[]
    for i in files:
        name=i[0:6]
        STATION_ID__num=int(name)
        #print(df[df.STATION_ID == STATION_ID__num].LONGITUDE)
        sta.append(STATION_ID__num)

        lat.append(df[df.STA_ID == STATION_ID__num].LAT)
        lng.append(df[df.STA_ID == STATION_ID__num].LNG)

    for j in range(len(sta)):
        print('站'+str(sta[j])+'lat'+str(lat[j])+'lng'+str(lng[j]))

    ########处理文件的#￥#####文本格式
    file_dir=r'E:\climate'
    rain_data_file_list=file_name(file_dir)
    contents=[]
    for i in rain_data_file_list:
        temp_dir=file_dir+'\\'+i
        for row in open(temp_dir):
            print('处理一行')
            try:
                Time = int(row[13:25])
                if Time > 201809160000 and Time < 201809180000:
                    contents.append(row)
            except ValueError:
                pass

    #content = [row for row in open(file_dir)]
    #print(result)
    with open('result.txt','w+',encoding='utf-8') as f:
        for i in contents:
            # if int(i[0:6]) in sta:
            #     index_sta=sta.index(int(i[0:6]))
            #     f.write(i+' '+str(lat[index_sta])+' '+str(lng[index_sta]))
            f.write(i)





