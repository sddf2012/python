import numpy as np

rnd = np.random.RandomState(42)
x = rnd.uniform(-3, 3, 10)
print(x)
y_no_noise = (np.sin(4 * x) + x)
y = (y_no_noise + rnd.normal(size=len(x))) / 2
print(y)
