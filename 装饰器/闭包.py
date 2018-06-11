#creat with :PyCharm
#Author:Wilson
#Date:2018/5/11
#Time:15:06

def outer():
    x = 10
    def inner():
        print(x)
    return inner

# 调用方式1，等同与方式2
f = outer()    # outer（）运行后返回inner（）
f()            #运行inner（）

# 调用方式2--有点奇怪
outer()()

# inner() 是局部变量，全局无法调用

# outer里return的inner是一个“闭包函数”，有x这个变量
# 闭包（closure）是函数式编程的重要的语法结构
# 定义：如果在一个内部函数里，在对外作用域（但不是在全局作用域）的变量进行引用，
#      那么内部函数就被认为是闭包（closure）

# 如上实例，inner就是内部函数，inner里引用了外部作用域的变量x
#         x在外部作用域outer里面，不是全局作用域
#         则这个内部函数inner就是一个闭包。


# 闭包=函数块+定义函数时的环境，inner就是函数块，x就是环境，当然这个环境可以有很多，不止一个简单的x。













