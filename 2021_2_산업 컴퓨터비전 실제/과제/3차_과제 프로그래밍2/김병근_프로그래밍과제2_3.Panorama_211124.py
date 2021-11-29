# 3. Panorama
# - CreaterStitcher 함수를 이용하여 4개의 영상 셋에 대해서 파노라마 이미지를 만드는 방법을 구현하시오.

import cv2
import numpy as np

images = []
images.append(cv2.imread('./Wed_ComputerVision/img/stitching/boat1.jpg', cv2.IMREAD_COLOR))
images.append(cv2.imread('./Wed_ComputerVision/img/stitching/boat2.jpg', cv2.IMREAD_COLOR))
images.append(cv2.imread('./Wed_ComputerVision/img/stitching/boat3.jpg', cv2.IMREAD_COLOR))
images.append(cv2.imread('./Wed_ComputerVision/img/stitching/boat4.jpg', cv2.IMREAD_COLOR))
images.append(cv2.imread('./Wed_ComputerVision/img/stitching/boat5.jpg', cv2.IMREAD_COLOR))
images.append(cv2.imread('./Wed_ComputerVision/img/stitching/boat6.jpg', cv2.IMREAD_COLOR))

stitcher = cv2.createStitcher()
ret, pano = stitcher.stitch(images)

if ret == cv2.STITCHER_OK:
    pano = cv2.resize(pano, dsize=(0,0), fx=0.2, fy=0.2)
    cv2.imshow('panorama', pano)
    cv2.waitKey()

    cv2.destroyAllWindows()
else:
    print('error during stiching')