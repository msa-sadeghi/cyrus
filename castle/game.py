import pygame
class Game:
    
    def show_scoreboard(font, level, castle_money, castle_ammo, screen):
        level_text = font.render(f"Level: {level}", True, (210, 10, 120))
        screen.blit(level_text, (0,0))
        money_text = font.render(f"money: {castle_money}", True, (210, 10, 120))
        screen.blit(money_text, (90,0))
        ammo_text = font.render(f"ammo: {castle_ammo}", True, (210, 10, 120))
        screen.blit(ammo_text, (0,45))
        
        