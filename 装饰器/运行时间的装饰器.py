#creat with :PyCharm
#Author:Wilson
#Date:2018/5/11
#Time:13:23

import time

# 定义显示程序运行时间的show_time函数
def show_time(f):
    start_time = time.time()
    f()
    end_time = time.time()
    print("运行程序用时:%s 秒 \n"%(end_time - start_time))

# 定义func1函数，通过time.sleep()模拟运行了2秒
def func1():
    print("This is function 1.")
    time.sleep(2)

# 定义func2函数，通过time.sleep()模拟运行了3秒
def func2():
    print("This is function 2.")
    time.sleep(3)

# 显示func1的运行时间，函数（函数）方式
show_time(func1)

# 显示func2的运行时间，函数（函数）方式
show_time(func2)

# 此时没用问题，但是我们是通过show_time(f)的方式获取的运行时间，改变了功能函数的调用方式
# 假如我们不要通过show_time(),而是通过func1（）函数自身就能直接获取运行时间呢？
# 请看进化版》》》



