# Operate with :PyCharm
# Author:Wilson
# Date:2018/5/28
# Time:15:59

import pickle

def foo():
	print("这里要新建这个函数，以前的foo（）的定义就不能用了")

f = open('pickle_text', 'rb')  # rb，2进制读
data = f.read()             # 读取文件，此时文件是json格式，不能直接查看

data = pickle.loads(data)            # json载入文件，才可以显示

data()
# 此处需要新建foo（）函数，否则报错
# ttributeError: Can't get attribute 'foo' on <module '__main__' from 'D:/python/内部模块/pickle_loads.py'>



