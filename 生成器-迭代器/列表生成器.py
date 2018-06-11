#creat with :PyCharm
#Author:Wilson
#Date:2018/5/12
#Time:10:59

a = [x for x in range(10)]
print(a)

#还可以放函数
def f(n):
    return n**2             #取平方

b = [f(x) for x in range(10)]   # range赋值给x，x给f(x)函数
print(b)

# 列表操作，[起始位：结束位：步进]，注意：起始位：结束位，顾头不顾尾，步进默认为1
# 步进为负数，则为从后往前
a=[1,2,3,4,5]
print("列表的值为：",a)

x=a[1:5:1] #从该index位置开始到5（不包括5）取值
print(x)
# [2, 3, 4, 5]

y=a[1]  #只写一位就是按index取值
print(y)
#2

y=a[1:]  #加：从该index位置开始取值
print(y)
#[2, 3, 4, 5]

y=a[:]  #：全部取值
print(y)
# [1, 2, 3, 4, 5]

z=a[::-1]
print(z)
# [5, 4, 3, 2, 1]
