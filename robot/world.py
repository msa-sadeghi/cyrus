import pygame
from obstacle import Obstacle
class World:
    def __init__(self, data, images, TILE_SIZE):
        
        self.tiles = []
        self.obstacles = []
        
        for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i][j] != -1:
                    
                    if 0<= data[i][j] <= 15:                   

                        self.obstacles.append(Obstacle('ground', j * TILE_SIZE , i *  TILE_SIZE, images[data[i][j]]))

                    # tile = (images[data[i][j]], images[data[i][j]].get_rect(topleft = (j * TILE_SIZE , i *  TILE_SIZE)))
                    # self.tiles.append(tile)
      
        
    def draw(self, screen):
        # for tile in self.tiles:
        #     screen.blit(tile[0], tile[1])
        for obs in self.obstacles:
            obs.draw(screen)

    # def check_collisions(self, player):
