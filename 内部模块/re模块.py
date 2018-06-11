# creat with :PyCharm
# Author:Wilson
# Date:2018/5/18
# Time:10:38

# 就其本质而言，正则表达式（或 RE）是一种小型的、高度专业化的编程语言，
# 在Python中,它内嵌在Python中，并通过 re 模块实现。
# 主要作用：匹配字符串
# 正则表达式模式被编译成一系列的字节码，然后由用 C 编写的匹配引擎执行。

# 字符匹配（普通字符，元字符）：
# 1 普通字符：大多数字符和字母都会和自身匹配
import re

a = re.findall('yuan', 'yuanaleSxalexwupeiqi')
print("re.findall('abc{1,4}', 'abccc')的值", a)  #['yuan']

# 2   元字符：. ^ $ * + ? { } [ ] | ( ) \
# 2.1 元字符之. ^ $ * + ? { }
# '.'     默认匹配除\n之外的任意一个字符，若指定flag DOTALL,则匹配任意字符，包括换行
# '^'     匹配字符开头，若指定flags MULTILINE,这种也可以匹配上(r"^a","\nabc\neee",flags=re.MULTILINE)
# '$'     匹配字符结尾，或e.search("foo$","bfoo\nsdfsf",flags=re.MULTILINE).group()也可以
# '*'     匹配*号前的字符0次或多次，re.findall("ab*","cabb3abcbbac")  结果为['abb', 'ab', 'a']
# '+'     匹配前一个字符1次或多次，re.findall("ab+","ab+cd+abb+bba") 结果['ab', 'abb']
# '?'     匹配前一个字符1次或0次
# '{m}'   匹配前一个字符m次
# '{n,m}' 匹配前一个字符n到m次，re.findall("ab{1,3}","abb abc abbcbbb") 结果'abb', 'ab', 'abb']
# '|'     匹配|左或|右的字符，re.search("abc|ABC","ABCBabcCD").group() 结果'ABC'
# '(...)' 分组匹配，re.search("(abc){2}a(123|456)c", "abcabca456c").group() 结果 abcabca456

ret=re.findall('a..in','helloalvin')
print("re.findall('a..in','helloalvin')的值：",ret)   #['alvin']


ret=re.findall('^a...n','alvinhelloawwwn')
print("re.findall('^a...n','alvinhelloawwwn')的值：",ret)#['alvin']


ret = re.findall('a...n$', 'alvinhelloawwwn')
print("re.findall('a...n$', 'alvinhelloawwwn')的值：",ret)  # ['awwwn']

ret = re.findall('a.n$', 'a无nhelloawa点n')  #$必须在末尾才可以匹配
print("re.findall('a...n$', 'a无nhelloawa点n')的值：",ret)  # ['a点n']

# * [0,+oo]
ret = re.findall('abc*', 'abxcbc')  # *贪婪匹配[0,+oo]
print("re.findall('abc*', 'abxcbc')的值：",ret)  # ['ab']

ret = re.findall('abc*', 'abccbc')  # 贪婪匹配[0,+oo]
print("re.findall('abc*', 'abccbc')的值：",ret)  # ['abcc']

# + [1,+oo]
ret = re.findall('abc+', 'abccc')  # +[1,+oo]
print("re.findall('abc+', 'abccc')的值：",ret)  # ['abccc']

# ? [0,1]
ret = re.findall('abc?', 'abccc')  # ?[0,1]
print("re.findall('abc?', 'abccc')的值：",ret)  # ['abc']


ret = re.findall('abc{1,4}', 'abccccccccc')             # {1,}  1，可以代表1到+oo
print("re.findall('abc{1,4}', 'abcccccccc')的值：",ret)  # 指定能匹配的个数或范围，['abccc'] 贪婪匹配

# 前面的*,+,?等都是贪婪匹配，也就是尽可能匹配，后面加?号使其变成惰性匹配
ret=re.findall('abc*?','abcccccc')
print("re.findall('abc*?','abcccccc')的值：", ret)  # ['ab']

# []字符集
ret=re.findall('a[b,c,d]e', 'abeaceadeabcde')
print("re.findall('a[b,c,d]e', 'abeaceadeabcde')的值：", ret)  # ['abe', 'ace', 'ade']

ret=re.findall('[a-z]', 'abcc')
print("re.findall('[a-z]', 'abcc')的值：", ret)  # ['a', 'b', 'c', 'c']

ret=re.findall('[1-9，a-z，A-Z]', '12abCD')
print("re.findall('[1-9，a-z，A-Z]', '12abCD')的值：", ret)  # ['1', '2', 'a', 'b', 'C', 'D']

#  []字符集:可以取消上面元字符的特殊功能
ret=re.findall('[b,*,,]', 'abeacea,dea*bcde')   # 可以取出后面字符串的，和*
print("re.findall('[b,*,,]', 'abeacea,dea*bcde')的值：", ret)  # ['b', ',', '*', 'b']

#  []内（- ^ \例外，取消不了功能）
#  [^]取反，不取值
ret=re.findall('[^b]', 'abc,')   # 除了b，其他都有
print("re.findall('[^b]', 'abc,')的值：", ret)  # ['a', 'c', ',']

ret=re.findall('[^a,b]', 'abc,')   # 除了a b 还有‘,’ 其他都有，注意这里','也没有了
print("re.findall('[^a,b]', 'abc,')的值：", ret)  # ['c']

# \
# \ 后面跟 元字符 去除 其特殊功能
# \ 后面跟 部分普通字符 可以实现 特殊功能
# '\A'    只从字符开头匹配，re.search("\Aabc","alexabc") 是匹配不到的
# '\Z'    匹配字符结尾，同$
# '\d'    匹配数字0-9
# '\D'    匹配非数字
# '\w'    匹配[A-Za-z0-9]
# '\W'    匹配非[A-Za-z0-9]
# '\s'     匹配空白字符、\t、\n、\r , re.search("\s+","ab\tc1\n3").group() 结果 '\t'
# \b 匹配一个特殊字符边界（比如空格 ， $ 等）
print(re.findall("\wasd", "abcasd"))  # ['casd']
print(re.findall("\w", "abcasd"))  # ['a', 'b', 'c', 'a', 's', 'd']

print(re.findall("I\s", "HI, I am a LIST"))  # ['I']
print(re.findall(r"I\b", "HI, I am a LIST"))  # ['I', 'I']

ret = re.search('sb', 'abcsb001')
print(ret)  # <_sre.SRE_Match object; span=(3, 5), match='sb'>
print(ret.group())  # sb

print(re.search('sb', 'abcsb001').group())  # 平时就这样使用，效果和上面的3行一样

m = re.findall('\bblow', ' blow')   # []   # \b在python里有特殊意义，传到re模块意义不一样
print(m)
m = re.findall(r'\bblow', 'blow111')  # ['blow']   # 前面加r，告诉re不要处理，直接传给python解释器？
print(m)

print(re.findall('c\\\c', 'abc\c'))   # ['c\\c']
print(re.findall('c\\\\c', 'abc\c'))  # ['c\\c']
print(re.findall(r'c\\c', 'abc\c'))   # ['c\\c']

# '(...)' 分组匹配，re.search("(abc){2}a(123|456)c", "abcabca456c").group() 结果 abcabca456
ret = re.search('(?P<id>\w{3}).(?P<name>\d{3})', 'web.123.com')   # ?P代表分组，<name>-分组的组名
print(ret.group())
print(ret.group('id'))
print(ret.group('name'))

# 正则表达式的方法
# 1. findall() : 所有的结果都返回到一个列表里
# 2. search（） ：返回匹配到的第一个对象（object），对象可以调用.group()返回结果
# 3. match（） ： 只在字符串开始的位置匹配，也返回一个对象，对象可以调用.group()返回结果
print(re.match('www', 'wwwabcwww001').group())  # www
# 4. split（）：分割
print('123456'.split('3'))   # ['12', '456'] 直接字符串分割的效果
print(re.split('abc', 'wwwabcwww001'))  # ['www', 'www001']
print(re.split('[a,0]', 'wwwabcwww001'))  # ['www', 'bcwww', '', '1']
# 先以a分割为 www bcwww001---》 然后以0去分割，前面没0跳过，后面继续分为 bcwww 01，--》01再分--》达到上面结果

# 5. sub（）替换
print(re.sub('a..x', 'abc', '123alex456'))

# 6. complie() 对象编译
re.compile()







