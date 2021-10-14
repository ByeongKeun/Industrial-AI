import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('lena.png').astype(np.float32) / 255.
img_lab = cv2.cvtColor(img, cv2.COLOR_BGR2Lab)  #COLOR_BGR2Lab: ci lab 사람의 시각과 비슷한 형식으로 변환

data = img_lab.reshape((-1, 3))

num_classes = 8 #몇개 색으로 구분할 것인지를 결정 함 --> 이부분을 키우면... orginal과 비슷해짐
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 50, 0.1)
_, labels, centers = cv2.kmeans(data, num_classes, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS) #KMEANS_RANDOM_CENTERS: 같은 num이라도 random이라 실행할때 마다 달라짐

segmented_alb = centers[labels.flatten()].reshape(img.shape)
segmented = cv2.cvtColor(segmented_alb, cv2.COLOR_Lab2RGB)

plt.subplot(121)
plt.axis('off')
plt.title('original')
plt.imshow(img[:,:,[2,1,0]])

plt.subplot(122)
plt.axis('off')
plt.title('segmented')
plt.imshow(segmented)
plt.show()
