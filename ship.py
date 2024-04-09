import pygame
import alien_invasion

class ship:
    """创建飞船图像类"""

    # 游戏管理类的屏幕对象
    screen=None
    # 屏幕对象的矩形
    screen_rect=None
    # 图像的路径
    image_path=None
    # 图像对象
    image=None
    # 图像对象的矩形
    rect=None
    # 向右移动标志
    moveFlag_right=False
    # 向左移动标志
    moveFlag_left=False
    # 图片矩形的x坐标
    x=None

    def __init__(self,ai_game) -> None:
        # 获取AlienInvasion类通过pygame.display.set_mode()生成的对屏幕对象变量
        ai_game:alien_invasion.AlienInvasion=ai_game
        self.screen=ai_game.screen
        self.setting=ai_game.Setting
        # 获取屏幕对象的矩形
        self.screen_rect=ai_game.screen.get_rect()
        # 要绘制成飞船的图像路径，如果是同一目录下直接文件名就行
        self.image_path='ship.PNG'
        # 传入路径生成图像对像
        self.image=pygame.image.load(self.image_path)
        # 获取图像的矩形对象
        self.rect=self.image.get_rect()
        # 把屏幕窗口对象的底部居中值给到图像的底中
        self.rect.midbottom=self.screen_rect.midbottom
        self.x=self.rect.x

    def blitme(self):
        """在屏幕对象中绘制图像"""
        self.screen.blit(self.image,self.rect)

    def update(self):
        """更新飞船的坐标得到移动的效果"""
        # 图像矩形x坐标左右移动的条件 and 右边的条件是屏幕窗口右边值大于图像右边值
        if self.moveFlag_right and self.screen_rect.right>self.rect.right:
            self.x+=self.setting.ship_speed
        elif self.moveFlag_left and self.rect.left>0:
            self.x-=self.setting.ship_speed
        self.rect.x=self.x