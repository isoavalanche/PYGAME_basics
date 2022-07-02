# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 11:20:21 2022

@author: adsnk
"""

import pygame

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
displayscreen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Blitting Image!")

bird_topleft = pygame.image.load("angrybird.png") #載入圖案
bird_topleft_rect = bird_topleft.get_rect() #取得圖案的大小放在變數中
bird_topleft_rect.topleft = (0, 0) #設定圖案出現的位置

bird_topright = pygame.image.load("angrybird.png")
bird_topright_rect = bird_topright.get_rect() 
bird_topright_rect.topright = (800, 0)

unicorn_bottomleft = pygame.image.load("unicorn.png")
unicorn_bottomleft_rect = unicorn_bottomleft.get_rect()
unicorn_bottomleft_rect.bottomleft = (0, 600)

unicorn_bottomright = pygame.image.load("unicorn.png")
unicorn_bottomright_rect = unicorn_bottomright.get_rect()
unicorn_bottomright_rect.bottomright = (800, 600)

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)

#fonts = pygame.font.get_fonts() //取得所有PYGAME內建字型
system_font = pygame.font.SysFont("century", 64)
custom_font = pygame.font.Font("AbstractGroovy.ttf", 50) #載入外部下載字型

#Define Text:
show_text_1 = system_font.render("Angry Bird Game:", True, GREEN, DARKGREEN)
show_text_1_rect = show_text_1.get_rect() #產生字體的方框
show_text_1_rect.center = (400, 30)

show_text_2 = custom_font.render("Move Angry Bird soon!", True, GREEN)
show_text_2_rect = show_text_2.get_rect()
show_text_2_rect.center = (400, 400)

#音效
sound_1 = pygame.mixer.Sound("sound_1.wav")
sound_2 = pygame.mixer.Sound("sound_2.wav")

sound_1.play()
pygame.time.delay(2000) #2000毫秒=2秒
sound_2.play()
pygame.time.delay(2000)

sound_2.set_volume(0.6) #設音量0.1~1.0
sound_2.play()

#背景音樂
pygame.mixer.music.load("music.wav")
pygame.mixer.music.play(-1, 0.0) #-1重複播放，0.0從頭播放
pygame.time.delay(10000)
pygame.mixer.music.stop()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    pygame.draw.line(displayscreen, WHITE, (0, 75), (800, 75), 5)
            
    displayscreen.blit(bird_topleft, bird_topleft_rect)
    displayscreen.blit(bird_topright, bird_topright_rect)
    displayscreen.blit(unicorn_bottomleft, unicorn_bottomleft_rect)
    displayscreen.blit(unicorn_bottomright, unicorn_bottomright_rect)
    displayscreen.blit(show_text_1, show_text_1_rect)
    displayscreen.blit(show_text_2, show_text_2_rect)
    pygame.display.update()

pygame.quit()