import cv2
import numpy as np
import matplotlib.pyplot as plt

#image load
img = cv2.imread("Lena.png", cv2.IMREAD_COLOR)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))

#Dilation(팽창)
def imageDilation(image, kernel, iterations = 1):
    return cv2.dilate(image, kernel=kernel, iterations=iterations)
    
#Erosion(침식)
def imageErosion(image, kernel, iterations = 1):
    return cv2.erode(image, kernel=kernel, iterations=iterations)

#Opening
def imageOpening(image, iterations = 1):
    kernel = np.ones((3, 3), np.uint8)
    erosion = imageErosion(image, kernel, iterations)
    return imageDilation(erosion, kernel, iterations)
    
#Closing
def imageClosing(image, iterations = 1):
    kernel = np.ones((3, 3), np.uint8)
    dilation = imageDilation(image, kernel, iterations)
    return imageErosion(dilation, kernel, iterations)

#
choise = input("D(dilation), E(erosion), O(open), C(close):").upper()
choiseNo = np.int(input("횟수입력: "))

imgCopy = img.copy()

for i in range(choiseNo):
    if choise == "D":
        imgCopy = imageDilation(imgCopy, kernel)
    elif choise == "E":
        imgCopy = imageErosion(imgCopy, kernel)
    elif choise == "O":
        imgCopy = imageOpening(imgCopy)
    elif choise == "C":
        imgCopy = imageClosing(imgCopy)

cv2.imshow("result", imgCopy)
cv2.waitKey()
cv2.destroyAllWindows()

# 전체 표시 캡쳐
# dilation = imageDilation(img, kernel)
# erosion = imageErosion(img, kernel)
# open = imageOpening(img)
# close = imageClosing(img)

# plt.figure()
# plt.subplot(221)
# plt.axis('off')
# plt.title('Dilation')
# plt.imshow(dilation)

# plt.subplot(222)
# plt.axis('off')
# plt.title('Erosion(침식)')
# plt.imshow(erosion)

# plt.subplot(223)
# plt.axis('off')
# plt.title('open')
# plt.imshow(open)

# plt.subplot(224)
# plt.axis('off')
# plt.title('close')
# plt.imshow(close, cmap='gray')

# plt.tight_layout()
# plt.show()