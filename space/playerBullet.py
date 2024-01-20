from pygame.sprite import Sprite
import pygame


class PlayerBullet(Sprite):
    def __init__(self, x,y, bullet_group):
        super().__init__()
        self.image = pygame.image.load("assets/player_bullet.png")
        self.rect = self.image.get_rect(center=(x,y))
        bullet_group.add(self)
        self.velocity = 5


    def update(self):
        self.rect.y -= self.velocity
        if self.rect.bottom <= 0:
            self.kill()