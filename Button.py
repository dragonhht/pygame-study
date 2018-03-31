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
    surface: 按钮放置的面板 
    text:   按钮上显示的文字 
    pos:    按钮左上角的x, y坐标 
    wh:     按钮的宽高 
    """
    def __init__(self, surface, text, pos, wh, font_size=12):
        self.surface = surface
        self.bordercolor = (150, 130, 160)
        self.btncolor = (255, 255, 255)
        self.text = text
        self.rect = Rect(pos, wh)
        self.x = pos[0]
        self.y = pos[1]
        self.width = wh[0]
        self.height = wh[1]
        self.enable = True
        self.font_size = font_size
        self.default_font_size = 12
        self.default_width = self.default_font_size / 2.8 * len(self.text) + 6
        self.default_height = self.default_font_size + 6
        if self.width < self.default_width:
            self.width = self.default_width
        if self.height < self.default_height:
            self.height = self.default_height

    def set_enable(self, status):
        """设置为是否可用"""
        self.enable = status

    def set_font_size(self, font_size):
        """设置文本字体大小"""
        self.font_size = font_size

    def __set_font_center__(self, font_size):
        """字体居中"""
        text_len = len(self.text)
        # 一个字的大小为(mm): 字号/2.8
        text_width = font_size / 2.8 * text_len
        if text_width >= self.width or text_width >= self.height:
            text_width = self.default_font_size / 2.8 * text_len
            self.font_size = self.default_font_size
        pos = (self.x + (self.width - text_width) / 2, self.y + (self.height - font_size) /2)
        self.set_font(pos)

    def create(self, btncolor=(255, 255, 255), bordercolor=(150, 130, 160), width=0):
        """创建按钮"""
        lines = self.corner_pos()
        pygame.draw.rect(self.surface, btncolor, self.rect, width)
        pygame.draw.lines(self.surface, bordercolor, False, lines, 2)
        self.__set_font_center__(self.font_size)

    def set_font(self, pos, font='arial'):
        """绘制字体"""
        my_font = pygame.font.SysFont(font, self.font_size)	
        text_surface = my_font.render(self.text, True, (0,0,0), (255, 255, 255))
        self.surface.blit(text_surface, pos)

    def corner_pos(self):
        """计算边框角坐标"""
        lines = [(self.x, self.y), (self.x + self.width, self.y),
         (self.x + self.width, self.y + self.height), (self.x, self.y + self.height), (self.x, self.y)]
        return lines

    def is_in_btn(self):
        """判断鼠标是否在按钮内"""
        mouse_x, mouse_y = pygame.mouse.get_pos()
        return mouse_x >= self.x and mouse_x <= self.x + self.width and mouse_y >= self.y and mouse_y <= self.y + self.height

    
    def mouse_over(self, func = None, *args, **kwargs):
        """ 鼠标在按钮上 """
        if self.enable and self.is_in_btn():
            # 变色
            pygame.draw.lines(self.surface, (0, 0, 0), False, self.corner_pos(), 2)
            if func == None:
                pass
            else:
                func(*args, **kwargs)

    def mouse_click(self, event, func = None,*args, **kwargs):
        """判断是否点击按钮, 并传入将执行的函数"""
        if self.enable and self.is_in_btn():
            if event.type == MOUSEBUTTONUP:
                if func == None:
                    pass
                else:
                    func(*args, **kwargs)