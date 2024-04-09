class settings:
    """游戏配置类"""

    # 屏幕宽度
    screenWidth=None
    # 屏幕高度
    screenHeight=None
    # 屏幕背景色
    bgColor=None
    # 飞船的速度
    ship_speed=None
    # 子弹的速度
    buttle_speed=None
    # 子弹的宽
    buttle_width=None
    # 子弹的高
    buttle_hight=None
    # 了弹的颜色
    buttle_color=()
    
    def __init__(self,screenWidth,screenHeight,shipSpeed=1) -> None:
        self.screenWidth=screenWidth
        self.screenHeight=screenHeight
        self.bgColor=(230,230,230)
        self.ship_speed=shipSpeed

        self.buttle_speed=2.0
        self.buttle_width=1
        self.buttle_hight=15
        self.buttle_color=(60,60,60)

        self.alien_speed=1
        self.alien_drop_speed=10
        self.alien_direction=1
    def setBackground(self,r,g,b):
        self.bgColor=(r,g,b)