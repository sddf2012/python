import matplotlib.pyplot as plt
import numpy as np

# 创建带有两行两列子图的图表
fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(8, 6))

# 生成随机数据
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = np.exp(x)

# 在子图中绘制数据
axs[0, 0].plot(x, y1)
axs[0, 0].set_title('Sin(x)')
axs[0, 1].plot(x, y2)
axs[0, 1].set_title('Cos(x)')
axs[1, 0].plot(x, y3)
axs[1, 0].set_title('Tan(x)')
axs[1, 1].plot(x, y4)
axs[1, 1].set_title('Exp(x)')

# 调整布局
plt.tight_layout()

# 显示图表
plt.show()