import random
class RandomWalk:
    """创建随机游戏类"""
    def __init__(self,num_points=5000) -> None:
        # 初始化点数
        self.num_point=num_points
        # 初始化x轴坐标列表
        self.x_values=[0]
        # 初始化y轴坐标列表
        self.y_values=[0]
    
    def fill_walk(self):
        """填充随机游走数据"""
        # 当x_values列表元素个数小于初始化点数时进去循环
        while len(self.x_values)<self.num_point:
            # x轴向左还是向右random.choice([])列表中随机返回值
            x_direction=random.choice([1,-1])
            # x轴移动的距离值
            x_distance=random.choice([0,1,2,3,4,5])
            # 计算出x轴向指定方向移动的步数
            x_step=x_direction*x_distance
            # y轴向上还是向下random.choice([])列表中随机返回值
            y_direction=random.choice([1,-1])
            # y轴移动的距离值
            y_distance=random.choice([0,1,2,3,4,5])
            # 计算出y轴向指定方向移动的步数
            y_step=y_direction*y_distance
            # 取列表最后一个元素与计算出的步数做和运算
            x=self.x_values[-1]+x_step
            y=self.y_values[-1]+y_step
            # 防止原地踏步
            if x_step==0 and y_step==0:
                continue
            # 向列表插入数据    
            self.x_values.append(x)
            self.y_values.append(y)