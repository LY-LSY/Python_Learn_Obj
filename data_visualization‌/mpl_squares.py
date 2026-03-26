import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

fig, ax = plt.subplots()
ax.plot(squares)

# 设置图题并给坐标加上标签
ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of Value', fontsize=14)

# 设置刻度标记的样式
ax.tick_params(labelsize=14)

plt.show()