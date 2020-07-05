import matplotlib.pyplot as plt 

from random_walk import RandomWalk 

while True:
    rw = RandomWalk()
    rw.fill_walk()

    plt.figure(dpi=128, figsize=(7, 3))#figure()函数用于指定图表的宽度、高度、分辨率和背景色的。

    point_numbers = list(range(rw.number_points))
    plt.scatter(rw.x_values, rw.y_values, s=1, c=point_numbers, cmap=plt.cm.Blues)

    plt.scatter(0, 0, s=10, c="black")#将起始点和终点以不同的颜色标记出来
    plt.scatter(rw.x_values[-1], rw.y_values[-1], s=10, c="red")

    plt.axes().get_xaxis().set_visible(False)#将坐标轴影藏起来
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make anther walk? (yes/no): ")
    if keep_running == "no":
        break