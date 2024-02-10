from constants import *
from world import World
from levels.level1 import world_data


game_world = World(world_data)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                
    game_world.draw()
    pygame.display.update()
    clock.tick(FPS)