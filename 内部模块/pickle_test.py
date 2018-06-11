# Operate with :PyCharm
# Author:Wilson
# Date:2018/5/28
# Time:15:47


import pickle


def foo():
	print('this is a function.')

data = pickle.dumps(foo)

f = open('pickle_text', 'wb')  # 注意这里是wb，2进制写入
f.write(data)
f.close()

# pickle_text内容如下：

# �c__main__
# foo
# q .





