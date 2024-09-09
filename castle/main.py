import pygame
from castle import Castle
from healthbar import HealthBar
from game import Game
from enemy import Enemy
from random import randrange
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


MAX_DIFFICAULTY = 1000
level_difficulty = 0

enemy_group = pygame.sprite.Group()

all_enemy_types = ("knight", "goblin", "red_goblin", "purple_goblin")
all_enemy_healths = (100, 125, 150,175)
all_enemy_speeds = (1, 1, 2,2)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
   
    while level_difficulty < MAX_DIFFICAULTY:
        i = randrange(len(all_enemy_types))
        e = Enemy(
                    all_enemy_types[i],
                    all_enemy_healths[i],
                    all_enemy_speeds[i],
                    enemy_group,
                    100, 
                    300
                  )
        level_difficulty += all_enemy_healths[i]
    print(len(enemy_group))    
    screen.blit(bg, (0,0))
    Game.show_scoreboard(font, level, castle.money, castle.ammo, screen)
    castle.draw(screen)
    castle.shoot(bullet_group)
    bullet_group.update()
    bullet_group.draw(screen)
    enemy_group.update()
    enemy_group.draw(screen)
    castle_healthbar.draw(screen, castle.health)
    pygame.display.update()
    clock.tick(FPS)