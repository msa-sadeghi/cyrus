from constants import *
from chick import Chick

class Game:
    def __init__(self, player, chick_group, player_bullet_group, chick_egg_group) -> None:
        self.player = player
        self.chick_group = chick_group
        self.player_bullet_group = player_bullet_group
        self.chick_egg_group = chick_egg_group
        self.font = pygame.font.Font("assets/AttackGraffiti.ttf",32)
        self.score = 0
        self.level_number = 1

    def start_new_level(self):
        for i in range(2 * self.level_number):
            for j in range(2 * self.level_number):
                chick = Chick(j * 64, i*64, self.chick_egg_group)
                self.chick_group.add(chick)




    def update(self):
        self.if_on_edge_bounce()
        self.check_collisions()
        self.check_round_completion()


    def draw(self):
        score_text = self.font.render(f"Score:{self.score}", True, (190,10, 170))
        score_rect = score_text.get_rect()

    def check_collisions(self):
        if pygame.sprite.groupcollide(self.player_bullet_group, self.chick_group, True, True):
            pass
        if pygame.sprite.spritecollide(self.player, self.chick_egg_group, True):
            self.player.lives -= 1

    
    def check_round_completion(self):
        if len(self.chick_group) == 0:
            self.level_number += 1
            self.start_new_level()

    
    def if_on_edge_bounce(self):
        on_edge = False
        for chick in self.chick_group:
            if chick.rect.right >= SCREEN_WIDTH or chick.rect.left <= 0:
                on_edge = True
                break
        if on_edge:
            for chick in self.chick_group:
                chick.direction *= -1
                chick.rect.y += self.level_number * 10



