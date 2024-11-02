import pygame
class Button:
    def __init__(self, image, x,y) -> None:
        self.image = image
        self.rect = self.image.get_rect(center=(x,y))
        
    def draw(self, screen) -> None:
        screen.blit(self.image, self.rect)
        
    def if_clicked(self) -> bool:
        c = False
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                c = True
        return c