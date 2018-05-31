import pygame
import os
import time
import random

pygame.init()
display_width = 800
display_height = 600

#initiate colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
cyan = (0,255,255)
purple = (255,0,255)

smalltext = pygame.font.Font('freesansbold.ttf',20)
largeText = pygame.font.Font('freesansbold.ttf',115)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

carFile = 'C:\Test\PyGameTutorial\PyGameTutorial\images\car1.png'
obsFile = 'C:\Test\PyGameTutorial\PyGameTutorial\images\obs1.xcf'
carImg = pygame.image.load(carFile)
car_width = 39

def game_quit():
    pygame.quit()
    quit()

def button(msg,x,y,w,h,inactiveColor,activeColor,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, activeColor, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
            if action == "play":
                game_loop()
            elif action == "quit":
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(gameDisplay, inactiveColor, (x, y, w, h))
    
    textSurf_button, textRect_button = text_objects(msg, smalltext)
    textRect_button.center = ((x + (w/2)), (y + (h/2)))
    gameDisplay.blit(textSurf_button, textRect_button)

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, red)
    gameDisplay.blit(text, (0,0))

def car(x,y):
    gameDisplay.blit(carImg, (x,y))

def things(thingx, thingy, thingw, thingh, thingcolor):
    pygame.draw.rect(gameDisplay, thingcolor, [thingx, thingy,thingw, thingh])

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()

def crash():
    message_display('You Crashed')

def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q: #quit game
                    pygame.quit()
                    quit()

        gameDisplay.fill(white)
        introtext = "A Bit Racy"
        TextSurf, TextRect = text_objects(introtext, largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        #Go button :: button(msg,x,y,w,h,inactiveColor,activeColor,action)
        hoverGreen = (0, 150, 0)
        button("GO!",150,450,100,50,green,hoverGreen,game_loop)
        #Quit Button :: button(msg,x,y,w,h,inactiveColor,activeColor,action)
        hoverRed = (150, 0, 0)
        button("NOPE!",550,450,100,50,red,hoverRed,game_quit)
        
        pygame.display.update()
        clock.tick(15)

#GAME LOOP
def game_loop():

    #game loop params
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0
    y_change = 0

    #obsticles 
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 5
    thing_width = 100
    thing_height = 100
    
    track_key_a = 0
    track_key_d = 0

    thing_color_r = 0
    thing_color_g = 255
    thing_color_b = 0
    
    thing_count = 1

    #achievements
    dodged = 0

    gameExit = False

    #game loop logic
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q: #quit game
                    gameExit = True
                    pygame.quit()
                    quit()
                if event.key == pygame.K_a:
                    track_key_a = 1
                    x_change = -5
                elif event.key == pygame.K_d:
                    track_key_d = 1
                    x_change = 5
                #elif event.key == pygame
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    x_change = 0
                
        x += x_change
        y += y_change
        
        #draw the game
        gameDisplay.fill(white) #draw background
        thing_color_now = (thing_color_r, thing_color_g, thing_color_b) #define color of obsticle
        things(thing_startx, thing_starty, thing_width, thing_height, thing_color_now) #draw an obsticle
        thing_starty += thing_speed #move the obsticle down across the screen
        car(x,y) #draw car
        things_dodged(dodged) #draw the score (dodged)

        if x > display_width - car_width or x < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            dodged += 1
            thing_speed += 1
            thing_width += (dodged * 1.2)
            thing_height += (dodged * 1.2)
            if thing_color_r < 245:
                thing_color_r += 10
            if thing_color_g > 10:
                thing_color_g -= 10

        if (y > thing_starty and y < thing_starty + thing_width) or (y + car_width > thing_starty and y + car_width < thing_starty + thing_width):
            print(thing_starty+thing_height)
            if (x > thing_startx and x < thing_startx + thing_width) or (x + car_width > thing_startx and x + car_width < thing_startx + thing_width):
                print('x crossOver')
                crash()
        
        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()