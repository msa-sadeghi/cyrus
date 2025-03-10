from pygame.sprite import Sprite
import pygame

from explosion import Explosion
class Grenade(Sprite):
    def __init__(self, x,y, group, direction):
        super().__init__()
        self.image = pygame.image.load("./assets/images/icons/grenade.png")
        self.rect = self.image.get_rect(topleft=(x,y))
        self.gravity = -15
        self.speed = 4
        self.timer = 100
        self.direction = direction
        group.add(self)
        
    def update(self, group):
        dx = self.direction * self.speed
        dy = self.gravity
        self.gravity += 1
        
        if self.rect.bottom + dy > 300:
            dy = 300 - self.rect.bottom
            self.gravity = 0
            self.speed= 0
            
        self.timer -= 1
        if self.timer <= 0:
            self.kill()
            Explosion(
                self.rect.centerx,
                self.rect.centery,
                group
                
            )
        self.rect.x += dx 
        self.rect.y += dy