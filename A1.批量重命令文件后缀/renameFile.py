# -*- coding: utf-8 -*-
"""
程序功能：批量将【指定文件路径】下的所有 某种特定文件格式 的文件名 修改为 另外一种格式的形式

使用方法：

在命令行下输入
python renameFile.py [必选参数：文件所在路径] [可选参数：原始文件格式 默认为blv] [可选参数：修改后文件格式 默认为mp4]
例如：
python renameFile.py D:\FFOutput\flvfile blv mp4
"""
import os
import sys


def renameFile(targetPath,originFileMode='blv',newFileMode='mp4'):
    #遍历所有文件
    for dir in os.listdir(targetPath):
        #用join方法得到单个文件路径（能调用库还是用库的较为有保障）
        filePath=os.path.join(targetPath,dir)
        #若是文件
        if os.path.isfile(filePath):
            #若是 要修改的文件格式
            if dir[-len(originFileMode):]==originFileMode:
                pathBefore=os.path.join(targetPath,dir)
                pathAfter=os.path.join(targetPath,dir[:-len(originFileMode)]+newFileMode)
                #重命令文件
                os.rename(pathBefore,pathAfter)

                
#文件路径
targetPath=sys.argv[1]
if len(sys.argv)==4:
    #原始文件格式
    originFileMode=sys.argv[2]
    #修改后的文件格式
    newFileMode=sys.argv[3]
    renameFile(targetPath,originFileMode,newFileMode)
else:
    renameFile(targetPath)