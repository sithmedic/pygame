import pygame
import os
import time
import random

pygame.init()

#basic Colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
cyan = (0,255,255)
purple = (255,0,255)

gameDisplay = pygame.display.set_mode((800,600))

gameDisplay.fill(black)

pixAr = pygame.PixelArray(gameDisplay)

pixAr[10][20] = yellow

pygame.draw.line(gameDisplay, blue, (100,200), (300,450), 5)
pygame.draw.rect(gameDisplay, red, (400,400,50,25))
pygame.draw.circle(gameDisplay, green, (150,150), 75)
pygame.draw.polygon(gameDisplay, purple, ((25,75),(76,125),(250,375),(400,25),(60,540)))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q: #quit game
                gameExit = True
                pygame.quit()
                quit()

    pygame.display.update()
