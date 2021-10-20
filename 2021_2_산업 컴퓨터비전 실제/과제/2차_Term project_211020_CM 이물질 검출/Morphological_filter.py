import cv2
import numpy as np

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
