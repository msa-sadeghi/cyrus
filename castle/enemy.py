
import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self,type, health,speed, enemy_group, x,y):
        super().__init__()
        self.type = type
        self.health = health
        self.speed = speed
        self.images = {}
        self.animations = ("walk", "attack", "death")
        for anime in self.animations:
            temp_list = []
            for i in range(20):
                img = pygame.image.load(f"assets/enemies/{type}/{anime}/{i}.png")
                w = img.get_width()
                h = img.get_height()
                img = pygame.transform.scale(img, (w * 0.3, h * 0.3))
                temp_list.append(img)
            self.images.update({anime: temp_list})
            
        self.image = self.images.get(self.animations[0])[0]
        self.rect = self.image.get_rect(topleft= (x,y))
        enemy_group.add(self)
            
            
        
        
        