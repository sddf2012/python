from random_walk import RandomWalk
import matplotlib.pyplot as plt

# while True:
#     msg = input("生成图片(y/n):")
#     if msg == "n":
#         break
rw = RandomWalk()
rw.fill_walk()

fig, ax = plt.subplots(figsize=(10, 7))
ax.scatter(rw.x_values, rw.y_values, s=1, c=range(rw.count), cmap=plt.cm.Blues)
# ax.plot(rw.x_values, rw.y_values)

ax.scatter(rw.x_values[0], rw.y_values[0], c="green", s=10)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c="red", s=10)

ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()
