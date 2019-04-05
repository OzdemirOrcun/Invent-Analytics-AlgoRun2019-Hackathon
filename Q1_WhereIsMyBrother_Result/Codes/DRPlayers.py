# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 19:47:50 2019

@author: Orçun
"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset

##############CHANGE FILE NAME HERE##################
dataset = pd.read_csv('DRplayers.csv') 

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




#Getting Summary of the Results
import statsmodels.formula.api as sm


X = np.append(arr = np.ones((392, 1)).astype(int), values = X, axis = 1)
X_opt = X[:, :]

regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
results_summary = regressor_OLS.summary()

results_as_html = results_summary.tables[1].as_html()
results_summary_as_dataframe = pd.read_html(results_as_html, header=0, index_col=0)[0]

#print (results_summary)


#Building the optimal model using Backward Elimination
import statsmodels.formula.api as sm
##############CHANGE DATASET SIZE HERE (375 YERINE)##################
X_new = np.append(arr = np.ones((392,1)).astype(int),values = X,axis = 1)
X_opt = X_new[:, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 21, 23, 24, 25, 28, 29, 30, 31, 32, 33, 34, 37, 38, 40, 41, 42, 43, 44, 45, 46, 48, 49, 51]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()