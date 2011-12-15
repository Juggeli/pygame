#/usr/bin/env python

import os, pygame
from pygame.locals import *
from utils import *
from snowman import SnowMan
from cross import Cross

def main():
    pygame.init()

    size = width, height = 1152, 648
    screen = pygame.display.set_mode(size)
    pygame.mouse.set_visible(0)

    background = pygame.image.load('data/bg.png').convert()
    screen.blit(background, (0, 0))
    
    clock = pygame.time.Clock()
    snowman = SnowMan()
    cross = Cross()
    allsprites = pygame.sprite.RenderPlain((snowman, cross))
    
    #pygame.display.update()

    while 1:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return
            elif event.type == MOUSEBUTTONDOWN:
                if cross.shoot(snowman):
                    snowman.shooted()
                #else:
            elif event.type is MOUSEBUTTONUP:
                cross.unshoot()

        allsprites.update()

        screen.blit(background, (0, 0))
        allsprites.draw(screen)
        pygame.display.flip()

if __name__ == '__main__':
    main()
