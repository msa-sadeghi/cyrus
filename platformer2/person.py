import pygame
from pygame.sprite import Sprite
import os
class Person(Sprite):
    def __init__(self, type, x,y, ammo, grenades, health):
        super().__init__()
        self.animation_types = ('Idle', 'Run', 'Jump', 'Death')
        self.images = {}
        for anim_type in self.animation_types:
            temp = []
            images_count = len(os.listdir(f'assets/img/{type}/{anim_type}'))
            for i in range(images_count):
                img = pygame.image.load(f'assets/img/{type}/{anim_type}/{i}.png')
                img_w = img.get_width()
                img_h = img.get_height()
                img = pygame.transform.scale(img, (img_w * 2, img_h * 2))
                temp.append(img)
            self.images[anim_type] = temp
        self.image_number = 0
        self.image = self.images['Idle'][0]
        self.rect = self.image.get_rect(topleft=(x,y))
        self.ammo = ammo
        self.grenades = grenades
        self.health = health
        self.max_health = health
        self.alive = True
        self.idling = True
        self.direction = 1
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
    def move(self):
        pass
                
            

            