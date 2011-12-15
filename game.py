#/usr/bin/env python

import os, pygame
from pygame.locals import *
from utils import *
from snowman import SnowMan

def main():
    pygame.init()

    size = width, height = 1152, 648

    screen = pygame.display.set_mode(size)

    background = pygame.image.load('data/bg.png').convert()
    screen.blit(background, (0, 0))
    
    clock = pygame.time.Clock()
    snowman = SnowMan()
    allsprites = pygame.sprite.RenderPlain((snowman))
    
    #pygame.display.update()

    while 1:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return
            # elif event.type == MOUSEBUTTONDOWN:
            #     if fist.punch(chimp):
            #         punch_sound.play() #punch
            #         chimp.punched()
            #     else:
            #         whiff_sound.play() #miss
            # elif event.type is MOUSEBUTTONUP:
            #     fist.unpunch()

        allsprites.update()

        screen.blit(background, (0, 0))
        allsprites.draw(screen)
        pygame.display.flip()

if __name__ == '__main__':
    main()
