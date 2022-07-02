# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 09:48:09 2022

@author: adsnk
"""

import pygame #載入

pygame.init() #啟動

WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
displayscreen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) #產生畫布
pygame.display.set_caption("My first pygame!")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MEG = (255, 0, 255)
GREY = (192, 192, 192)

displayscreen.fill(GREY) #填滿畫布背景

#pygame.draw.line(畫布名稱, color, start, end, thickness)
pygame.draw.line(displayscreen, CYAN, (0, 300), (800, 300), 3)
pygame.draw.line(displayscreen, CYAN, (400, 0), (400, 600), 3)
pygame.draw.line(displayscreen, CYAN, (0, 0), (800, 600), 3)
pygame.draw.line(displayscreen, CYAN, (800, 0), (0, 600), 3)

#pygame.draw.circle(畫布名稱, color, center, radius, thickness) thickness=0(填滿)
RAD = 100
for i in range(10):
    pygame.draw.circle(displayscreen, MEG, (400, 300), RAD, 3)
    RAD += 10
    
#pygame.draw.rect(畫布名稱, 顏色, (topleft-x, topleft-y, width, height), thickness) thickness=0(填滿)
pygame.draw.rect(displayscreen, BLUE, (0, 0, 800, 100), 3)


running = True
while running:
    for event in pygame.event.get(): #抓取畫布上所有的事件
        if event.type == pygame.QUIT: #事件的type==QUIT(按下結束鍵)
            running = False
            
    pygame.display.update() #畫布更新

pygame.quit() #結束