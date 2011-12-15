#/usr/bin/env python

import os, pygame, random
from pygame.locals import *
from utils import *
from snowman import SnowMan
from cross import Cross
from car import Car

def main():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    
    size = width, height = 1152, 648
    screen = pygame.display.set_mode(size)
    pygame.mouse.set_visible(0)

    background = pygame.image.load('data/bg.png').convert()
    screen.blit(background, (0, 0))
    
    pygame.mixer.music.load('data/music/08.mp3')
    pygame.mixer.music.play(-1)
    
    clock = pygame.time.Clock()
    snowman = SnowMan()
    cross = Cross()
    #car = Car()
    uisprites = pygame.sprite.Group((cross))
    shootables = pygame.sprite.Group((snowman))
    CAREVENT = USEREVENT+1
    pygame.time.set_timer(CAREVENT, random.randint(600, 1000))
    pygame.mixer.music.load('data/music/08.mp3')
    pygame.mixer.music.play(-1)

    while 1:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return
            elif event.type == MOUSEBUTTONDOWN:
                for shootable in shootables:
                    if cross.shoot(shootable):
                        shootable.shooted()
                #else:
            elif event.type is MOUSEBUTTONUP:
                cross.unshoot()
            elif event.type is CAREVENT:
                pygame.time.set_timer(CAREVENT, random.randint(600, 1000))
                shootables.add(Car())
                
        uisprites.update()
        shootables.update()

        screen.blit(background, (0, 0))
        uisprites.draw(screen)
        shootables.draw(screen)
        pygame.display.flip()

if __name__ == '__main__':
    main()
