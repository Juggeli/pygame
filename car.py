import pygame, random
from utils import *

class Car(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        rnd = random.randint(0,3)
        if rnd == 0: 
            self.image, self.rect = load_image('fedex_car.png', -1)
        elif rnd == 1:
            self.image, self.rect = load_image('car.png', -1)
        elif rnd == 2: 
            self.image, self.rect = load_image('car_trailer.png', -1)
        elif rnd == 3: 
            self.image, self.rect = load_image('car_trailer_green.png', -1)
        
        
        
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        #self.image = pygame.transform.flip(self.image, 1, 0)
        #self.area = pygame.Rect(0, 150, 400, 100)
        self.rect.topleft = -self.rect.width, 425
        self.speed = 9
        self.driving = 1
        
    def update(self):
        if self.driving:
            self._drive()
        else:
            self._explode()
            
    def _drive(self):
        newpos = self.rect.move((self.speed, 0))
        self.rect = newpos
        if self.rect.left > self.area.right:
            self.kill()

    def _explode(self):
        pass

    def shooted(self):
        if self.driving:
            self.explode = 1
            self.original = self.image
            self.kill()
