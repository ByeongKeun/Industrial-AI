from typing import ChainMap
import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('./Lena.png', 0)

dx = cv2.Sobel(image, cv2.CV_32F, 1, 0)
dy = cv2.Sobel(image, cv2.CV_32F, 0, 1)

#grad = 

plt.figure(figsize=(8,3))
plt.subplot(131)
plt.axis('off')
plt.title('image')
plt.imshow(image, cmap='gray')

plt.subplot(132)
plt.axis('off')
plt.imshow(dx, cmap='gray')

plt.title(r'$frac{dI}{dx}$')
plt.subplot(133)
plt.axis('off')
plt.title(r'$frac{dI}{dx}$')
plt.imshow(dy, cmap='gray')

# plt.subplot(134)
# plt.axis('off')
# plt.title(r'$frac{dI}{dx}$'+\frac{})
# plt.imshow(dy, cmap='gray')

plt.tight_layout()
plt.show()