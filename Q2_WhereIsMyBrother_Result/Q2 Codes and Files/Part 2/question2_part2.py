
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset_train = pd.read_csv('fixture.csv')
dataset = pd.read_csv('test_fixture_edited.csv')







X_train= dataset_train.iloc[:, 7:].values
y_home_train= dataset_train.iloc[:,5].values
y_away_train= dataset_train.iloc[:,6]



X_test= dataset.iloc[:, 7:].values
y_home_test= dataset.iloc[:,5].values
y_away_test= dataset.iloc[:,6]


#For Home



from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(X_train, y_home_train)


y_pred_home = regressor.predict(X_test)



X_grid = np.arange(min(X_test), max(X_test), 0.01)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X_test, y_pred_home, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
plt.title('Overall Power Difference or Home Score (Decision Tree Regression)')
plt.xlabel('Overall Power Difference')
plt.ylabel('Home Score')
plt.show()





#For Away



from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(X_train, y_away_train)




y_pred_away = regressor.predict(X_test)



X_grid = np.arange(min(X_test), max(X_test), 0.01)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X_test, y_pred_away, color = 'green')
plt.plot(X_grid, regressor.predict(X_grid), color = 'violet')
plt.title('Overall Power Difference or Away Score (Decision Tree Regression)')
plt.xlabel('Overall Power Difference')
plt.ylabel('Away Score')
plt.show()








