# Operate with :PyCharm
# Author:Wilson
# Date:2018/5/31
# Time:13:31



#!_*_coding:utf-8_*_
#__author__:"Alex Li"

import os
import sys

# 程序文件主目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)

# 添加环境变量
sys.path.append(BASE_DIR)


from core import main

if __name__ == '__main__':
    main.run()







