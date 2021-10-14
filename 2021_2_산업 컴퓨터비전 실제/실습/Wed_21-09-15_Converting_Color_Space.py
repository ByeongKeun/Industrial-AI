import cv2
import numpy as np
from numpy.lib.type_check import imag

image = cv2.imread('Lena.png').astype(np.float32) / 255
print("shape: ", image.shape)
print("Data type: ", image.dtype)
cv2.imshow("Original image", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print('Converted to grayscale')
print('shape: ', gray.shape)
print('Data type: ', gray.dtype)
cv2.imshow('gray-scale image', gray)

hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
print('Converted to HSV')
print('shape: ', hsv.shape)
print('Data type: ', hsv.dtype)
#cv2.imshow('gray-scale image', gray)

hsv[:,:,2] *= 2
from_hsv = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
print('Converted back to RGB from HSV')
print('shape: ', from_hsv.shape)
print('Data type: ', from_hsv.dtype)
cv2.imshow('from_hsv', from_hsv)
cv2.waitKey()
cv2.destroyAllWindows()
