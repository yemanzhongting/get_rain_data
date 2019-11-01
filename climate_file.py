# -*- coding: UTF-8 -*-
__author__ = 'zy'
__time__ = '2019/4/16 20:01'
import os


def file_name(file_dir):

    for root, dirs, files in os.walk(file_dir):
        print(root)  # 当前目录路径
        print(dirs)  # 当前路径下所有子目录
        print(files)  # 当前路径下所有非目录子文件

    print('---------')
    print(files)
    return files

if __name__=='__main__':
    root_source=r'C:\Users\hp\Desktop\气象数据'
    file_list=file_name(root_source)
    path=r'C:\Users\hp\Desktop\java_file'
    # 修改当前工作目录
    os.chdir(path)
    # 查看修改后的工作目录
    retval = os.getcwd()
    print(retval)
    cmds=[]
    for i in file_list:
        print(i)
        i=r'C:\Users\hp\Desktop\气象数据'+'\\'+i
        cmds.append('java -classpath . ishJava'+' '+i+' '+i+'.out')

    for cmd in cmds:
        os.system(cmd)
        print('处理一个')


