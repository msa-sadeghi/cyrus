from constants import *
from player import Player
from game import Game

chick_group = pygame.sprite.Group()
chick_egg_group = pygame.sprite.Group()

player_bullet_group = pygame.sprite.Group()
player = Player(player_bullet_group)

game = Game(player, chick_group,player_bullet_group, chick_egg_group)

game.start_new_level()

WELCOME_TEXT = font72.render("WELCOME TO SPACE GAME", True, (170,10,190))
WELCOME_RECT = WELCOME_TEXT.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
start_time = pygame.time.get_ticks()
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            if event.key == pygame.K_SPACE:
                player.shoot()
    SCREEN.fill((0,0,0))
    if pygame.time.get_ticks() - start_time < 2000:
        SCREEN.blit(WELCOME_TEXT, WELCOME_RECT)

    else:
        player.draw()
        player.move()
        chick_group.draw(SCREEN)
        chick_group.update()
        chick_egg_group.draw(SCREEN)
        chick_egg_group.update()
        player_bullet_group.draw(SCREEN)
        player_bullet_group.update()
        game.update()

    pygame.display.update()
    CLOCK.tick(FPS)