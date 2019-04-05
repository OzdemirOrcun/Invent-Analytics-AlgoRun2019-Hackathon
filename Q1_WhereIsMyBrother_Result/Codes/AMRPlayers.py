# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 19:44:47 2019

@author: Orçun
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


dataset = pd.read_csv('AMRplayersdeneme.csv')

dataset['Value'] = pd.to_numeric(dataset['Value'], errors='coerce')

dataset.loc[:,'Height'] *= 1/10 #seems to prevent SettingWithCopyWarning 


X= dataset.iloc[:, 4:]
y= dataset.iloc[:,3].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)



#Building the optimal model using Backward Elimination
import statsmodels.formula.api as sm
##############CHANGE DATASET SIZE HERE (375 YERINE)##################
X_new = np.append(arr = np.ones((652,1)).astype(int),values = X,axis = 1)


X_opt = X_new[:, [0, 1,  3, 4, 5, 6, 7, 8, 9,  11, 12, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
results_summary_AMR = regressor_OLS.summary()
print (results_summary_AMR)
