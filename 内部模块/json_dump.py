# Operate with :PyCharm
# Author:Wilson
# Date:2018/5/28
# Time:9:15

import json
dic = {'name': 'jacky', 'age': '18'}
f = open('JSON_text2', 'w', encoding="utf-8")

# data = json.dumps(dic)
# f.write(data)

json.dump(dic, f)  # 这里用dump，等于上面的2行，dumps序列化及文件写入
# 注意这里的写法和dumps不同，多了一个f句柄，代表f.write()

f.close()



