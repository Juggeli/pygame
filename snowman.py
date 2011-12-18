import pygame
from utils import *

class SnowMan(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('snowman.png', -1)
        screen = pygame.display.get_surface()
        #self.area = screen.get_rect()
        self.area = pygame.Rect(400, 150, 400, 100)
        self.rect.topleft = 400, 150
        self.speed = 1
        self.dizzy = 0
        self.stopped = 0
        self.count = 0
        self.rnd = 4
        
    def update(self):
        self.count += 1
        if self.count > 120:
            if self.stopped == 1:
                self.stopped = 0
            else:
                self.stopped = 1
            self.count = 0
        if not self.stopped:
            self._walk()
        if self.dizzy:
            self._spin()
            
    def _walk(self):
        newpos = self.rect.move((self.speed, 0))
        if not self.area.contains(newpos):
            if self.rect.left < self.area.left or self.rect.right > self.area.right:
                self.speed = -self.speed
                newpos = self.rect.move((self.speed, 0))
                self.image = pygame.transform.flip(self.image, 1, 0)
        self.rect = newpos

    def _spin(self):
        center = self.rect.center
        self.dizzy += 12
        if self.dizzy >= 360:
            self.dizzy = 0
            self.image = self.original
        else:
            rotate = pygame.transform.rotate
            self.image = rotate(self.original, self.dizzy)
        self.rect = self.image.get_rect(center=center)

    def shooted(self):
        if not self.dizzy:
            self.dizzy = 1
            self.original = self.image
    