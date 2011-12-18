#/usr/bin/env python

import os, pygame, random
from pygame.locals import *
from utils import *
from snowman import SnowMan
from cross import Cross
from car import Car
from helicopter import Helicopter
from ball import Ball

def main():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    
    size = width, height = 1152, 648
    moveRight = 0
    moveLeft = 0
    points = 10
    timer = 30
    running = 1
    screen = pygame.display.set_mode(size)

    background = pygame.image.load('E:/Koodi/Python/pygame/data/bg.png').convert()
    screen.blit(background, (0, 0))
    
    pygame.mixer.music.load('E:/Koodi/Python/pygame/data/music/08.mp3')
    boom = pygame.mixer.Sound('E:/Koodi/Python/pygame/data/music/explosion-02.wav')
    pygame.mixer.music.play(-1)
    
    clock = pygame.time.Clock()
    snowman = SnowMan()
    heli = Helicopter()
    uisprites = pygame.sprite.Group((heli))
    shootables = pygame.sprite.Group((snowman))
    CAREVENT = USEREVENT+1
    TIMEEVENT = USEREVENT+2
    
    pygame.time.set_timer(CAREVENT, random.randint(600, 1000))
    pygame.time.set_timer(TIMEEVENT, 1000)
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return
            elif event.type == KEYDOWN and event.key == K_RIGHT:
                print "right"
                moveRight = 1
            elif event.type == KEYDOWN and event.key == K_LEFT:
                print "left"
                moveLeft = 1
            elif event.type == KEYDOWN and event.key == K_SPACE:
                points = points-1
                uisprites.add(Ball(heli.rect.right-65))
                print "space"
            elif event.type == KEYUP and event.key == K_LEFT:
                moveLeft = 0
            elif event.type == KEYUP and event.key == K_RIGHT:
                moveRight = 0
                
            elif event.type is CAREVENT:
                pygame.time.set_timer(CAREVENT, random.randint(600, 1000))
                shootables.add(Car())
            elif event.type is TIMEEVENT:
                timer = timer - 1
                if timer == 0:
                    running = 0
                
        if moveRight:
            heli.moveRight()
        elif moveLeft:
            heli.moveLeft()
            
        for shootable in pygame.sprite.groupcollide(shootables, uisprites , 1, 1):
            print "shoot"
            shootable.shooted()
            print shootable.rnd
            if shootable.rnd == 5:
                points = points + 1
            elif shootable.rnd == 0:
                points = points - 10
            elif shootable.rnd == 2 or shootable.rnd == 3:
                points = points + 2
            else:
                points = points + 5
            boom.play()
            
        font = pygame.font.Font(None, 30)
        text = font.render('Points '+str(points), 1, (255,
        255, 255))
        timetext = font.render('Time: '+str(timer), 1, (255,
        255, 255))

        shootables.update()
        uisprites.update()
        screen.blit(background, (0, 0))
        screen.blit(text, (1000, 50))
        screen.blit(timetext, (1000, 80))
        
        shootables.draw(screen)
        uisprites.draw(screen)
        pygame.display.flip()
        
    raw_input('Press Enter...')

if __name__ == '__main__':
    main()
