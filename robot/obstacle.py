from pygame.sprite import Sprite
import pygame

class Obstacle(Sprite):
    def __init__(self, type, x,y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=(x,y))
        self.type = type


    def draw(self, screen):
        screen.blit(self.image, self.rect)