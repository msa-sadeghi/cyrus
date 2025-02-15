import pygame
from player import Player

screen = pygame.display.set_mode((800, 600))
my_player = Player(100, 400)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    my_player.draw(screen)       
    pygame.display.update()