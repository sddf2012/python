import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import export_text
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

iris=load_iris()
X_train, X_test, y_train, y_test=train_test_split(iris.data,iris.target,random_state=1)

clf = DecisionTreeClassifier(criterion='gini', max_depth=3)
# 训练模型
clf.fit(X_train, y_train)

# 预测
y_pred = clf.predict(X_test)

# 计算准确率
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')
print(iris.feature_names)
# 输出特征重要性
feature_importances = clf.feature_importances_
for feature, importance in zip(iris.feature_names, feature_importances):
    print(f'{feature}: {importance:.4f}')
# 输出决策树
tree_rules = export_text(clf, feature_names=iris.feature_names)
print(tree_rules)

plt.figure(figsize=(20,10))
plot_tree(clf, feature_names=iris.feature_names, class_names=iris.target_names, filled=True)
plt.show()