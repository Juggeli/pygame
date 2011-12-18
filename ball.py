import pygame, random
from utils import *

class Ball(pygame.sprite.Sprite):
    def __init__(self, left):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('ball.png', -1)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        #self.area = pygame.Rect(0, 150, 400, 100)
        self.rect.topleft = left, 95
        self.dropping = 1
        self.speed = 0
        
    def drop(self):
        if not self.dropping:
            self.dropping = 1
        
    def moveRight(self):
        if self.rect.right > self.area.right:
            newpos = self.rect
        newpos = self.rect.move((5, 0))
        self.rect = newpos
        
    def moveLeft(self):
        if self.rect.left > self.area.left:
            newpos = self.rect
        newpos = self.rect.move((-5, 0))
        self.rect = newpos
        
    def update(self):
        if self.dropping:
            self.speed += 1
            newpos = self.rect.move((0, self.speed))
            self.rect = newpos
            if self.rect.top > self.area.bottom:
                self.kill()
    def shooted(self):
        if self.dropping:
            self.kill()
        