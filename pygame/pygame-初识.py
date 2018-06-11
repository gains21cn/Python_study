#creat with :PyCharm
#Author:Wilson
#Date:2018/5/17
#Time:14:27

# 2018年5月17日 14:38:12 星期四 pip install pygame 成功

# 获取python版本号，以便安装对应的包
# import pip
# print(pip.pep425tags.get_supported())

# 生成一个窗口，写一段文字

import pygame
import sys
from pygame.locals import *

white = 255,255,255
blue = 0,0,200

pygame.init()
screen = pygame.display.set_mode((600,500))

myfont = pygame.font.Font(None,60)
textImage = myfont.render("Hello Pygame", True, white)

while True:
     for event in pygame.event.get():
         if event.type in (QUIT, KEYDOWN):
             sys.exit()

     screen.fill(blue)
     screen.blit(textImage, (100,100))
     pygame.display.update()


