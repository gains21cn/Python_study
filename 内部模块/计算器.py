import re

source = '515411+566'

# 检查公式的合法性,有无非法字符
def check(s):
	flag = True
	if not s.count('(') == s.count(')'):
		print('请检查,括号未闭合')
		flag = False
	elif re.findall('[!@#$&]','s'):
		print('请检查,该公式含有非法符号')
		flag = False
	elif re.findall('[a-zA-Z]', 's'):
		print('请检查,该公式含有字母')
		flag = False
	elif s >= u'\u4e00' and s <= u'\u9fa5':
		print('请检查,该公式含有中文')
		flag = False
	return s
	
# 格式化公式
def formats(s):
	s = s.replace(' ','')
	s = s.replace('++','+')
	s = s.replace('--','+')
	s = s.replace('+-|-+','-')
	s = s.replace('*+','*')
	s = s.replace('/+','/')
	return s

# 定义乘除   # (2+5.2*3)
def cal_cheng_chu(s)
	ret1 = re.search('\d+\.?\d* [*/] \d+\.?\d*', 's').group()  # \d+\.?\d*代表一个带小数点的数
	# 5.2*3
	x,y = re.split('[*/]',ret1) # 分割,2个变量去接受 '5.2' '3'
	# 2个值是字符型,需要转换为float型
	
	ret2 = float(x) * float(y)
	ret2 = str(ret2) # 把float转换为str型
	s.replace(ret1,ret2) # 把计算后的结果,替代本来的乘除公式
	return s
	
# 定义加减 
def cal_jia_jian(s)

# 开始计算
if check(source):
	print('你要计算的是:',source)
	print('eval的标准结果是:',eval(source)
	source = formats(source)
	print(source)
	
	
	while re.search('\(,'source'):    # 检测有()
		source = re.search('\([^()]+\)','source').group()
		source = cal_cheng_chu(source)   # (2+15)
		source = cal_jia_jian(source)    # (17)  切片[1,-1],取出()内的数字
		
	else:     # 没有()后继续执行
		source = cal_cheng_chu(source)   # (2+15)
		source = cal_jia_jian(source) 