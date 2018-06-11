# creat with :PyCharm
# Author:Wilson
# Date:2018/5/18
# Time:12:33

# 与文本文件不同，图片、声音等文件都是二进制文件，
# 对二进制文件的读写基本是类似的，所不同的是传入open()的第二参数不同：

# 读取二进制文件使用 'rb' 模式
# 写入二进制文件使用 'wb' 模式

with open('test.jpg', 'rb') as f:
    image_data = f.read()

with open('test2.jpg', 'wb') as f:
    f.write(image_data)

# 上面的代码中，前两行读取test.jpg的内容，后两行将其写入test2.jpg。
# 代码执行完后，你可以在当前目录看到，新增了一张命名为test2.jpg，且与test.jpg完全一样的图片。
