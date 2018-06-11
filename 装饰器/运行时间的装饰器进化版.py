#creat with :PyCharm
#Author:Wilson
#Date:2018/5/11
#Time:13:40

import time

def show_time(f):
    def inner():
        start_time = time.time()
        f()
        end_time = time.time()
        print("运行程序用时:%s 秒\n"%(end_time - start_time))
    return inner

def func1():
    print("This is function 1.")
    time.sleep(2)
# func1 = show_time(func1)  #不能空格，要顶行，与def平等。也可以写在运行函数的上面（见26行），也可参考21行 @show_time。

@show_time     #等同与 func2 = show_time(func2)
def func2():
    print("This is function 2.")
    time.sleep(3)

# show_time(func1)的值 就是inner函数
t = show_time(func1) #<function show_time.<locals>.inner at 0x0000000002994C80>
print("这是show_time(func1)的值：",t,"\n")

# 把inner函数赋值到func1函数，就是运行了inner（func1）
func1 = show_time(func1)  # 也可以放到func1函数下,见19行
func1()    # 等于执行了 inner 函数


func2()




