# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Liu Zhao

import re

# ret1 = re.search('\d+\.?\d* [*/] \d+\.?\d*', 's').group()  # \d+\.?\d*代表一个带小数点的数
def chengchu(s):  # 处理带负号的乘除，负号歪打正着处理成功了
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


def jiajian(s):  # 处理加减法，变成数组，全加
	li = re.findall(r'([\d\.]+|\+|-)', s)
	sum = 0
	for i in range(len(li) - 1):  # 处理有两个--号连续的情况
		if li[i] == '-' and li[i + 1] == '-':
			li[i] = '+'
			li[i + 1] = '+'
	for i in range(len(li)):
		if li[i] == '-':
			li[i] = '+'
			li[i + 1] = float(li[i + 1]) * -1
	for i in li:
		if i == '+':
			i = 0
		sum = sum + float(i)
	return str(sum)


def simple(s):  # 处理不带括号的
	return jiajian(chengchu(s))


def complex(s):  # 处理带括号的
	while '(' in s:
		reg = re.compile(r'\([^\(\)]+\)')
		ma = re.search(reg, s).group()
		result = simple(ma[1:-1])
		s = s.replace(ma, result, 1)
	return simple(s)


ss = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'.replace(' ', '')
print(complex(ss))
print(eval(ss))


