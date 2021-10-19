import cv2 
import numpy as np
from matplotlib import pyplot as plt

imgOrg = cv2.imread('stain2.jpg')
img = cv2.imread('stain2.jpg',0)

#----- cv2.threshold(src, threshold_value, value, flag)
# src: 입력 영상(grayscale)
# threshold_value: 픽셀 문턱값
# value: 픽셀 threshold값보다 커질때 적용되는 최대값
# flag: threshold 적용 스타일
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

# ---- cv2.Sobel(src, ddepth, dx, dy, dst, ksize, scale, delta, borderType) -----
# src: 입력 영상
# ddepth: 출력 영상의 dtype (-1: 입력 영상과 동일)
# dx, dy: 미분 차수 (0, 1, 2 중 선택, 둘 다 0일 수는 없음)
# ksize: 커널의 크기 (1, 3, 5, 7 중 선택)
# scale: 미분에 사용할 계수
# delta: 연산 결과에 가산할 값

# dx, dy: 0/1/2 중 실습 시 배운 미분차수가 가장 좋음
thresh6 = cv2.Sobel(img, cv2.CV_32F, 1, 0)  #dx/dy(미분차수) = 1 / 0 
thresh7 = cv2.Sobel(img, cv2.CV_32F, 0, 1)  #dx/dy(미분차수) = 0 / 1


titles = ['Original', 'Original(Gray)','T_BINARY','T_BINARY_INV','T_TRUNC',
          'T_TOZERO','T_TOZERO_INV', 'SOBEL_1_0', 'SOBEL_0_1']
images = [imgOrg, img, thresh1, thresh2, thresh3, thresh4, thresh5, thresh6, thresh7]
for i in range(9):
    plt.subplot(3,3,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()