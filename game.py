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
    screen = pygame.display.set_mode(size)
    pygame.mouse.set_visible(0)

    background = pygame.image.load('E:/Koodi/Python/pygame/data/bg.png').convert()
    screen.blit(background, (0, 0))
    
    pygame.mixer.music.load('E:/Koodi/Python/pygame/data/music/08.mp3')
    boom = pygame.mixer.Sound('E:/Koodi/Python/pygame/data/music/explosion-02.wav')
    pygame.mixer.music.play(-1)
    
    clock = pygame.time.Clock()
    snowman = SnowMan()
    #cross = Cross()
    heli = Helicopter()
    #ball = Ball()
    #car = Car()
    uisprites = pygame.sprite.Group((heli))
    shootables = pygame.sprite.Group((snowman))
    #helisprite = pygame.sprite.Group((heli))
    CAREVENT = USEREVENT+1
    pygame.time.set_timer(CAREVENT, random.randint(600, 1000))

    while 1:
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
                uisprites.add(Ball(heli.rect.right-65))
                print "space"
            elif event.type == KEYUP and event.key == K_LEFT:
                moveLeft = 0
            elif event.type == KEYUP and event.key == K_RIGHT:
                moveRight = 0
            #elif event.type == MOUSEBUTTONDOWN:
                #for shootable in pygame.sprite.spritecollide(cross, shootables, 0):
                    #print "shoot"
                    #shootable.shooted()
                    #boom.play()

            #elif event.type is MOUSEBUTTONUP:
                #print "unshoot"
                #cross.unshoot()
                
            elif event.type is CAREVENT:
                pygame.time.set_timer(CAREVENT, random.randint(600, 1000))
                shootables.add(Car())
                
        if moveRight:
            heli.moveRight()
            #ball.moveRight()
        elif moveLeft:
            heli.moveLeft()
            #ball.moveLeft()
            
        for shootable in pygame.sprite.groupcollide(uisprites, shootables, 1, 1):
            print "shoot"
            shootable.shooted()
            boom.play()
        
        shootables.update()
        uisprites.update()
        #helisprite.update()
        screen.blit(background, (0, 0))
        
        shootables.draw(screen)
        uisprites.draw(screen)
        #helisprite.draw(screen)
        pygame.display.flip()

if __name__ == '__main__':
    main()
