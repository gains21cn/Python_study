# Operate with :PyCharm
# Author:Wilson
# Date:2018/5/18
# Time:16:29

# -*- UTF-8 -*-
from urllib import request
from bs4 import BeautifulSoup
import os
import time, threading


exe_Count = 1
aList = []


def CallView(url, timeout, directoryPath,exe_count):
    try:
        listAvalue = []
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2716.5 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
        }
        rep = request.Request(url, headers=headers)
        response = request.urlopen(rep, timeout=timeout)
        soup = BeautifulSoup(response, 'lxml')
        # 获取a标签href 属性并写入list
        for a in soup.find_all("a"):
            if a.string is None:
                continue
            if not a.attrs["href"].strip() in aList:
                aList.append(a.attrs["href"].strip())
                listAvalue.append([a.string.strip()[0:11], a.attrs["href"].strip()])
            else:
                continue
        # 创建不存在的目录
        if not os.path.exists(directoryPath):
            os.mkdir(directoryPath)
        print("新目录：" + directoryPath)
        # 开启线程递归
        thread = threading.Thread(target=ForRequest, args=(listAvalue, timeout, directoryPath,exe_count))
        thread.start()
        listImgSrc = []
        # 获取img标签 并下载
        for img in soup.find_all("img"):
            try:
                imgSrc = img.attrs["src"]
                print(imgSrc)
                # 过滤重复src
                if not imgSrc in listImgSrc:
                    listImgSrc.append(imgSrc)
                    # 读取图片
                    rep = request.Request(imgSrc)
                    response = request.urlopen(rep, timeout=timeout)
                    # 写入图片
                    filepath = directoryPath + "/" + imgSrc.split('/')[len(imgSrc.split('/')) - 1]
                    with open(filepath, "wb") as o:
                        o.write(response.read())
            except:
                print("访问图片或者写入本地Error")
    except request.HTTPError as e:
        print(e.code)
    except:
        print("CallView Error")


def ForRequest(listA, timeout, directoryPath,exe_count):
    print("当前已执行：" + str(exe_count) + " 次")
    #调用次数超过200跳出
    if exe_count == 200:
        thread = threading.current_thread()
        raise SystemError("正在停止线程")
    else:
        exe_count = exe_count + 1

    for info in listA:
        directoryChildPath = directoryPath + "/" + info[0]
        if not os.path.exists(directoryChildPath):
            os.mkdir(directoryChildPath)
        CallView(info[1], timeout, directoryChildPath, exe_count)

try:
    print("爬虫开始活动了")
    CallView("http://www.ssss18.com/p05/index.html", 15000, "./output", exe_Count)
    print("爬虫正在偷偷活动,不要着急哦！")
except:
    print("Error")


