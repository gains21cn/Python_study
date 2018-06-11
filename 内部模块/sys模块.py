#creat with :PyCharm
#Author:Wilson
#Date:2018/5/16
#Time:12:30


import sys
# sys.argv           *****重要，命令行参数List，第一个元素是程序本身路径
# sys.exit(n)        退出程序，正常退出时exit(0)，0是默认参数，其他的是其他异常退出
# sys.version        获取Python解释程序的版本信息
# sys.maxint         最大的Int值
# sys.path           返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
# sys.platform       ***返回操作系统平台名称，跨平台使用时，针对各个系统使用不同语句
# sys.stdout.write('please:')    标准输出
# val = sys.stdin.readline()[:-1]

# example 1 进度条：
import sys,time
for i in range(50):
    sys.stdout.write('>>')
    time.sleep(0.1)  # 0.1秒
    sys.stdout.flush()  # 间隔0.1秒刷新一次，模拟进度条效果，否则就是一下子全部显示
