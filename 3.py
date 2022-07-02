# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 14:31:49 2022

@author: adsnk
"""

import pygame
import random

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
displayscreen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Movement and Collisions!")

#set FPS(Frequency Per Second) and clock(抓CPU的時序)
FPS = 60
clock = pygame.time.Clock()

#Set game values
VELOCITY = 5 #速率
CYAN = (0, 255, 255)

unicorn = pygame.image.load("unicorn.png")
unicorn_rect = unicorn.get_rect()
unicorn_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

coin = pygame.image.load("coin.png")
coin_rect = coin.get_rect()
coin_rect.center = (100, 100)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed() #偵測目前有哪個按鍵被按下
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and unicorn_rect.left > 0:
        unicorn_rect.x -= VELOCITY
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and unicorn_rect.right < WINDOW_WIDTH:
        unicorn_rect.x += VELOCITY
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and unicorn_rect.top > 0:
        unicorn_rect.y -= VELOCITY
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and unicorn_rect.bottom < WINDOW_HEIGHT:
        unicorn_rect.y += VELOCITY
        
    if unicorn_rect.colliderect(coin_rect):
        print("HIT")
        coin_rect.x = random.randint(0, WINDOW_WIDTH-50)
        coin_rect.y = random.randint(0, WINDOW_HEIGHT-50)
        
    displayscreen.fill(CYAN)
    
    displayscreen.blit(unicorn, unicorn_rect)
    displayscreen.blit(coin, coin_rect)
    pygame.display.update()
    clock.tick(FPS)
            
pygame.quit()