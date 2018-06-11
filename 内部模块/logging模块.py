#creat with :PyCharm
#Author:Wilson
#Date:2018/5/16
#Time:14:06

# import logging
#
# logging.debug('debug message')
# logging.info('info message')
# logging.warning('warning message')
# logging.error('error message')
# logging.critical('critical message')

# 输出：
# WARNING:root:warning message
# ERROR:root:error message
# CRITICAL:root:critical message

# 可见，默认情况下Python的logging模块将日志打印到了标准输出中，且只显示了大于等于WARNING级别的日志，
# 这说明默认的日志级别设置为WARNING
# 日志级别等级CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET
# 默认的日志格式为日志级别：Logger名称：用户输出消息。

print("灵活配置日志级别，日志格式，输出到指定位置（可以输出到屏幕，文件等）")
# 二  灵活配置日志级别，日志格式，输出位置

import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='test.log',
                    filemode='a')  #文件模式为a，appen添加

logging.debug('new debug message')
logging.info('new info message')
logging.warning('new warning message')
logging.error('new error message')
logging.critical('new critical message')

# 文件内输出的内容：
# Wed, 16 May 2018 14:52:44 logging模块.py[line:32] DEBUG debug message
# Wed, 16 May 2018 14:52:44 logging模块.py[line:33] INFO info message
# Wed, 16 May 2018 14:52:44 logging模块.py[line:34] WARNING warning message
# Wed, 16 May 2018 14:52:44 logging模块.py[line:35] ERROR error message
# Wed, 16 May 2018 14:52:44 logging模块.py[line:36] CRITICAL critical message

# 可见在logging.basicConfig()函数中可通过具体参数来更改logging模块默认行为，可用参数有
# filename：用指定的文件名创建FiledHandler（后边会具体讲解handler的概念），这样日志会被存储在指定的文件中。
# filemode：文件打开方式，在指定了filename时使用这个参数，默认值为“a”还可指定为“w”。
# format：指定handler使用的日志显示格式。
# datefmt：指定日期时间格式。
# level：设置rootlogger（后边会讲解具体概念）的日志级别
# stream：用指定的stream创建StreamHandler。可以指定输出到sys.stderr,sys.stdout或者文件(f=open('test.log','w'))，默认为sys.stderr。若同时列出了filename和stream两个参数，则stream参数会被忽略。
#
# format参数中可能用到的格式化串：
# %(name)s Logger的名字
# %(levelno)s 数字形式的日志级别
# %(levelname)s 文本形式的日志级别
# %(pathname)s 调用日志输出函数的模块的完整路径名，可能没有
# %(filename)s 调用日志输出函数的模块的文件名
# %(module)s 调用日志输出函数的模块名
# %(funcName)s 调用日志输出函数的函数名
# %(lineno)d 调用日志输出函数的语句所在的代码行
# %(created)f 当前时间，用UNIX标准的表示时间的浮 点数表示
# %(relativeCreated)d 输出日志信息时的，自Logger创建以 来的毫秒数
# %(asctime)s 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
# %(thread)d 线程ID。可能没有
# %(threadName)s 线程名。可能没有
# %(process)d 进程ID。可能没有
# %(message)s用户输出的消息

# http://www.cnblogs.com/yuanchenqi/articles/5732581.html
import logging

logger = logging.getLogger()
# 创建一个handler，用于写入日志文件
fh = logging.FileHandler('test.log')

# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh) #logger对象可以添加多个fh和ch对象
logger.addHandler(ch)

logger.debug('logger debug message')
logger.info('logger info message')
logger.warning('logger warning message')
logger.error('logger error message')
logger.critical('logger critical message')
