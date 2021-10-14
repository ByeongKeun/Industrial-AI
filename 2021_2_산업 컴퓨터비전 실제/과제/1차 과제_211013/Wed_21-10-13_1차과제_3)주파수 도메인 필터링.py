import cv2
import numpy as np
import matplotlib.pyplot as plt

#image load
image = cv2.imread('./Lena.png', 0).astype(np.float32) / 255

#1. 사용자로부터 반지름 입력받아, image에 원을 그리고
radius = np.int(input("반지름을 입력하시오:")) #25
red = (0, 0, 255)
center = image.shape[0]//2
radImg = cv2.circle(image, (center, center), radius, red, 5)
# cv2.imshow("원그리기", radImg)
# cv2.waitKey()
# cv2.destroyAllWindows()

#2. DFT를 통해서 영상을 주파수 도메인으로 바꿔서 출력한 후에
fft = cv2.dft(radImg, flags = cv2.DFT_COMPLEX_OUTPUT)
fft_shift = np.fft.fftshift(fft, axes=[0,1])    #주파수가 0인부분을 정중앙에 위치시키고 재배열 함
sz = 25

#3. fft * 입력받은 반지름
fft = fft * radius

#fft(512, 512, 2) shape만큼의 mask array(0) 생성
mask = np.zeros(fft.shape, np.uint8)
mask[image.shape[0]//2-sz:image.shape[0]//2+sz,
    image.shape[1]//2-sz:image.shape[1]//2+sz, 
    :] = 1

#4. 사용자료 부터 Hig or Low 주파수 입력
frequancy = input("H(high) or L(low)").upper()

if frequancy == "H":
    fft_shift *= 1 - mask #high 프리퀀시
    frequancy = "High"
elif frequancy == "L":  
    fft_shift *= mask   #low 프리퀀시
    frequancy = "Low"

fft = np.fft.ifftshift(fft_shift, axes=[0,1])   #주파수가 0인부분을 정중앙에 위치시키고 재배열 함
filtered = cv2.idft(fft, flags=cv2.DFT_SCALE | cv2.DFT_REAL_OUTPUT)
mask_new = np.dstack((mask, np.zeros((image.shape[0], image.shape[1]), dtype=np.uint8)))

image = cv2.imread('./Lena.png', 0).astype(np.float32) / 255

#5. image show
plt.figure()
plt.subplot(131)
plt.axis('off')
plt.title('original')
plt.imshow(image, cmap='gray')

plt.subplot(132)
plt.axis('off')
plt.title('circle')
plt.imshow(radImg, cmap='gray')

plt.subplot(133)
plt.axis('off')
plt.title(frequancy + ' frequencies')
plt.imshow(filtered, cmap='gray')

plt.tight_layout()
plt.show()