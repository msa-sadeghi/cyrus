import pygame
class Button:
    def __init__(self, image, x,y) -> None:
        self.image = image
        self.rect = self.image.get_rect(center=(x,y))
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)