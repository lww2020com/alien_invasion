
import matplotlib.animation as ani
import matplotlib.pyplot as plt
import random_walk



    # plt.ion()
    # 创建画板、创建一个或多个子图
fig,ax=plt.subplots()
    #设置全局字体为楷体，防止中文乱码
plt.rcParams['font.sans-serif']=['Kaiti']
    # 修复负号问题
plt.rcParams['axes.unicode_minus']=False 

        #清除上一幅图像，防止重叠
        # 擦除子图，防止重叠
        # plt.cla()
        # 获取或创建子图
ax1=plt.subplot()
        # 创建随机游戏对象
rw=random_walk.RandomWalk()
        # 调用方法填充数据
rw.fill_walk()
        # 绘制散点图
ax1.scatter(rw.x_values,rw.y_values,s=1,c=rw.y_values,cmap='Reds')

def update(n):
    plt.cla()
    # 创建随机游戏对象
    rw=random_walk.RandomWalk()
   # 调用方法填充数据
    rw.fill_walk()
    ax1.scatter(rw.x_values,rw.y_values,s=1,c=rw.y_values,cmap='Reds')
    pass

anim=ani.FuncAnimation(fig,func=update,frames=None,interval=5000)
        
plt.show()