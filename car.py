import pygame
from utils import *

class Car(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('fedex_car.png', -1)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        #self.area = pygame.Rect(0, 150, 400, 100)
        self.rect.topleft = -self.rect.width, 425
        self.speed = 9
        self.shooted = 0
        
    def update(self):
        if not self.shooted:
            self._drive()
        else:
            self._explode()
            
    def _drive(self):
        newpos = self.rect.move((self.speed, 0))
        self.rect = newpos

    def _explode(self):
        pass

    def shooted(self):
        if not self.shooted:
            self.explode = 1
            self.original = self.image
