import matplotlib.pyplot as plt
import numpy as np

# 生成示例数据
x = np.linspace(0, 10, 100)
print(x)
y1 = np.sin(x)
y2 = np.cos(x)

# 绘制图形
plt.plot(x, y1, label='Sine Wave')
plt.plot(x, y2, label='Cosine Wave')

# 添加图例
plt.legend(loc='upper right', fontsize='large', title='Trigonometric Functions', title_fontsize='medium', ncol=1, frameon=True)

# 显示图形
plt.show()