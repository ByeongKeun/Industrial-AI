import cv2 
import numpy as np
from matplotlib import pyplot as plt
import Morphological_filter as mo

imgOrg = cv2.imread('stain2.jpg')
img = cv2.imread('stain2.jpg',0)

for sigma in range(1, 4):
    img = cv2.GaussianBlur(img, (0, 0), sigma)

choiseNo = np.int(input("횟수입력: "))
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))

imgCopyD = img.copy()
imgCopyE = img.copy()
imgCopyO = img.copy()
imgCopyC = img.copy()

#D(dilation), E(erosion), O(open), C(close)
for i in range(choiseNo):
    imgCopyD = mo.imageDilation(imgCopyD, kernel)
    imgCopyE = mo.imageErosion(imgCopyE, kernel)
    imgCopyO = mo.imageOpening(imgCopyO)
    imgCopyC = mo.imageClosing(imgCopyC)

# ---- cv2.Sobel(src, ddepth, dx, dy, dst, ksize, scale, delta, borderType) -----
# src: 입력 영상,               # ddepth: 출력 영상의 dtype (-1: 입력 영상과 동일)
# dx, dy: 미분 차수 (0, 1, 2 중 선택, 둘 다 0일 수는 없음)
# ksize: 커널의 크기 (1, 3, 5, 7 중 선택)   # scale: 미분에 사용할 계수
# delta: 연산 결과에 가산할 값
# dx, dy: 0/1/2 중 실습 시 배운 미분차수가 가장 좋음
sobelD1 = cv2.Sobel(imgCopyD, cv2.CV_32F, 1, 0)  #dx/dy(미분차수) = 1 / 0 
sobelD2 = cv2.Sobel(imgCopyD, cv2.CV_32F, 0, 1)  #dx/dy(미분차수) = 0 / 1
sobelE1 = cv2.Sobel(imgCopyE, cv2.CV_32F, 1, 0)  
sobelE2 = cv2.Sobel(imgCopyE, cv2.CV_32F, 0, 1)  
sobelO1 = cv2.Sobel(imgCopyO, cv2.CV_32F, 1, 0)  
sobelO2 = cv2.Sobel(imgCopyO, cv2.CV_32F, 0, 1)  
sobelC1 = cv2.Sobel(imgCopyC, cv2.CV_32F, 1, 0)  
sobelC2 = cv2.Sobel(imgCopyC, cv2.CV_32F, 0, 1)  
sobelT1 = cv2.Sobel(imgCopyC, -1, 0, 1, kernel)
sobelT2 = cv2.Sobel(imgCopyC, -1, 1, 0, kernel)

#D(dilation), E(erosion), O(open), C(close)
titles = ['img(Org)', 'img(Gray)','sobel(dilation)1','sobel(dilation)2',
          'sobel(erosion)1','sobel(erosion)2', 'sobel(open)1', 'sobel(open)2', 'sobel(close)1', 'sobel(close)2',
          'sobelT1', 'sobelT2']
images = [imgOrg, img, sobelD1, sobelD1, sobelE1, sobelE2, sobelO1, sobelO2, sobelC1, sobelC2, sobelT1, sobelT2]
for i in range(12):
    plt.subplot(4,3,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()