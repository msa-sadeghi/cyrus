from pygame.sprite import Sprite
import pygame
import os
class Player(Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.animation_types = os.listdir("./png")
        self.all_images = {}

        for animation in self.animation_types:
            temp = []
            num_of_images = len(os.listdir(f"./png/{animation}"))
            for i in range(1, num_of_images):
                img = pygame.image.load(f"./png/{animation}/{animation}{i}.png")
                img = pygame.transform.scale_by(img, 0.4)
                temp.append(img)

            self.all_images[animation] = temp

        self.frame_index = 0
        self.action = "Idle"
        self.image = self.all_images[self.action][self.frame_index]
        self.rect = self.image.get_rect(topleft=(x,y))
        self.last_index_change_time = pygame.time.get_ticks()
        self.direction = 1
        self.idle = True
        self.flip = False
        self.x_speed = 5

    def draw(self, screen):
        image = self.all_images[self.action][self.frame_index]
        image = pygame.transform.flip(image, self.flip, False)
        screen.blit(image, self.rect)
        self.animation()

    def animation(self):
        if pygame.time.get_ticks() - self.last_index_change_time >=100:
            self.frame_index += 1
            if self.frame_index >= len(self.all_images[self.action]):
                self.frame_index = 0
            self.last_index_change_time = pygame.time.get_ticks()

    def move(self):
        dx = 0
        dy = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.direction = -1
            self.flip = True
            self.idle = False
            dx -= self.x_speed
        if keys[pygame.K_RIGHT]:
            self.direction = 1
            self.flip = False
            self.idle = False
            dx += self.x_speed
        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.idle = True

        self.rect.x += dx
        self.rect.y += dy



        



