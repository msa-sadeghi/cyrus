import pygame
from castle import Castle
from healthbar import HealthBar
from game import Game
bullet_group = pygame.sprite.Group()
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
castle = Castle(SCREEN_WIDTH-270, SCREEN_HEIGHT -350)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
FPS = 60    
bg = pygame.image.load("assets/bg.png")

level = 1
castle_healthbar = HealthBar(600, 200, castle.health, castle.max_health)
font = pygame.font.SysFont("arial", 20)



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
   
    
    screen.blit(bg, (0,0))
    Game.show_scoreboard(font, level, castle.money, castle.ammo, screen)
    castle.draw(screen)
    castle.shoot(bullet_group)
    bullet_group.update()
    bullet_group.draw(screen)
    castle_healthbar.draw(screen, castle.health)
    pygame.display.update()
    clock.tick(FPS)