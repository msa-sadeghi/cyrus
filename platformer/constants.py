import pygame
screen = pygame.display.set_mode()
SCREEN_WIDTH = screen.get_width()
SCREEN_HEIGHT = screen.get_height()
FPS = 60
clock = pygame.time.Clock()

ENEMY_IMG = pygame.image.load("assets/blob.png")
COIN_IMG = pygame.image.load("assets/coin.png")
DIRT_IMG = pygame.image.load("assets/dirt.png")
GRASS_IMG = pygame.image.load("assets/grass.png")
WATER_IMG = pygame.image.load("assets/water.png")
LAVA_IMG = pygame.image.load("assets/lava.png")
EXIT_IMG = pygame.image.load("assets/exit.png")
GHOST_IMG = pygame.image.load("assets/ghost.png")
RESTART_IMG = pygame.image.load("assets/restart_btn.png")