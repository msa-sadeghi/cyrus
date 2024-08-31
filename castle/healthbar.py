import pygame
class HealthBar:
    def __init__(self, x,y, health, max_health):
        self.x = x
        self.y = y
        self.health = health
        self.max_health = max_health
        self.font = pygame.font.SysFont("arial", 18)
        self.text = self.font.render(str(health), True, (0,0,0))
        self.rect = self.text.get_rect(topright=(self.x + 60, 200))
        
    def draw(self, screen, health):
        self.text = self.font.render(str(health), True, (0,0,0))
        self.health = health
        ratio = self.health / self.max_health
        pygame.draw.rect(screen, (255, 0,0), (self.x, self.y, 80, 20))
        pygame.draw.rect(screen, (0, 255,0), (self.x, self.y, 80 * ratio, 20))
        screen.blit(self.text, self.rect)
        
        