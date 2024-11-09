from pygame.sprite import Sprite
import pygame
import math
from bullet import Bullet
class Tower(Sprite):
    def __init__(self, x,y, group):
        super().__init__()
        image_100 = pygame.image.load("assets/tower/tower_100.png")
        self.image_100 = pygame.transform.scale(image_100, (image_100.get_width() * 0.2,\
             image_100.get_height() * 0.2))
        image_50 = pygame.image.load("assets/tower/tower_50.png")
        self.image_50 = pygame.transform.scale(image_50, (image_50.get_width() * 0.2,\
             image_50.get_height() * 0.2))
        image_25 = pygame.image.load("assets/tower/tower_25.png")
        self.image_25 = pygame.transform.scale(image_25, (image_25.get_width() * 0.2,\
             image_25.get_height() * 0.2))
        
        
        self.image = self.image_100
        self.rect = self.image.get_rect(topleft = (x,y))
        self.health = 1000
        
        self.angle = 0
        self.last_shoot_time = 0
        self.alive = True
        group.add(self)
        
    def draw(self, screen)    :
        screen.blit(self.image, self.rect)
        
    def shoot(self, bullet_group, enemy_group):
         target = None
         for enemy in enemy_group:
              if enemy.alive:
                    if pygame.time.get_ticks() - self.last_shoot_time > 300 :
                         self.last_shoot_time = pygame.time.get_ticks()
                         y_dist = -(enemy.rect.y - self.rect.y)
                         x_dist = enemy.rect.x - self.rect.x
                         self.angle = math.atan2(y_dist, x_dist)
                         Bullet(self.rect.midleft[0], self.rect.midleft[1], bullet_group, self.angle)
                         
    def update(self,bullet_group, enemy_group)        :
          self.shoot(bullet_group, enemy_group)
   