# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 11:18:44 2021
    배치: 느린 I/O를 통해서 데이터를 읽는 횟수를 줄이기 위해, 묶음(Batch)로 데이터를 입력 받아 학습 시킴
    미니배치: 전체 학습 데이터의  n등분 하여 학습 데이터를 Batch(묶음) 하는 방식으로 학습
    에폭(Epoch): 인공 신경망에서 전체 데이터 셋에 대해 한 번 학습을 완료한 상태를 의미
    1 epoch(모든 데이터 셋을 1번 학습) = 10(batch_size) * 100(iteration or step)
    1 iteratio: 1회 학습

@author: BK
"""

import sys, os
sys.path.append(os.pardir)  # 부모 디렉터리

import numpy as np
from dataset.mnist import load_mnist
from two_layer_net import TwoLayerNet
import matplotlib.pyplot as plt
import time

start = time.time()
h_size = 50 #hidden size를 print하기 위해 별도 변수 선언

# 데이터 읽기
(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

network = TwoLayerNet(input_size=784, hidden_size=h_size, output_size=10)

#하이퍼 파라미터
iters_num = 100   #반복 횟수 설정
train_size = x_train.shape[0]
batch_size = 50    #미니배치 크기
learning_rate = 0.1

train_loss_list = []
train_acc_list = []
test_acc_list = []

iter_per_epoch = max(train_size / batch_size, 1)
j = 1

for i in range(iters_num):
    #미니배치 획득
    batch_mask = np.random.choice(train_size, batch_size)
    x_batch = x_train[batch_mask]
    t_batch = t_train[batch_mask]
    
    # 기울기 계산
    #grad = network.numerical_gradient(x_batch, t_batch) # 수치 미분 방식
    grad = network.gradient(x_batch, t_batch) # 성능 개선판, 오차역전파법 방식(훨씬 빠르다)
    
    # 매개변수 갱신
    for key in ('W1', 'b1', 'W2', 'b2'):
        network.params[key] -= learning_rate * grad[key]
    
    #학습 경과 기록
    loss = network.loss(x_batch, t_batch)
    train_loss_list.append(loss)
    
    #1에폭당 정확도 계산
    if i % iter_per_epoch == 0:
        train_acc = network.accuracy(x_train, t_train)
        test_acc = network.accuracy(x_test, t_test)
        train_acc_list.append(train_acc)
        test_acc_list.append(test_acc)
        print("train acc | test acc| → |{0} | {1}|".format(str(train_acc),  str(test_acc)))
        j += 1
    

print("수행시간: {0}초 | Epoch 횟수: {1}회".format(str(time.time() - start), str(j)))
print("batch size: {0} | hidden size: {1}".format(str(batch_size), str(h_size)))

#그래프 - matplotlib
x = np.arange(len(train_acc_list))
# plt.figure(figsize=(20,8))
plt.plot(x, train_acc_list, label='train accuracy', linestyle='solid')
plt.plot(x, test_acc_list, label='test accuracy', linestyle='--')
plt.xlabel("epochs")    #학습 횟수
plt.ylabel("accuracy")  #정확도
plt.ylim(0, 1.0)
plt.legend(loc='lower right')
plt.show()

# plt.figure(figsize=(20,8))
# plt.plot(train_loss_list[:1000], linewidth=0.5)
# plt.title('Train Loss Graph')
# plt.xlabel('iteration')
# plt.ylabel('loss')
# plt.show()