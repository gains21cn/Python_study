# Operate with :PyCharm
# Author:Wilson
# Date:2018/5/28
# Time:9:15

import json
dic1 = {
        "江苏省":{
            "苏州市": {"黄埔区":{"黄河路","人民广场","南京路",},
                    "静安区":{"静安寺","北京西路",},
                    "虹口区":{"大连路":{},"飞虹路":{},"公平路":{},},
                    "杨浦区":{"控江路","周家嘴路","军工路",},},
            "无锡市": {"黄埔区":{"黄河路", "人民广场","南京路",},
                     "静安区": {"静安寺", "北京西路", },
                    "虹口区":{"大连路":{},"飞虹路":{},"公平路":{},},
                    "杨浦区":{"控江路","周家嘴路","军工路",},},
            "常州市": {"黄埔区":{"黄河路","人民广场","南京路",},
                    "静安区":{"静安寺","北京西路",},
                    "虹口区":{"大连路":{},"飞虹路":{},"公平路":{},},
                    "杨浦区":{"控江路","周家嘴路","军工路",},},
            "镇江市": {"黄埔区":{"黄河路","人民广场","南京路",},
                    "静安区":{"静安寺","北京西路",},
                    "虹口区":{"大连路":{},"飞虹路":{},"公平路":{},},
                    "杨浦区":{"控江路","周家嘴路","军工路",},},
        }
}

dic = {'name': 'jacky', 'age': '18'}

data = json.dumps(dic)
json.dump()
f = open('JSON_text', 'w', encoding="utf-8")
f.write(data)
f.close()



