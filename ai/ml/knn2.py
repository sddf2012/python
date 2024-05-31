from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.datasets import load_iris

iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 使用交叉验证选择最佳 K 值
k_values = range(1, 31)
cv_scores = []

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn, X_train, y_train, cv=10, scoring='accuracy')
    cv_scores.append(scores.mean())

# 找到最佳的 K 值
best_k = k_values[np.argmax(cv_scores)]
print(f"The best K value is: {best_k}")

# 绘制 K 值与交叉验证准确率的关系图
import matplotlib.pyplot as plt
plt.plot(k_values, cv_scores)
plt.xlabel('K Value')
plt.ylabel('Cross-Validated Accuracy')
plt.title('K Value vs. Cross-Validated Accuracy')
plt.show()