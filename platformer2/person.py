import pygame
from pygame.sprite import Sprite
import os
from bullet import Bullet
from grenade import Grenade
class Person(Sprite):
    def __init__(self, type, x,y, ammo, grenades, health):
        super().__init__()
        self.type = type
        self.animation_types = ('Idle', 'Run', 'Jump', 'Death')
        self.images = {}
        for anim_type in self.animation_types:
            temp = []
            images_count = len(os.listdir(f'assets/images/{type}/{anim_type}'))
            for i in range(images_count):
                img = pygame.image.load(f'assets/images/{type}/{anim_type}/{i}.png')
                img_w = img.get_width()
                img_h = img.get_height()
                img = pygame.transform.scale(img, (img_w * 2, img_h * 2))
                temp.append(img)
            self.images[anim_type] = temp
        self.image_number = 0
        self.action = "Idle"
        self.image = self.images['Idle'][0]
        self.rect = self.image.get_rect(topleft=(x,y))
        self.ammo = ammo
        self.grenades = grenades
        self.health = health
        self.max_health = health
        self.alive = True
        self.idling = True
        self.direction = 1
        self.flip = False
        self.last_animation_update_time = 0
        self.y_velocity = 0
        self.in_air = False
        self.last_shoot_time = 0
        
    def draw(self, screen):
        self.animation()
        img = pygame.transform.flip(self.image, self.flip, False)
        screen.blit(img, self.rect)
    def gravity(self):
        
        dy = 0   
        self.y_velocity += 1
        dy += self.y_velocity
        if self.y_velocity >= 10:
            self.y_velocity = 10
            
        if self.rect.bottom + dy > 300:
            self.y_velocity = 0
            dy = 300 - self.rect.bottom 
            self.in_air = False
        self.rect.y += dy
        
        
    def move(self, moving_left, moving_right):
        dx = 0
        
        
        if moving_left:
            dx -= 5
            self.direction = -1
            self.flip = True
        if moving_right:
            dx += 5
            self.direction = 1
            self.flip = False
        
        self.rect.x += dx
        
    def animation(self):
        self.image = self.images[self.action][self.image_number]
        if pygame.time.get_ticks() - self.last_animation_update_time > 100:
            self.last_animation_update_time = pygame.time.get_ticks()
            self.image_number += 1
            if self.image_number >= len(self.images[self.action]):
                self.image_number = 0
        

    def change_action(self, new_action):
        if self.action != new_action:
            self.action = new_action
            self.image_number = 0
            
            
    def shoot(self,weapon, weapon_group):
        if weapon == "bullet":
            if self.ammo > 0 and pygame.time.get_ticks() - self.last_shoot_time > 100:
                self.last_shoot_time = pygame.time.get_ticks()
                self.ammo -= 1
                Bullet(self.type, self.rect.centerx + \
                    self.direction * self.rect.size[0], self.rect.centery, \
                        weapon_group, self.direction)
        elif weapon == "grenade":
            if self.grenades > 0 and pygame.time.get_ticks() - self.last_shoot_time > 100:
                self.last_shoot_time = pygame.time.get_ticks()
                self.grenades -= 1
                Grenade(self.rect.centerx + \
                    self.direction * self.rect.size[0], self.rect.centery - self.rect.size[1], \
                        weapon_group,self.direction)