#creat with :PyCharm
#Author:Wilson
#Date:2018/5/11
#Time:14:44

# 接进化版，这版需求是除了打印时间外，还需要输入日志（可选择输出或不输出）
import time

def logger(flag):
    def show_time(f):
        def inner(*x):
            start_time = time.time()
            f(*x)
            end_time = time.time()
            print("运行程序用时:%s 秒"%(end_time - start_time))

            if flag == "true":
                print("日志处理程序》》》...... \n")

        return inner
    return show_time

#flag为true时，运行“日志处理程序”
@logger("true")
def add(*x):
    sums = 0
    for i in x:
        sums += i
    print("函数add的值为：",sums)
    time.sleep(2)

# flag为其他，除了原来的运行时间外，其他什么也不做
@logger("ddddd")
def func2():
    print("This is function 2.")
    time.sleep(3)

#运行函数add（），里面的值不定项，要用*x
add(1,2,3,4,5)

#运行函数func2（）
func2()



