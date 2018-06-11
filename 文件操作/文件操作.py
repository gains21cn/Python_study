#creat with :PyCharm
#Author:Wilson
#Date:2018/5/4
#Time:12:05
import time

file = open("poem","r",encoding="utf8") #读出文件
# 文件读出到内存，操作文件
# 并不会影响到磁盘中的文件

# 在第6行末尾加上一句话
number = 0
for i in file:
    number += 1
    if number == 6:
       i="***此处可以是空字符".join([i.strip(),"-***这里一定要有内容，可以是空字符"])
       #join的格式="".join([i."添加的文本"])，注意join()内要用[]括起来
    print(i.strip())
file.close()  #文件打开后要关闭


#-------------------------可爱的分割线-------------------------------------
print ("-------------------------可爱的分割线-------------------------------------")

file = open("poem","r",encoding="utf8") #读出文件
data =file.readlines()  #readlines()会将所有的文件都导入内存，不要用这种方法
for j in data:
    print(j.strip())
file.close()  #文件打开后要关闭

#-------------------------可爱的分割线-------------------------------------
print ("-------------------------可爱的分割线-------------------------------------")
file = open("poem","r+",encoding="utf8") #读出文件
print(file.tell()) #当前指针的位置
print(file.read(3))#read（）读几个字符  英文为1个字符，中文为3个字符
print(file.tell())#当前指针的位置

file.seek(1) #指针重新回到第1位后
print(file.tell()) #当前指针的位置
file.write("\n %s "%time.ctime()) #本来用seek回到第1位后，应该添到其后，但是依然加到最后，说明：读和写的位置是不相关的
print(file.read(3))#read（）读几个字符  英文为1个字符，中文为3个字符
print(file.tell())
