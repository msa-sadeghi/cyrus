import pygame
from person import Person
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640
FPS = 60
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
enemy_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
grenade_group = pygame.sprite.Group()
explosion_group = pygame.sprite.Group()
player = Person('player', 100, 300, 50, 10, 100)
enemy = Person('enemy', 400, 300, 50, 0, 100)
enemy_group.add(enemy)
moving_left = False
moving_right = False
jumped = False
shoot = False
grenade_thrown = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moving_left = True
            if event.key == pygame.K_RIGHT:
                moving_right = True
            if event.key == pygame.K_UP:
                jumped = True
            if event.key == pygame.K_SPACE:
                shoot = True
            if event.key == pygame.K_g:
                grenade_thrown = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False
            if event.key == pygame.K_RIGHT:
                moving_right = False
            if event.key == pygame.K_UP:
                jumped = False
            if event.key == pygame.K_SPACE:
                shoot = False
            if event.key == pygame.K_g:
                grenade_thrown = False
    screen.fill((0, 0, 0))
    if player.alive:
        if moving_left or moving_right:
            player.change_action("Run")
        elif jumped:
            player.y_velocity = -13
            player.in_air = True

        else:
            player.change_action("Idle")
        if player.in_air:
            player.change_action("Jump")
        player.move(moving_left, moving_right)
        player.gravity()
        if shoot:
            player.shoot("bullet",bullet_group)
        elif grenade_thrown:
            player.shoot("grenade", grenade_group)
    player.draw(screen)
    enemy_group.draw(screen)
    enemy_group.update()
    bullet_group.draw(screen)
    bullet_group.update()
    grenade_group.draw(screen)
    grenade_group.update(explosion_group)
    explosion_group.update()
    explosion_group.draw(screen)
    pygame.display.update()
    clock.tick(FPS)
