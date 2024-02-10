import pygame
screen = pygame.display.set_mode()
SCREEN_WIDTH = screen.get_width()
SCREEN_HEIGHT = screen.get_height()


ROWS = SCREEN_HEIGHT//32
COLS = SCREEN_WIDTH//32

print(ROWS)
print(COLS)
FPS = 60
clock = pygame.time.Clock()

ENEMY_IMG = pygame.transform.scale(pygame.image.load("assets/blob.png"), (32,32))
COIN_IMG = pygame.transform.scale(pygame.image.load("assets/coin.png"), (32,32))
DIRT_IMG = pygame.transform.scale(pygame.image.load("assets/dirt.png"), (32,32))
GRASS_IMG = pygame.transform.scale(pygame.image.load("assets/grass.png"), (32,32))
LAVA_IMG = pygame.transform.scale(pygame.image.load("assets/lava.png"), (32,32))
EXIT_IMG = pygame.transform.scale(pygame.image.load("assets/exit.png"), (32,32))
GHOST_IMG = pygame.transform.scale(pygame.image.load("assets/ghost.png"), (32,32))
RESTART_IMG = pygame.image.load("assets/restart_btn.png")
BG_IMG = pygame.image.load("assets/sky.png")