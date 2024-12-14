import pygame
from person import Person
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640
FPS = 60
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
enemy_group = pygame.sprite.Group()
player = Person('player', 100, 300, 50, 10, 100)
enemy = Person('enemy', 400, 300, 50, 0, 100)
enemy_group.add(enemy)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    player.draw(screen)
    enemy_group.draw(screen)
    enemy_group.update()
    pygame.display.update()
    clock.tick(FPS)
    
    