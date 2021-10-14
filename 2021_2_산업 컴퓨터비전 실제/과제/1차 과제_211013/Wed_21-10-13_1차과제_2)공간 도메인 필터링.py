#양방향 필터(bilateralFilter)
#엣지가 아닌 부분에 대한 blur처리 함
import cv2
import numpy as np
import matplotlib.pyplot as plt

#image load
img = cv2.imread("Lena.png").astype(np.float32) / 255

#noise 생성
noised = (img + 0.2 * np.random.rand(*img.shape).astype(np.float32))
noised = noised.clip(0, 1)

#사용자로 부터 값 입력
d = np.int(input("입력하시오: Diameter(int):"))
sc, ss = np.double(input("입력하시오: Sigma Color(double), Sigma Space(double):").split())

# bilateralFilter (src, d, sigmaColor, sigmaSpace ...)
# 1: src 입력영상
# 2: (int) diameter 필터링에 사용될 이웃 픽셀의 거리(지름), -1인 경우 sigmaSpace값
# 3: (doulbe) sigma color 색 공간에서 필터의 표준편차, 클수록 이웃한 픽셀과 기준색상에 영향이 커짐
# 4: (double) sigram space 좌표공간에서 필터의 표준편차, 값이 클수록 긴밀하게 주변픽셀에 영향을 미침. 클수록 속도도 느려짐
bilat = cv2.bilateralFilter(noised, d, sc, ss)

# cv2.imshow("original", img)
# cv2.imshow("noised", noised)
cv2.imshow("bilateralFilter", bilat)
cv2.waitKey()
cv2.destroyAllWindows()