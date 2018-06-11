#creat with :PyCharm
#Author:Wilson
#Date:2018/5/18
#Time:12:14

# readline（）
with open("poem.txt","r",encoding="utf-8") as f:
    # 只能读取一行
    line = f.readline()
    print(line)

    # while循环全部读出
    while True:
        line = f.readline()
        if not line:
            break
        print(line,end="") #加end=""是为了避免print自动换行，也可以删除end=""看看效果