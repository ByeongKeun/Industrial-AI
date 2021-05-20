from sklearn import datasets
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
import numpy as np
import time

start = time.time()

# 데이터셋을 읽고 훈련 집합과 테스트 집합으로 분할
#손글씨로 쓴 숫자를 분류하는 데이터 셋을 sklearn.datasets에서 받아옴
digit=datasets.load_digits()
 #손글씨 데이터 셋을 X(feature)와 Y(target)으로 나누고, train과 test 데이터를 6:4로 나눠서 변수에 저장
x_train,x_test,y_train,y_test=train_test_split(digit.data,digit.target,train_size=0.6)

# MLP 분류기 모델을 학습
#다층퍼셉트론 객체를 생성하는데,
#은닉층 SIZE를 
mlp=MLPClassifier(hidden_layer_sizes=(100),learning_rate_init=0.001,batch_size=32,max_iter=300,solver='sgd',verbose=True)
mlp.fit(x_train,y_train)

res=mlp.predict(x_test) # 테스트 집합으로 예측

# 혼동 행렬
conf=np.zeros((10,10))
for i in range(len(res)):
    conf[res[i]][y_test[i]]+=1
print(conf)

# 정확률 계산
no_correct=0
for i in range(10):
    no_correct+=conf[i][i]
accuracy=no_correct/len(res)
print("테스트 집합에 대한 정확률은 ", accuracy*100, "%입니다.")
print("수행시간: {0}초".format(str(time.time() - start)))

import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(10,7))
sns.set(font_scale=2)
sns.heatmap(conf, annot=True)