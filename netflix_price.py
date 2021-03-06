# -*- coding: utf-8 -*-
"""Netflix_Price.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x8CbhrAvh_HtBytRpm8OhKVoEv2BOelm
"""

import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
plt.style.use('bmh')

from google.colab import files
uplooaded = files.upload()

df = pd.read_csv('NFLX.csv')
df.head(10)

df.shape

plt.figure(figsize=(16,8))
plt.title('NetFlix')
plt.xlabel('Days')
plt.ylabel('Close Price USD ($)')
plt.plot(df['Close'])
plt.show()

df = df[['Close']]
df.head(4)

future_days = 25
df['Prediction'] = df[['Close']].shift(-future_days)
df.tail(4)

X = np.array(df.drop(['Prediction'], 1))[:-future_days]
print(X)

y = np.array(df['Prediction'])[:-future_days]
print(y)

x_train, x_test, y_train, y_test = train_test_split(X,y,test_size = 0.25)

tree = DecisionTreeRegressor().fit(x_train, y_train)
lr = LinearRegression().fit(x_train,y_train)

x_future = df.drop(['Prediction'], 1)[:-future_days]
x_future = x_future.tail(future_days)
x_future = np.array(x_future)
x_future

tree_prediction = tree.predict(x_future)
print(tree_prediction)
print()

lr_prediction = lr.predict(x_future)
print(lr_prediction)

predictions = tree_prediction

valid = df[X.shape[0]:]
valid['Predictions'] = predictions
plt.figure(figsize=(16,8))
plt.title('Model')
plt.xlabel('Days')
plt.ylabel('Close Price USD $')
plt.plot(df['Close'])
plt.plot(valid[['Close' , 'Predictions']])
plt.legend(['Orig', 'val', 'Pred'])
plt.show()



