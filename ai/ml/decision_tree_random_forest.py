from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import numpy as np

# 加载数据集
iris = load_iris()
X = iris.data
y = iris.target

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 创建随机森林分类器
rf_clf = RandomForestClassifier(n_estimators=100, criterion='gini', max_depth=None, random_state=42)

# 训练模型
rf_clf.fit(X_train, y_train)

# 预测
y_pred = rf_clf.predict(X_test)

# 计算准确率
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

# 输出特征重要性
feature_importances = rf_clf.feature_importances_
for feature, importance in zip(iris.feature_names, feature_importances):
    print(f'{feature}: {importance:.4f}')

# 可视化特征重要性
plt.figure(figsize=(10,6))
indices = np.argsort(feature_importances)
plt.barh(range(len(indices)), feature_importances[indices], color='b', align='center')
plt.yticks(range(len(indices)), [iris.feature_names[i] for i in indices])
plt.xlabel('Relative Importance')
plt.title('Feature Importances in Random Forest')
plt.show()
