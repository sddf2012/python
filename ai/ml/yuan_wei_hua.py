from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

import numpy as np
import pandas as pd
import mglearn
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
from sklearn.neighbors import KNeighborsClassifier

iris_dataset = load_iris()

# print(f"Keys of iris_dataset: {iris_dataset.keys()}")
# print(iris_dataset)

X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state=0)

# print(X_test.shape)
# print(X_train.shape)
# iris_dataframe = pd.DataFrame(X_train, columns=iris_dataset.feature_names)
# scatter_matrix(iris_dataframe, c=y_train, figsize=(15, 15), marker='o',hist_kwds={'bins': 20}, s=60, alpha=.8, cmap=mglearn.cm3)
# plt.show()

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)

# X_new = np.array([[5, 2.9, 1, 0.2]])
# prediction = knn.predict(X_new)
# print(prediction)
# print(iris_dataset['target_names'][prediction])

y_pred = knn.predict(X_test)
print(y_pred)
print(knn.score(X_test, y_test))