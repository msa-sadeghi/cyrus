from pygame.sprite import Sprite
from constants import *

from playerBullet import PlayerBullet
class Player(Sprite):
    def __init__(self, bullet_group):
        super().__init__()
        self.image = pygame.image.load("assets/space_rocket.png")
        self.rect = self.image.get_rect(bottom = SCREEN_HEIGHT, centerx = SCREEN_WIDTH/2)
        self.velocity = 5
        self.bullet_group = bullet_group
        self.last_fire_time = pygame.time.get_ticks()


    def draw(self):
        SCREEN.blit(self.image, self.rect)


    def move(self):
        keys = pygame.key.get_pressed()
        # if keys[pygame.K_UP] and self.rect.top > 100:
        #     self.rect.y -= self.velocity
        # if keys[pygame.K_DOWN] and self.rect.bootom < SCREEN_HEIGHT:
        #     self.rect.y += self.velocity
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.velocity

    def shoot(self):
        if pygame.time.get_ticks() - self.last_fire_time > 400:

            PlayerBullet(self.rect.centerx, self.rect.top, self.bullet_group)
            self.last_fire_time = pygame.time.get_ticks()

