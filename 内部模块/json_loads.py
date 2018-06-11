# Operate with :PyCharm
# Author:Wilson
# Date:2018/5/28
# Time:13:56

import json

f = open('JSON_text', 'r')  # 打开文件
data = f.read()             # 读取文件，此时文件是json格式，不能直接查看

json.loads(data)            # json载入文件，才可以显示

print(data)


