import pygame
from player import Player
pygame.init()


width = 1000
height = 600

clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))
fps = 60

my_player = Player(100, 300)
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")
    my_player.draw(screen)
    my_player.move()
    pygame.display.update()
    clock.tick(fps)