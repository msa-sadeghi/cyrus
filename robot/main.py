import pygame
from player import Player
from rock import Rock
from world import World
pygame.init()
import pickle
import os
TILE_SIZE = 50
WIDTH = 1000
HEIGHT = 600
images = [
    pygame.transform.scale(pygame.image.load(f"tiles/png/Tile/{img}"), (TILE_SIZE, TILE_SIZE))
    for img in os.listdir(f"./tiles/png/Tile")
]
bg_image = pygame.image.load("./tiles/png/BG.png")
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))

def load_level(level):
    with open(f"level{level}.dat", "rb") as file:
        level_data = pickle.loads(file.read())
        
        new_world = World(level_data, images, TILE_SIZE)

    return new_world
        
rock_group = pygame.sprite.Group()
level = 2
width = 1000
height = 600

clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))
fps = 60

rock = Rock()
rock_group.add(rock)
bullet_group = pygame.sprite.Group()
my_player = Player(100, 300)
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if my_player.in_air:
        my_player.change_animation("Jump")
    elif my_player.sliding:
        my_player.change_animation("Slide")
    elif my_player.run_shoot:
        my_player.change_animation('RunShoot')
    elif my_player.idle:
        my_player.change_animation("Idle")

    else:
        my_player.change_animation("Run")
 
    game_world = load_level(level)
    screen.blit(bg_image , (0,0))
    game_world.draw(screen)
   
    my_player.draw(screen)
    my_player.move(bullet_group)
    rock_group.update(my_player)
    rock_group.draw(screen)
    bullet_group.update()
    bullet_group.draw(screen)
    
    pygame.display.update()
    clock.tick(fps)