
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
        self.image_number = 0
        self.action = "walk"
        self.last_animation_update_time = 0
        enemy_group.add(self)
        self.touch = False
        self.last_damage_time = 0
        self.alive = True
        
    def update(self, bullet_group, castle, all_enemy_types, all_enemies_damage):
        if self.alive:
            if not self.touch:
                self.rect.x += self.speed
            self.check_alive()
            self.check_collisions(bullet_group, castle,all_enemy_types, all_enemies_damage)
        self.animation()
        
    def check_collisions(self, bullet_group, castle,all_enemy_types, all_enemies_damage):
        
        if self.rect.colliderect(castle.rect):
            self.touch = True
            if pygame.time.get_ticks() - self.last_damage_time > 1000:
                self.last_damage_time = pygame.time.get_ticks()
                i = all_enemy_types.index(self.type)
                castle.health -= all_enemies_damage[i]
                if castle.health < 0:
                    castle.health = 0
            
        if self.action == "death":
            castle.money += 10
        
        if pygame.sprite.spritecollide(self, bullet_group, True):
            self.health -= 25
            if self.health <= 0:
                self.health = 0
    def check_alive(self):
        if self.alive:
            if self.health <= 0:
                self.alive = False
                self.action = "death"
        
    def animation(self):
        self.image = self.images.get(self.action)[self.image_number]
        if pygame.time.get_ticks() - self.last_animation_update_time > 100:
            self.last_animation_update_time = pygame.time.get_ticks()
            self.image_number += 1
            if self.image_number >= len(self.images[self.action]):
                if self.action != "death":
                    self.image_number = 0
                else:
                    self.image_number = len(self.images[self.action]) - 1
        
            
            
        
        
        