import matplotlib.pyplot as plt

# 设置字体名称和大小
plt.rcParams['font.family'] = 'SimHei'  # 使用中文字体（例如：宋体、黑体等）
plt.rcParams['font.size'] = 12

# 六个点的坐标
x = [0.186350, 0.21674, 0.20785, 0.164850, 0.186350, 0.20785]
y = [0.062099, 0.0925, 0.114, 0.157, 0.208889, 0.157]

# 绘制散点图
plt.scatter(x, y)

# 添加文本标注
for i in range(len(x)):
    plt.annotate(str(i+1), (x[i], y[i]), textcoords="offset points", xytext=(0,10), ha='center')

# 设置横轴和纵轴的标题
plt.xlabel('X轴')
plt.ylabel('Y轴')
plt.axis('equal')

# 设置图表标题
plt.title('六个点在二维平面上的位置')

# plt.xlim(0, 0.225)

fig = plt.gcf()
fig.set_size_inches(5,5)

# 显示图表
plt.show()