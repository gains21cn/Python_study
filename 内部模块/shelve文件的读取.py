# Operate with :PyCharm
# Author:Wilson
# Date:2018/5/28
# Time:16:36

import shelve

f = shelve.open(r'shelve建立的文件')   # （）内是要打开的文件名
# 注意这里的r，是防止文件名或目录内的\n等产生歧义

# f['info'] = {'name': 'jack', 'age': '18'}  # 到这步，直接运行，会生成3个同名的不同后缀的文件

data = f.get('info')  # 通过get（‘键值’）取出结果
print(data)    # {'name': 'jack', 'age': '18'}

