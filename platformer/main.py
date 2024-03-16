from constants import *
from world import World
from levels.level1 import world_data

player_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
game_world = World(world_data, player_group, enemy_group)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                
    game_world.draw()
    player_group.update(game_world.tile_map)
    player_group.draw(screen)
    enemy_group.update()
    enemy_group.draw(screen)
    pygame.display.update()
    clock.tick(FPS)