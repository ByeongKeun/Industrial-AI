import cv2
import numpy as np
import matplotlib.pyplot as plt

circle_image = np.zeros((500, 500), np.uint8)
cv2.circle(circle_image, (250, 250), 100, 255, -1)

rect_image = np.zeros((500, 500), np.uint8)
cv2.rectangle(rect_image, (100, 100), (400,250), 255, -1)

circle_and_rect_image = circle_image & rect_image
circle_or_rect_image = circle_image | rect_image

plt.figure(figsize=(10,10))

plt.subplot(221)
plt.axis('off')
plt.title('cicle')
plt.imshow(circle_image, cmap='gray')

plt.subplot(222)
plt.axis('off')
plt.title('rectangle')
plt.imshow(rect_image, cmap='gray')

plt.subplot(223)
plt.axis('off')
plt.title('cicle & rectangle')
plt.imshow(circle_and_rect_image, cmap='gray')

plt.subplot(224)
plt.axis('off')
plt.title('cicle | rectangle')
plt.imshow(circle_or_rect_image, cmap='gray')

plt.tight_layout(True)
plt.show()