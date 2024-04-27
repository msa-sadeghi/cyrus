from constants import *
from world import World
from levels.level1 import world_data
from button import Button
from healthbar import HealthBar
from player import Player
pygame.init()
restart_button = Button(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

pygame.mixer.music.load("assets/music.wav")
pygame.mixer.music.play(-1)

player_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()
game_world = World(world_data, player_group, enemy_group, coin_group)

player = Player(100,500, enemy_group)

def reset_game():
    enemy_group.empty()
    coin_group.empty()
    player.__init__(100,500, enemy_group)
    game_world = World(world_data, player_group, enemy_group,coin_group)
   
    return game_world
    

health_bar = HealthBar(10,10, player.health, player.max_health)

i = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                
    game_world.draw()
    health_bar.draw(screen, player.health)
    player.update(game_world.tile_map , coin_group)
    player.draw(screen)
    enemy_group.update()
    enemy_group.draw(screen)
    coin_group.update()
    coin_group.draw(screen)
    if not player.alive:
        restart_button.draw(screen)
        
        if restart_button.check_click():
            
            game_world = reset_game()
            
    pygame.display.update()
    clock.tick(FPS)