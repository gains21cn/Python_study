import re

# 给出一段如下行，比较复杂的运算公式，自己编写代码计算
# 1 - 2.99 * ( (60.2-30 +( -40/ 5) * (9-2*5/3 + 7 /3*99/4*2998 +10.5 * 568/14 )) - (-4*3)/ (16-3*2) )
# 思路：
# step1.需要先检查合法性，检测有无字母及其他的非运算的非法字符
# step2.格式化公式，去除空格，替换（--，+-，-+，++）之类的双运算符为（+，-，-，+）
# step3.先计算（）内的乘除，加减，然后再计算最后不含（）的乘除，加减


# 检查公式的合法性,有无非法字符
def check(s):
	if not s.count('(') == s.count(')'):
		print('请检查,括号未闭合')
	elif re.findall('[!@#$]', 's') is not None:
		print('请检查,该公式含有非法符号')
	elif re.findall('[a-zA-Z]', 's') is not None:
		print('请检查,该公式含有字母')
	elif s >= u'\u4e00' and s <= u'\u9fa5':
		print('请检查,该公式含有中文')


# 格式化公式，去除空格，重新定义双符号
def formats(s):
	s = s.replace(' ', '')
	s = s.replace('++', '+')
	s = s.replace('--', '+')
	s = s.replace('+-|-+', '-')
	s = s.replace('*+', '*')
	s = s.replace('/+', '/')
	return s

# 取数字和带小数点的方法，2种结果都一样，注意体会
# ret = re.findall(r'[\d\.]+', 'numbrt 1.58 abc 123')
# print(ret)  # ['1.58', '123']
#
# ret = re.findall('\d\.?\d*', 'numbrt 1.58 abc 123')
# print(ret)  # ['1.58', '123']


def cheng_chu(s):  # 处理带负号的乘除
	s = formats(s)
	r = re.compile(r'[\d\.]+[\*/]-?[\d\.]+')
	while re.search(r'[\*/]', s):
		ma = re.search(r, s).group()
		# print(ma)
		li = re.findall(r'(-?[\d\.]+|\*|/)', ma)
		if li[1] == '*':
			result = str(float(li[0]) * float(li[2]))
		else:
			result = str(float(li[0]) / float(li[2]))
		s = s.replace(ma, result, 1)
	return s


def jia_jian(s):  # 处理加减法，变成数组，全加
	s = formats(s)
	li = re.findall(r'([\d\.]+|\+|-)', s)
	nums = 0

	for i in range(len(li)):
		if li[i] == '-':
			li[i] = '+'
			li[i + 1] = float(li[i + 1]) * -1
	for i in li:
		if i == '+':
			i = 0
		nums = nums + float(i)
	return str(nums)


def simple(x):  # 处理不带括号的
	return jia_jian(cheng_chu(x))


def jiSuan(x):  # 处理带括号的

	while '(' in x:
		reg = re.compile(r'\([^\(\)]+\)')
		ma = re.search(reg, x).group()
		result = simple(ma[1:-1])
		x = x.replace(ma, result, 1)
	return simple(x)

ss = '1 - 2.99 * ( (60.2-30 +( -40/ 5) * (9-2*5/3 + 7 /3*99/4*2998 +10.5 * 568/14 )) - (-4*3)/ (16-3*2) )'.replace(' ', '')
print('你的计算结果：', jiSuan(ss))
print('eval计算结果：', eval(ss))

if jiSuan(ss) == eval(ss):
	print('计算正确，你很棒哟 @_@')
else:
	print('计算不正确，请重新来过！')

# 这里很奇怪，要是不str（），直接比较，就会显示‘计算不正确’，难道后面还有小数点吗？
if str(jiSuan(ss)) == str(eval(ss)):
	print('计算正确，你很棒哟 @_@')
else:
	print('计算不正确，请重新来过！')


