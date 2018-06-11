# Operate with :PyCharm
# Author:Wilson
# Date:2018/5/28
# Time:15:59

import json


f = open('JSON_text', 'r')

# data = f.read()             # 读取文件，此时文件是json格式，不能直接查看
# data = json.loads(data)

data = json.load(f)            # 等于上面2行，json.load直接载入并读出文件，可以直接显示

print(data['name'])


