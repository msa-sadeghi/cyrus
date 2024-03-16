from pygame.sprite import Sprite
from constants import *
class Player(Sprite):
    def __init__(self, x,y, enemy_group):
        super().__init__()
        self.enemy_group = enemy_group
        self.right_images = []
        self.left_images = []
        for i in range(1,5):
            img = pygame.image.load(f"assets/guy{i}.png")
            self.right_images.append(img)
            img_left = pygame.transform.flip(img, True, False)
            self.left_images.append(img_left)
        self.frame_index = 0
        self.image = self.right_images[self.frame_index]
        self.rect = self.image.get_rect(topleft = (x,y))
        self.alive = True
        self.idle = True
        self.vel_y = 0
        self.speed = 5
        self.direction = 1
        self.last_animated = pygame.time.get_ticks()   
        self.last_idle = pygame.time.get_ticks()  
        self.jumped = False 
        self.health = 3
        self.dead_image = pygame.image.load("assets/ghost.png")
    def update(self, tile_map):
        if self.alive:
            self.move(tile_map)
            self.animation() 
            self.check_alive()       
    def move(self, tile_map):
        dx = 0
        dy = 0        
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RIGHT]:
            self.direction = 1
            self.idle = False
            dx += self.speed
        if keys[pygame.K_LEFT]:
            self.direction = -1
            self.idle = False
            dx -= self.speed
        if not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT] and pygame.time.get_ticks() - self.last_idle > 500: 
            self.idle = True 
            self.last_idle =pygame.time.get_ticks()
        
        if keys[pygame.K_SPACE] and not self.jumped:
            self.vel_y = -15  
            self.jumped = True          
        dy += self.vel_y
        self.vel_y += 1      
        for tile in tile_map:
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.image.get_width(), self.image.get_height()):
                dx = 0
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.image.get_width(), self.image.get_height()):
                if self.vel_y > 0:
                    self.vel_y = 0
                    dy = tile[1].top - self.rect.bottom
                    self.jumped = False
                elif self.vel_y < 0:
                    self.vel_y = 0
                    dy = tile[1].bottom - self.rect.top
                    
        # if pygame.sprite.spritecollide(self, self.enemy_group, True)        :
        #     self.health -= 1
        for enemy in self.enemy_group.sprites():
            if enemy.rect.colliderect(self.rect):
                self.health -= 1
                enemy.kill()
            
        
        
        self.rect.x += dx
        self.rect.y += dy
        
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.vel_y = 0
            self.rect.bottom = SCREEN_HEIGHT
    
    def check_alive(self):
        print("********", self.health)
        if self.health <= 0:
            self.alive = False
            self.image = self.dead_image
        
    def animation(self):
        if pygame.time.get_ticks() - self.last_animated > 200:
            self.last_animated = pygame.time.get_ticks()
            self.frame_index += 1
            if self.frame_index >= len(self.right_images):
                self.frame_index = 0
        
        if not self.idle:
            if self.direction == 1:
                self.image = self.right_images[self.frame_index]
            if self.direction == -1:
                self.image = self.left_images[self.frame_index]
        else:
            self.frame_index = 0
            if self.direction == 1:
                self.image = self.right_images[self.frame_index]
            if self.direction == -1:
                self.image = self.left_images[self.frame_index]
            
            
        
        
        