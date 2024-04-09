import pygame
import alien_invasion 
# 导入pygame的精灵类
from pygame.sprite import Sprite
class buttle(Sprite):
    """子弹类并继承精灵类"""
   
    def __init__(self,ai_game) -> None:
        super().__init__()
        # 获取传入的游戏管理在行业类
        ai_game:alien_invasion.AlienInvasion=ai_game
        # 获取游戏管理初始化时创建的setting对象
        self.setting=ai_game.Setting
        # 获取游戏管理初始化时创建的screen对象
        self.screen=ai_game.screen
        # self.color=self.setting.buttle_color
        # 这里通过图像绘制子弹，不通过注释掉的代码手动绘制子弹
        self.image=pygame.image.load("laserGreen13.png")
        self.rect=self.image.get_rect()
        # self.rect=pygame.Rect(0,0,self.setting.buttle_width,self.setting.buttle_hight)
        self.rect.midtop=ai_game.ship.rect.midtop
        self.y=self.rect.y
    
    def update(self) -> None:
        self.y-=self.setting.buttle_speed
        self.rect.y=self.y

    def draw_buttle(self):
        # pygame.draw.rect(self.screen,self.color,self.rect)
        self.screen.blit(self.image,self.rect)