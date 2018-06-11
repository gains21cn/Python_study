#creat with :PyCharm
#Author:Wilson
#Date:2018/5/12
#Time:16:17

b = [x*x for x in range(10)]   # range赋值给x，x给f(x)函数
print("列表生成器",b)


b = (x for x in range(10))   # range赋值给x，x给f(x)函数
print("\n生成器")
print(b)
#每用一次就只取一个值
print(next(b))    #等价与 b.__next__()
print(b.__next__())
print(next(b))
