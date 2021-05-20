#Iteration : 상호작용
from sklearn.datasets import fetch_openml
from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt
import numpy as np
import time

start = time.time()

# MNIST 데이터셋을 읽고 훈련 집합과 테스트 집합으로 분할
# scykit learn에서 손글시 데이터셋을 받아 mnist 변수에 저장하고
mnist=fetch_openml('mnist_784') #shape (70000, 784)
mnist.data=mnist.data/255.0 #데이터 전처리 (RGB=255,255,255)를 255로 나눠, 0 or 1로 바꾸는 데이터 정규화

#feature: train과 test로 분할 X_train(0~6만장), X_test(6만~7만장)
x_train=mnist.data[:60000]; x_test=mnist.data[60000:]
#target: train과 test를 Y_train(0~6만장), Y_test(6만~7만)
y_train=np.int16(mnist.target[:60000]); y_test=np.int16(mnist.target[60000:])

# MLP 분류기 모델을 학습(multi layer perceptron)
mlp=MLPClassifier(hidden_layer_sizes=(50), #100개의 뉴런을 1개 은닉층으로 설정
                  learning_rate_init=0.001, #학습률, 단계별로 움직이는 학습 속도
                  batch_size=128,   #한번에 처리할 batch size
                  max_iter=300, #최대 반복 횟수
                  solver='adam',    #가중치 최적화를 위해 사용하는 함수 = adam = trainning시간 및 평가에 유리한 알고리즘
                  verbose=True)
mlp.fit(x_train,y_train)    #학습 실행

# 테스트 집합으로 예측
res=mlp.predict(x_test) #학습 결과를 x_test dataset으로 예측

# 혼동 행렬
conf=np.zeros((10,10),dtype=np.int16)   #0의 array생성 (shape = 10*10행렬, dtype = int16, order=default)
for i in range(len(res)):   
    conf[res[i]][y_test[i]]+=1  #예측결과와 target인 y_test데이터의 혼동 행렬 구성
print(conf)

# 정확률 계산
no_correct=0
for i in range(10):
    no_correct+=conf[i][i]  #혼동 행렬에서 행/렬이 같은 index인 값의 합계
accuracy=no_correct/len(res)    # 정확도 계산: 전체 데이터 vs 혼동 행렬의 정답값
print("테스트 집합에 대한 정확률은", accuracy*100, "%입니다.")
print("수행시간: {0}초".format(str(time.time() - start)))

#혼동 행열을, graph로 표현
import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(10,7))
sns.set(font_scale=2)
sns.heatmap(conf, annot=True)   #heatmap graph