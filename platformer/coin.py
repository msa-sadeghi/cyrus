import pygame
from pygame.sprite import Sprite

class Coin(Sprite):
    def __init__(self, x,y, coin_group):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("assets/coin.png"), (32,32))
        self.rect = self.image.get_rect(topleft = (x,y))
        coin_group.add(self)
        self.direction = 1
        self.counter = 0
        
    def update(self):
        self.rect.y += self.direction
        self.counter += 1
        if self.counter > 64:
            self.counter *= -1
            self.direction *= -1
            