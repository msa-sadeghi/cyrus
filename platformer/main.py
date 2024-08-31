from constants import *
from world import World
import pickle
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
door_group = pygame.sprite.Group()

level = 1

def load_level_data(level):
    with open(f"levels\level{level}", "rb") as f:
        world_data = pickle.load(f)
    return world_data
world_data = load_level_data(level)
game_world = World(world_data, player_group, enemy_group, coin_group, door_group)

player = Player(100,500, enemy_group)


def next_level():
    global world_data 
    world_data= load_level_data(level)
    return reset_game()
    
    


def reset_game():
    enemy_group.empty()
    coin_group.empty()
    player.__init__(100,500, enemy_group)
    game_world = World(world_data, player_group, enemy_group,coin_group,door_group)
   
    return game_world
    

health_bar = HealthBar(10,10, player.health, player.max_health)
start = False
i = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_RETURN:
                start =True
    
               
    game_world.draw()
    print(world_data[-6][11])
    health_bar.draw(screen, player.health)
    player.update(game_world.tile_map , coin_group, door_group)
    player.draw(screen)
    enemy_group.update()
    enemy_group.draw(screen)
    coin_group.update()
    coin_group.draw(screen)
    door_group.draw(screen)
    if not player.alive:
        restart_button.draw(screen)
        
        if restart_button.check_click():
            
            game_world = reset_game()
    if player.next_level:
        if level < 10:
            level += 1
            game_world =next_level()     
        else:
            pass   
    pygame.display.update()
    clock.tick(FPS)