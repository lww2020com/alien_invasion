from typing import Any
import pygame
import alien_invasion
from pygame.sprite import Sprite

class alien(Sprite):

    def __init__(self,ai_game) -> None:
        super().__init__()
        ai_game:alien_invasion.AlienInvasion=ai_game
        self.screen=ai_game.screen
        self.setting=ai_game.Setting
        self.image=pygame.image.load('enemyBlue1.png')
        self.rect=self.image.get_rect()
        self.rect.x=45
        self.rect.y=20
        self.x=self.rect.x
    
    def update(self) -> None:
        self.x+=self.setting.alien_speed*self.setting.alien_direction
        self.rect.x=self.x
    # def draw_alien(self):
    #     self.screen.blit(self.image,self.rect)
    def check_edges(self):
        self.screen_rect=self.screen.get_rect()
        return self.rect.right>=self.screen_rect.right or self.rect.left<=0