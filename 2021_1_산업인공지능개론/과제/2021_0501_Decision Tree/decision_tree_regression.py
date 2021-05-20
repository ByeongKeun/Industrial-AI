# -*- coding: utf-8 -*-
"""
Created on Thu May  6 10:00:21 2021

@author: BK
"""

import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

f = pd.read_excel('carrierloading_down_event.xlsx', 0)
#print(eventsfile)

eventsfile = f #f.fillna(0)    #혹시나 있을지 모르는 nan값 치환(결측치)

data_train = eventsfile[eventsfile['PREV_TRANS_TIME'] < 6080000] #5월 1일~ 6일 08시
data_test = eventsfile[eventsfile['PREV_TRANS_TIME'] >= 6080000] #5월 6일 08시 이후

# print(data_train['PREV_TRANS_TIME'].dtypes)
# print(data_train['DOWN_TIME'].dtypes)


# print(data_train['PREV_TRANS_TIME'].shape)
# print(data_train['PREV_TRANS_TIME'][:, np.newaxis].shape)

# print(data_train['PREV_TRANS_TIME'])
# print("---------------------------------------")
# print(data_train['PREV_TRANS_TIME'][:, np.newaxis])

x_train = data_train['PREV_TRANS_TIME'][:, np.newaxis] # train data를 1열로 생성
y_train = data_train['DOWN_TIME']

tree = DecisionTreeRegressor()
tree.fit(x_train, y_train)

x_all = eventsfile['PREV_TRANS_TIME'].values.reshape(-1, 1) # fit을 하기위해, 1열로 만듬
pred_tree = tree.predict(x_all)

# plt.scatter(eventsfile['PREV_TRANS_TIME'], data_train['DOWN_TIME'], c= 'lightblue', label = 'train data')
# plt.scatter(eventsfile['PREV_TRANS_TIME'], data_test['DOWN_TIME'], c= 'blue', label = 'test data')
# # plt.plot(data_test['PREV_TRANS_TIME'], data_test['DOWN_TIME'], color='blue', label = 'test data')
# plt.plot(data_train['PREV_TRANS_TIME'], pred_tree, color='red', label = 'predict data')

plt.scatter(eventsfile['PREV_TRANS_TIME'], pred_tree, c= 'lightblue', label = 'predict')
plt.plot(data_train['PREV_TRANS_TIME'], data_train['DOWN_TIME'], color='red', label = 'train data')
plt.plot(data_test['PREV_TRANS_TIME'], data_test['DOWN_TIME'], color='blue', label = 'test data')

plt.xlabel('time', size=10)
plt.ylabel('down time', size=10)
plt.legend(loc='upper right')
plt.show()

# print(data_train['DOWN_TIME'])
# print(pred_tree)