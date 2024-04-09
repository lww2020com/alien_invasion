import sys
import pygame
import Setting
import ship
import buttle
import alien

class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self) -> None:
        """初始化游戏并创建游戏资源"""
        pygame.init()
        # 创建settings对象设置屏幕尺寸
        self.Setting=Setting.settings(800,600)
        self.screen=pygame.display.set_mode((self.Setting.screenWidth,self.Setting.screenHeight))
        # 设置屏幕标题
        pygame.display.set_caption("外星入侵")
        # 创建飞船ship对象，传入当前alienInvasion对象为参数
        self.ship=ship.ship(self)
        # 创建子弹的精灵组，用于放子弹精灵
        self.buttles=pygame.sprite.Group()
        self.aliens=pygame.sprite.Group()
        self._create_aliens()
        self.clock=pygame.time.Clock()

    def _create_aliens(self):
        """创建敌机并放入精组灵"""
        alien_1=alien.alien(self)
        alien_width=alien_1.rect.width
        alien_height=alien_1.rect.height
        current_x=alien_1.rect.x
        current_y=alien_1.rect.y
        # self.aliens.add(alien_1)
        # print(alien_1.rect.x)
        # print(self.Setting.screenWidth)
        # i=0
        while current_y <(self.Setting.screenHeight-3*alien_height):
            while current_x<(self.Setting.screenWidth-alien_width):
                print(current_x)
                alien_2=alien.alien(self)
                alien_2.x=current_x
                alien_2.rect.x=current_x
                alien_2.rect.y=current_y
                self.aliens.add(alien_2)
                current_x+=alien_width+10
            # self.bgcolor=(230,230,230)s
            current_x=alien_1.rect.x
            current_y+=alien_width+20
    def run_game(self):
        """开始游戏的主循环"""

        while True:
            # 侦听键盘和鼠标事件
            self._check_events()

            self.ship.update()

            self._updata_buttles()
            self._check_aliens_edges()
            self.aliens.update()
                # print(len(self.buttles))            
            self._update_screen()

            self.clock.tick(60)

    def _updata_buttles(self):

        self.buttles.update()
            
        self._remove_buttle()

    def _remove_buttle(self):
        """通过copy()函数返回的列表的副本，遍历它并从精灵组中移除到达顶端的子弹"""
        for v in self.buttles.copy():
            if v.rect.bottom<=0:
                self.buttles.remove(v)
        collisicons=pygame.sprite.groupcollide(self.buttles,self.aliens,True,True)

    def _update_screen(self):
        """更新屏幕，并切的换到新屏幕"""
        # 填充屏幕背景
        self.screen.fill(self.Setting.bgColor)
        
        for v in self.buttles.sprites():
            v.draw_buttle()

        # 调用ship对象的blitem自定义方法绘制飞船图像
        self.ship.blitme()

        self.aliens.draw(self.screen)

        # self.alien=alien.alien(self)
        # self.alien.draw_alien()

        # 显示最近绘制的屏幕
        pygame.display.flip()

    def _check_events(self):
        # 获取并遍历事件模块
        for event in pygame.event.get():
                # Pygame Event事件模块 QOUIT 用户按下窗口的关闭按钮	
            if event.type==pygame.QUIT:
                    # 退出系统
                sys.exit()
            # 键盘按键事件,调用自定义函数_check_keydown_event(event)
            elif event.type==pygame.KEYDOWN:
                self._check_keydown_events(event)
            # 键盘释放事件,调用自定义函数_check_keyup_event(event)
            elif event.type==pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keyup_events(self, event):
        if event.key==pygame.K_RIGHT:
            self.ship.moveFlag_right=False
        elif event.key==pygame.K_LEFT:
            self.ship.moveFlag_left=False

    def _check_keydown_events(self, event):
        if event.key==pygame.K_RIGHT:
            self.ship.moveFlag_right=True
        elif event.key==pygame.K_LEFT:
            self.ship.moveFlag_left=True
        elif event.key==pygame.K_SPACE:
            self._fire_buttle()

    def _fire_buttle(self):
        """创建子弹对象并放入精灵组"""
        bul=buttle.buttle(self)
        self.buttles.add(bul)
    
    def _check_aliens_edges(self):
        """在有外星人到达边缘时采取相应的措施"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_aliens_direction()
                break
    
    def _change_aliens_direction(self):
        """将整个队列向下移动,并改变配置对象中alien_direction的值"""
        for alien in self.aliens.sprites():
            alien.rect.y+=self.Setting.alien_drop_speed
        self.Setting.alien_direction*=-2


if __name__=='__main__':
    ai=AlienInvasion()
    ai.run_game()
    