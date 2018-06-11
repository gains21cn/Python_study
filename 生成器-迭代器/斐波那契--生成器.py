#creat with :PyCharm
#Author:Wilson
#Date:2018/5/14
#Time:11:58

# 使用yield生成器


def fibo(n):
    a, b = 0, 1

    while n>0:
        yield b
        a,b = b,a+b
        n -= 1
    return "finish"

x = fibo(10)
# 每次输出一个数字
print("用next（）输出前面的数字，有几个next就输出几个")
print(next(x))
print(next(x))
print(next(x))
print(next(x))

print("下面用for循环输出剩余的数字")
for i in x:
    print(i)

