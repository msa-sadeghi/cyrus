import random
from constants import *
from pygame.sprite import Sprite
from chickenEgg import ChickenEgg

class Chick(Sprite):
    def __init__(self, x,y, eggs_group) -> None:
        super().__init__()
        self.image = pygame.image.load("assets/chick.png")
        self.rect = self.image.get_rect(topleft = (x,y))
        self.eggs_group = eggs_group
        self.direction = 1
        self.speed = 4


    def update(self):
        self.rect.x += self.direction * self.speed
        if random.randint(0,200) > 198 and len(self.eggs_group) < 3:
            self.fire()

    def fire(self):
        ChickenEgg(self.rect.centerx, self.rect.centery, self.eggs_group)


    
