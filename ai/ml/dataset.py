import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
import pandas as pd
import mglearn


# cancer = load_breast_cancer()
# print(cancer.keys())
# print(cancer.target_names)
# print(cancer.feature_names)

# # 创建 DataFrame
# df = pd.DataFrame(data=cancer.data, columns=cancer.feature_names)
# df['target'] = cancer.target

# print(df.head())

X, y = mglearn.datasets.make_forge()
# 数据集绘图
mglearn.discrete_scatter(X[:, 0], X[:, 1], y)
plt.legend(["Class 0", "Class 1"], loc=4)
plt.xlabel("First feature")
plt.ylabel("Second feature")
print("X.shape: {}".format(X.shape))

mglearn.plots.plot_knn_classification(n_neighbors=1)