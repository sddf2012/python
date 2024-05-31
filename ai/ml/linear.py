import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# import mglearn


# mglearn.plots.plot_linear_regression_wave()
iris=load_iris()
X_train, X_test, y_train, y_test=train_test_split(iris.data,iris.target,random_state=1)

model=LinearRegression()
lr=model.fit(X_train,y_train)
# print(lr.coef_)
# print(lr.intercept_)

print(lr.score(X_test, y_test))
print(lr.score(X_train, y_train))