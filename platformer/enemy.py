import pygame
from pygame.sprite import Sprite

class Enemy(Sprite):
    def __init__(self, x,y, enemy_group):
        super().__init__()
        self.image = pygame.image.load("assets/blob.png")
        self.rect = self.image.get_rect(topleft = (x,y))
        enemy_group.add(self)
        self.direction = 1
        self.counter = 0
        
    def update(self):
        self.rect.x += self.direction
        self.counter += 1
        if self.counter > 64:
            self.counter *= -1
            self.direction *= -1
            