# 1. Feature Detection
# - stitching.zip에서 4장의 영상(boat1, budapest1, newpaper1, s1)을 선택한 후에 Canny Edge와 Harris Corner를 검출해서 결과를 출력하는 코드를 작성하시오.

import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

print(os.getcwd())
img1 = cv2.imread('./Wed_ComputerVision/img/stitching/boat1.jpg', cv2.IMREAD_COLOR)
img2 = cv2.imread('./Wed_ComputerVision/img/stitching/budapest1.jpg', cv2.IMREAD_COLOR)
img3 = cv2.imread('./Wed_ComputerVision/img/stitching/newspaper1.jpg', cv2.IMREAD_COLOR)
img4 = cv2.imread('./Wed_ComputerVision/img/stitching/s1.jpg', cv2.IMREAD_COLOR)

# cv2.imshow("img3", img3)
# img3 = cv2.resize(img31, dsize=(0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
# img3 = cv2.resize(img3, (0,0), fx=0.5, fy=0.5) 

def cornerHarris(img):
    corners = cv2.cornerHarris(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 2, 3, 0.04)
    corners = cv2.dilate(corners, None)

    show_img = np.copy(img)
    show_img[corners>0.1*corners.max()]-[0, 0, 255]

    corners = cv2.normalize(corners, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
    show_img = np.hstack((show_img, cv2.cvtColor(corners, cv2.COLOR_GRAY2BGR)))

    return show_img

def CannyEdge(img):
    edges = cv2.Canny(img,100,200)

    return edges

show_img1 = cornerHarris(img1)
show_img2 = cornerHarris(img2)
show_img3 = cornerHarris(img3)
show_img4 = cornerHarris(img4)

show_img11 = CannyEdge(img1)
show_img21 = CannyEdge(img2)
show_img31 = CannyEdge(img3)
show_img41 = CannyEdge(img4)

titles = ['harris_boat1', 'harris_budapest1','harris_newpaper1','harris_s1', 
            'canny_boat1', 'canny_budapest1','canny_newpaper1','canny_s1']
images = [show_img1, show_img2, show_img3, show_img4, show_img11, show_img21, show_img31, show_img41]
for i in range(8):    
    plt.subplot(4,4,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()

# if cv2.waitKey(0) == 27:
#     cv2.destroyAllWindows()