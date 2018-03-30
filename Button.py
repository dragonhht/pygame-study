#!/usr/bin/env python 
# encoding: utf-8 

# @Author: dragonhht 
# @Date: 2018-03-30 17:06:43 
# @Last Modified by:   dragonhht 
# @Last Modified time: 2018-03-30 17:06:43 

import pygame
from pygame.locals import *

class Button(object):
    """
    按钮类.
    """
    def __init__(self, surface, text, rect):
        self.surface = surface
        self.bordercolor = (150, 130, 160)
        self.btncolor = (255, 255, 255)
        self.text = text
        self.rect = rect
        self.x = self.rect[0]
        self.y = self.rect[1]
        self.width = self.rect[2]
        self.height = self.rect[3]
        self.enable = True

    # 设置为不可点击
    def set_disable(self, status):
        self.enable = status

    # 创建按钮
    def create(self, btncolor=(255, 255, 255), bordercolor=(150, 130, 160), width=0):
        text_len = len(self.text)
        text_width = 4 * text_len
        pos = (self.rect[0] + (self.rect[2] - text_width) / 2, self.rect[1] + (self.rect[3] - 14) /2)
        lines = self.corner_pos()
        pygame.draw.rect(self.surface, btncolor, self.rect, width)
        if self.enable:
            pygame.draw.lines(self.surface, bordercolor, False, lines, 2)
        else:
            pygame.draw.lines(self.surface, (0, 0, 0), False, self.corner_pos(), 2)
        self.set_font(pos)

    # 绘制字体
    def set_font(self, pos, font='arial'):
        my_font = pygame.font.SysFont(font, 12)	
        text_surface = my_font.render(self.text, True, (0,0,0), (255, 255, 255))
        self.surface.blit(text_surface, pos)

    # 计算边框角坐标
    def corner_pos(self):
        lines = [(self.x, self.y), (self.x + self.width, self.y),
         (self.x + self.width, self.y + self.height), (self.x, self.y + self.height), (self.x, self.y)]
        return lines

    # 判断鼠标是否在按钮内
    def is_in_btn(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        return mouse_x >= self.x and mouse_x <= self.x + self.width and mouse_y >= self.y and mouse_y <= self.y + self.height

    # 鼠标在按钮上
    def mouse_over(self):
        if self.enable and self.is_in_btn():
            # 变色
            pygame.draw.lines(self.surface, (0, 0, 0), False, self.corner_pos(), 2)
            # TODO 准备可以传入函数执行

    # 判断是否点击按钮
    def mouse_click(self, event):
        if self.enable and self.is_in_btn():
            if event.type == MOUSEBUTTONUP:
                pass