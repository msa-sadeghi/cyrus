import pygame
class Button:
    def __init__(self,image, x,y):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)   
        self.clicked = False
        self.hovered = False
    def update(self, screen):
        self.hovered = self.rect.collidepoint(pygame.mouse.get_pos())
        if self.hovered:
            self.image.set_alpha(200)
        else:
            self.image.set_alpha(255)
        screen.blit(self.image, (self.rect.x, self.rect.y))
        if self.hovered and pygame.mouse.get_pressed()[0] and not self.clicked:
            self.clicked = True
        if not pygame.mouse.get_pressed()[0]:
            self.clicked = False
        return self.clicked, self.hovered