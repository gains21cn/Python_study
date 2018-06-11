#creat with :PyCharm
#Author:Wilson
#Date:2018/5/14
#Time:14:31

#通过yield实现伪并发

import time

def consumer(name):
    print("%s 准备吃包子啦！" %name)
    while True:
        baozi = yield

        print("包子【%s】来了，被【%s】吃了！"%(baozi,name))

def producer(name):
    c1 = consumer("A")
    c2 = consumer("B")
    c1.__next__()
    c2.__next__()
    print("我开始准备做包子啦！")

    for i in range(10):
        time.sleep(1)
        print("做了2个包子！")
        c1.send(i)
        c2.send(i)

producer("Alex")