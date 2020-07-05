import matplotlib.pyplot as plt 

x_value = [0, 1, 2, 3, 4, 5]
y_value = [0, 1, 4, 9, 16, 25]
plt.plot(x_value, y_value, linewidth=2)#plot()函数是将点绘制成折线图的函数；linewidth=2是将曲线宽度设为2

plt.title("square numbers", fontsize=20)#将标题"square numbers"字体大小设为20
plt.xlabel("value", fontsize=10)
plt.ylabel("square", fontsize=10)

plt.tick_params(axis="both", labelsize=10)#tick_params()函数是设置刻度式样的函数；axis="both"是将x,y轴都设置为整数；labelsize=10是将刻度标记的字号设为10

plt.show()