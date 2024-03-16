from constants import *
from player import Player
from enemy import Enemy
class World:
    def __init__(self, world_data, player_group, enemy_group):
        self.tile_map = []
        self.image = pygame.transform.scale(BG_IMG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.topleft = (0,0)
        self.player_group = player_group
        self.enemy_group = enemy_group
        
        for i in range(ROWS):
            for j in range(COLS):
                if world_data[i][j] == 1:
                    img = DIRT_IMG
                    rect = img.get_rect(topleft=(j*32, i*32))
                    self.tile_map.append((img,rect))
                if world_data[i][j] == 2:
                    img = GRASS_IMG
                    rect = img.get_rect(topleft=(j*32, i*32))
                    self.tile_map.append((img,rect))
                if world_data[i][j] == 3:
                    Enemy(j*32, i*32, self.enemy_group)
                if world_data[i][j] == 4:
                    player = Player(j*32, i*32, enemy_group)
                    self.player_group.add(player)
                    
        
        
        
    def draw(self):
        screen.blit(self.image, self.rect)
        for i in range(len(self.tile_map)):
                screen.blit(self.tile_map[i][0], self.tile_map[i][1])
            