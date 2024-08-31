from pygame.sprite import Sprite
import pygame
import math
class Bullet(Sprite):
    def __init__(self, x,y, group, direction):
        super().__init__()
        img = pygame.image.load("assets/bullet.png")
        img_w = img.get_width()
        img_h = img.get_height()
        self.image = pygame.transform.scale(img, (img_w * 0.15, img_h * 0.15))
        self.rect = self.image.get_rect(center = (x,y))
        self.direction = direction
        self.speed = 5
        group.add(self)
        
    def update(self):
        self.rect.x += self.speed * math.cos(self.direction)
        self.rect.y += -(self.speed * math.sin(self.direction))