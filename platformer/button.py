from constants import *
class Button:
    def __init__(self,x,y):
        self.image = RESTART_IMG
        self.rect = self.image.get_rect(center=(x,y))
        self.clicked = False
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def check_click(self):
        action = False
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                action = True
                self.clicked = True
        if not pygame.mouse.get_pressed()[0]    :
            self.clicked = False
        return action