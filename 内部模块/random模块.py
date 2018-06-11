#creat with :PyCharm
#Author:Wilson
#Date:2018/5/16
#Time:12:05

import random
#随机数
print(random.random())       #默认0-1之间的小数----float
print(random.randint(1,2))   #1-2之间的整数
print(random.randrange(1,10)) #1-9之间的序列
print(random.choice([1, '23', [4, 5]]))  # 23
print(random.sample([1, '23', [4, 5]], 2))  # [[4, 5], '23']
print(random.uniform(1, 3))  # 1.927109612082716

# example 1:
# 空字符串+一串字符可以合并
a=''+'a'+'b'+'c'
print("字符串合并 '' + 'a' + 'b' + 'c'：",a)

# example 2 生成5位的数字及字母 随机验证码
import random
checkcode = ''
for i in range(5):
    num = random.randrange(0,5)  #取个随机数
    if num != i:                 #取字母
        temp = chr(random.randint(65,90))   # chr()把整数转换为字母 A=‘65’
    else:                        #取数字
        temp = random.randint(0,9)
    checkcode += str(temp)       # 空字符串+一串字符可以合并,见上面example 1
print("随机验证码:",checkcode)

# example 3 生成5位的数字及字母 随机验证码
import random

def v_code():

    code = ''
    for i in range(5):

        num=random.randint(0,9)
        alf=chr(random.randint(65,90))
        add=random.choice([num,alf])
        code += str(add)
    return code

print("example3随机验证码:",v_code())

#随机排序
item=[1,3,5,7,9]
random.shuffle(item)
print(item)

