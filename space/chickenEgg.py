from constants import *
from pygame.sprite import Sprite
class ChickenEgg(Sprite):
    def __init__(self, x,y, egg_group):
        super().__init__()
        image = pygame.image.load("assets/egg.png")
        self.image = pygame.transform.scale(image, (image.get_width() * 0.7, image.get_height() * 0.7))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speed = 10
        egg_group.add(self)


    def update(self):
        self.rect.y += self.speed

        if self.rect.top >= SCREEN_HEIGHT:
            self.kill()