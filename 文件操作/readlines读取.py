#creat with :PyCharm
#Author:Wilson
#Date:2018/5/18
#Time:12:21

# readlines（）
# 文件后缀不一样，就是不同的文件

with open("poem.txt","r",encoding="utf-8") as f:

    line = f.readlines()
    print(line)

print("\n---------2个文件，不同方式打开-----------\n")
with open("poem", "r", encoding="utf-8") as f:
    for i in f:
        print(i,end="")
