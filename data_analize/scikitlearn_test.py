import matplotlib.pyplot as plt
import pandas as pd

# 古い記述方法
# import sklearn.datasets
# import sklearn.linear_model
# import sklearn.model_selection

# boston = sklearn.datasets.load_boston()

# X = boston.data
# df = pd.DataFrame(boston.data, columns=boston.feature_names)

# 新しい記述方法(ボストン住宅価格事情)
from sklearn.datasets import fetch_openml
housing = fetch_openml(name="house_prices", as_frame=True)
# print(type(housing))
# # print(housing)

# df = pd.DataFrame(housing.data,columns=housing.feature_names)
# print(df)
# print(df['MSSubClass'])
# print(housing.target)

X = housing.data
y = housing.target

import sklearn.datasets
import sklearn.linear_model
import sklearn.model_selection
X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X,y, test_size=0.2)

# 線形階乗
lr = sklearn.linear_model.LinearRegression()
lr.fit(X_train,y_train)
lr.score(X_test, y_test)
#ValueError (RL)が発生するのでここはこれまで

predicted = lr.predict(X)

fig, ax = plt.subplots()
ax.scatter(y,predicted,edgecolors=(0,0,0))
ax.plot([y.min(), y.max()], [y.min(), y.max()], 'k--',lw=4)
ax.set_xlabel('Measured')
ax.set_ylabel('Predicted')
plt.show()