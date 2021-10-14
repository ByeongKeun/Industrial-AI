import cv2
import numpy as np
import matplotlib.pyplot as plt

#image load
img = cv2.imread("Lena.png", cv2.IMREAD_COLOR)
#평탄화 후, image
imgEq = img.copy()
#b/g/r로 chennel 분할
b, g, r = cv2.split(img)

#사용자 입력
inColor = input("r/g/b 중 입력하시오")
#평탄화 처리
eq = cv2.equalizeHist(b)

if inColor == "b":    
    imgEq = cv2.merge((eq, g, r))
elif inColor == "g":
    eq = cv2.equalizeHist(g)
    imgEq = cv2.merge((r, eq, r))
elif inColor == "r":
    eq = cv2.equalizeHist(r)
    imgEq = cv2.merge((b, g, eq))

#histogram 표시
hist, bins = np.histogram(eq, 256, [0, 255])
plt.fill(hist)
plt.xlabel('histogram')
plt.show()

#orignal image와 chennel 평탄화후 merge 이미지
cv2.imshow("orginal image", img)
cv2.imshow("equalize color=" + inColor, imgEq)
cv2.waitKey()
cv2.destroyAllWindows()