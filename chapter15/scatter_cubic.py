import matplotlib.pyplot  as plt 

x_value = list(range(5001))
y_value = [x**3 for x in x_value]
plt.scatter(x_value, y_value, s=1, c=y_value, cmap=plt.cm.Blues)#scatter（）函数是绘制散点图的函数；s=1是将每个散点的大小设为1；c=y_value, cmap=plt.cm.Blues颜色映射，从起始颜色到结束颜色

plt.title("cubic of number", fontsize=20)
plt.xlabel("value", fontsize=10)
plt.ylabel("cubic number", fontsize=10)

plt.tick_params(axis="both", labelsize=10)
plt.axis([0, 5000, 0, 125000000000])#axis([0, 5000, 0, 125000000000])是将x轴设置为0-5000，y轴设置为0-125000000000；

plt.show()
#plt.savefig('cubic_plot.png', bbox_inches='tight')#自动保存图标的函数，'cubic_plot.png'是将文件名保存成什么样的，bbox_inches='tight'是将图标多余的部分裁减掉