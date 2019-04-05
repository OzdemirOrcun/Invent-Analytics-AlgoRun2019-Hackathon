import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


dataset_backup = pd.read_csv('stats_datawteamranks.csv')
dataset = pd.read_csv('stats_datawteamranks.csv')

dataset['Possession'] = dataset['Possession'].str.rstrip('%').astype('float') / 10.0

X= dataset.iloc[:, [2,3,4,5,6]]
y= dataset.iloc[:,8].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)



#Building the optimal model using Backward Elimination
import statsmodels.formula.api as sm
X_new = np.append(arr = np.ones((784,1)).astype(int),values = X,axis = 1)
X_opt = X_new[:, [1, 2, 3, 4, 5]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
results_summary_STC = regressor_OLS.summary()
print (results_summary_STC)



















