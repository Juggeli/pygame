import pygame
from utils import *

class Helicopter(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('lolikopperi.png', -1)
        
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        #self.image = pygame.transform.flip(self.image, 1, 0)
        #self.area = pygame.Rect(0, 150, 400, 100)
        self.rect.topleft = 0, 25
            
    def moveRight(self):
        if self.rect.right > self.area.right:
            newpos = self.rect
        else:
            newpos = self.rect.move((5, 0))
            self.rect = newpos
        
    def moveLeft(self):
        if self.rect.left < self.area.left:
            newpos = self.rect
        else:
            newpos = self.rect.move((-5, 0))
            self.rect = newpos