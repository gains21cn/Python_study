# Operate with :PyCharm
# Author:Wilson
# Date:2018/5/28
# Time:16:25

import shelve

f = shelve.open('shelve建立的文件')   # （）内是建立的文件名

f['info'] = {'name': 'jack', 'age': '18'}  # 到这步，直接运行，会生成3个同名的不同后缀的文件


