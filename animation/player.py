import pygame
class Player:
    def __init__(self, x,y):
        self.idle_images = []
        self.run_images = []
        for i in range(1,10):
            img = pygame.image.load(f"./images/Idle{i}.png")
            img = pygame.transform.scale(img, (
                img.get_width() * 0.2, img.get_height() * 0.2
            ))
            self.idle_images.append(img)
        for i in range(1,9):
            img = pygame.image.load(f"./images/Run{i}.png")
            img = pygame.transform.scale(img, (
                img.get_width() * 0.2, img.get_height() * 0.2
            ))
            self.run_images.append(img)
            
        self.image = self.idle_images[0]
        self.frame_index = 0
        self.rect = self.image.get_rect(topleft=(x,y))
        self.last_animation_time = pygame.time.get_ticks()
        
    def draw(self, screen):
        self.animation()
        img =  self.idle_images[self.frame_index]
        screen.blit(img, self.rect)
        
    def animation(self):
        if pygame.time.get_ticks() - self.last_animation_time >= 100:
            self.last_animation_time = pygame.time.get_ticks()
            self.frame_index += 1
            if self.frame_index >= len(self.idle_images):
                self.frame_index = 0
    
    def move(self):
        # TODO
        pass