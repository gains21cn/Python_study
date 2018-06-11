import os
# os.getcwd()  #获取当前工作目录
# os.chdir(r"c:\user") #需要加个r
#
# os.makedirs('file1\\file2\\file3') #在当前工作目录下创建多层目录
# os.mkdir('file')  #只能生成单个目录
# os.mkdir('file')
# os.mkdir('file\\file1')  #如果已经有file目录,则可以在其下面建立file1,否则报错
#
# os.rmdir('dirname')  #删除单级空目录,如目录不为空,则无法删除,报错
# os.removedirs('file1\\file2\\file3') #删除空目录,有内容不删除
#
# os.listdir(r'c:\user')  #显示目录内所有的文件及文件夹,包括隐藏文件,以列表方式打开
# os.remove() #只能删除文件,不能删除文件夹
# os.rename("oldName","newName") #重新命名文件及文件夹
#
# os.stat('file') #获取文件或目录信息
# 	info=os.stat('.\\file')
# 	print(info)  #获取文件信息
# 	print(info.st_size) #获取文件大小
#
# os.sep  #获取操作系统的文件夹分隔符,win系统是 \, liunx是 /
#         #各种操作系统中,跨平台使用文件夹,很有用
# 		#feGe=os.sep
# 		#C:\user\david     c: %s user%s david  %feGe  这样各个平台都没有影响
#
# os.linesep #输出当前平台的换行操作符   win系统是 '\r\n' ,linux系统是'\n'
# os.pathsep #文件路径分隔符    win系统是 ; ,linux是 :
#
# os.name # 显示当前系统类型  win系统是 nt ,linux系统是 posix
# os.system('bash command')  #运行shell命令，直接显示
# os.path.abspath('./fileName') #从相对路径获取绝对路径





















