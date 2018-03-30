#!/usr/bin/env python 
# encoding: utf-8 
 
# @Author: dragonhht 
# @Date: 2018-03-29 22:17:45 
# @Last Modified by:   dragonhht 
# @Last Modified time: 2018-03-29 22:17:45 

import pygame
from pygame.locals import *
from sys import exit
from Button import *

pygame.init()

# 创建窗体
screen = pygame.display.set_mode((300, 300), 0, 32)
pygame.display.set_caption('hello')

btn = Button(screen, 'submit', Rect((10, 20), (40, 20)))

while True:
    event = pygame.event.wait()
    # 退出
    if event.type == QUIT:
        print('退出...')
        exit()

    if event.type == KEYDOWN:
        print('按下键盘: %s' % event.key) 

    screen.fill((255, 255, 255))
    btn.create()
    btn.mouse_over()
    btn.mouse_click(event)
    pygame.display.update()

