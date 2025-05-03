import pygame

class World:
    def __init__(self, data, images, TILE_SIZE):
        
        self.tiles = []
        for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i][j] != -1:
                    tile = (images[data[i][j]], images[data[i][j]].get_rect(topleft = (j * TILE_SIZE , i *  TILE_SIZE)))
                    self.tiles.append(tile)

    def draw(self, screen):
        for tile in self.tiles:
            screen.blit(tile[0], tile[1])