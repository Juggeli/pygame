import pygame
from utils import *

class Cross(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #call Sprite initializer
        self.image, self.rect = load_image('cross.png', -1)
        self.shooting = 0

    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.midtop = pos
        if self.shooting:
            self.rect.move_ip(5, 10)

    def shoot(self, target):
        if not self.shooting:
            print "cross shooting"
            #hitbox = self.rect.inflate(-5, -5)
            hitbox = self.rect.inflate(0, 0)
            print target.rect
            print hitbox
            self.shooting = 1
            return hitbox.colliderect(target.rect)

    def unshoot(self):
        self.shooting = 0