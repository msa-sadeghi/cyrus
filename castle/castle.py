from pygame.sprite import Sprite
import pygame
import math
from bullet import Bullet
class Castle(Sprite):
    def __init__(self, x,y):
        super().__init__()
        image_100 = pygame.image.load("assets/castle/castle_100.png")
        self.image_100 = pygame.transform.scale(image_100, (image_100.get_width() * 0.2,\
             image_100.get_height() * 0.2))
        image_50 = pygame.image.load("assets/castle/castle_50.png")
        self.image_50 = pygame.transform.scale(image_50, (image_50.get_width() * 0.2,\
             image_50.get_height() * 0.2))
        image_25 = pygame.image.load("assets/castle/castle_25.png")
        self.image_25 = pygame.transform.scale(image_25, (image_25.get_width() * 0.2,\
             image_25.get_height() * 0.2))
        
        
        self.image = self.image_100
        self.rect = self.image.get_rect(topleft = (x,y))
        self.health = 1000
        self.max_health = 1000
        self.money = 0
        self.score = 0
        self.angle = 0
        self.last_shoot_time = 0
        self.ammo = 150
        
    def draw(self, screen)    :
        screen.blit(self.image, self.rect)
        
    def shoot(self, group):
         mouse_pos = pygame.mouse.get_pos() 
         if mouse_pos[1] > 80 and pygame.mouse.get_pressed()[0] and pygame.time.get_ticks() - self.last_shoot_time > 100 and self.ammo > 0:
              self.last_shoot_time = pygame.time.get_ticks()
              y_dist = -(mouse_pos[1] - self.rect.midleft[1])
              x_dist = mouse_pos[0] - self.rect.midleft[0]
              self.angle = math.atan2(y_dist, x_dist)
              Bullet(self.rect.midleft[0], self.rect.midleft[1], group, self.angle)
              self.ammo -= 1
              
    def repair(self):
          if self.health <= self.max_health and self.money >= 200:
               self.health += self.max_health//2
               if self.health > self.max_health:
                    self.health = self.max_health
               self.money -= 200
               
               
    def armour(self):
         if self.money >= 250:
              
               self.max_health += int(self.max_health * 0.2)
               self.money -= 250
          