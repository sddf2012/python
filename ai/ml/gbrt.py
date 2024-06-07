import numpy as np
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error

# 创建一个回归数据集
X, y = make_regression(n_samples=1000, n_features=20, n_informative=15, random_state=42)

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 初始化GBRT模型
gbrt = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)

# 拟合模型
gbrt.fit(X_train, y_train)

# 预测
y_pred = gbrt.predict(X_test)

# 计算并打印均方误差
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# 打印模型的特征重要性
feature_importances = gbrt.feature_importances_
print("Feature Importances:")
for feature, importance in zip(range(X.shape[1]), feature_importances):
    print(f"Feature {feature}: {importance}")
