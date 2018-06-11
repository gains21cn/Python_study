#creat with :PyCharm
#Author:Wilson
#Date:2018/5/16
#Time:13:11

import hashlib

m= hashlib.md5()
print(m)    #<md5 HASH object @ 0x00000000020F0378>

m.update('hello world'.encode('utf-8')) #.encode注意.

#hex 16进制数
print(m.hexdigest())   #5eb63bbbe01eeed093cb22bb8f5acdc3

m.update('wilson'.encode('utf-8'))
print("m的新值",m)
print("m的新值加密16进制数字",m.hexdigest())

print("admin的md5加密：",hashlib.md5('admin'.encode('utf8')).hexdigest())
print("admin的sha1加密：",hashlib.sha1('admin'.encode('utf8')).hexdigest())
print("admin的sha3-256加密：",hashlib.sha3_256('admin'.encode('utf8')).hexdigest())
print("admin的sha3-512加密：",hashlib.sha3_512('admin'.encode('utf8')).hexdigest())

# ######## md5 ########
hash = hashlib.md5()
hash.update('admin'.encode('utf-8'))
print(hash.hexdigest())

# ######## sha1 ########
hash = hashlib.sha1()
hash.update('admin'.encode('utf-8'))
print(hash.hexdigest())

# ######## sha256 ########
hash = hashlib.sha256()
hash.update('admin'.encode('utf-8'))
print(hash.hexdigest())

# ######## sha512 ########
hash = hashlib.sha512()
hash.update('admin'.encode('utf-8'))
print(hash.hexdigest())

# 以上加密算法虽然依然非常厉害，但时候存在缺陷，即：通过撞库可以反解。所以，有必要对加密算法中添加自定义key再来做加密。

import hashlib
# ######## md5 ########
hash = hashlib.md5('898oaFs09f'.encode('utf-8'))
hash.update('admin'.encode('utf-8'))
print("加密算法中添加自定义key:",hash.hexdigest())


# 还不够吊？python还有一个hmac模块，它内部对我们创建key和内容再进行处理然后再加密
import hmac

h = hmac.new('wueiqi'.encode('utf-8'))
h.update('hellowo'.encode('utf-8'))
print("hmac模块，它内部对我们创建key和内容再进行处理,然后再加密",h.hexdigest())

