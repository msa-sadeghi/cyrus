from pygame.sprite import Sprite
import pygame

class Bullet(Sprite):
    def __init__(self, owner, x,y, group, direction):
        super().__init__()
        self.owner = owner
        self.image = pygame.image.load("./assets/img/icons/bullet.png")
        self.rect = self.image.get_rect(topleft=(x,y))
        self.direction = direction
        group.add(self)
        
    def update(self):
        self.rect.x +=                                
        if self.rect.x <= 0 or self.rect.x >= 800:
            self.kill()