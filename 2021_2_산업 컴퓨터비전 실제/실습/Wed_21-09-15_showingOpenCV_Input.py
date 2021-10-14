import argparse
import cv2
import numpy as np
import random

parser = argparse.ArgumentParser()
parser.add_argument('--path', default='Lena.png', help='Image path.')
parser.add_argument('--iter', default=50, help='Dwonsampling-upsampling iterations number.')
params = parser.parse_args()

orig = cv2.imread(params.path)
orig_size = orig.shape[0:2]

image_to_show = np.copy(orig)

w, h = orig.shape[1], orig.shape[0]

cv2.imshow("original image", orig)
#cv2.waitKey(2000)

print("w, h=", w, ",", h)

def rand_pt(mult=1.):
    return (random.randrange(int(w*mult)),
    random.randrange(int(h*mult)))

mouse_pressed = False
s_x = s_y = e_x = e_y = -1

mode = 0

def mouse_callback(event, x, y, flags, param):
    global image_to_show, s_x, s_y, e_x, e_y, mouse_pressed

    if event == cv2.EVENT_LBUTTONDOWN:
        mouse_pressed = True
        s_x, s_y = x, y
        e_x, e_y = x, y
        image_to_show= np.copy(orig)

    elif event == cv2.EVENT_MOUSEMOVE:
        if mouse_pressed:
            image_to_show = np.copy(orig)
            if mode == 0:
                cv2.rectangle(image_to_show, (s_x, s_y), (x, y), (0, 255, 0), 1)
            elif mode == 1:
                cv2.line(image_to_show, (s_x, s_y), (x, y), (0, 255, 0), 2, cv2.LINE_AA)
            elif mode == 2:
                cv2.arrowedLine(image_to_show, (s_x, s_y), (x, y), (0, 0, 255), 3, cv2.LINE_AA)                

    elif event == cv2.cv2.EVENT_LBUTTONUP:
        mouse_pressed = False
        e_x, e_y = x, y

cv2.namedWindow('image')
cv2.setMouseCallback('image', mouse_callback)


finish = False
while not finish:
    
    cv2.imshow('image', image_to_show)
    key = cv2.waitKey(1)
    
    if key == ord('r'): #rectangle
        mode = 0
        print("key=r")
        #cv2.rectangle(image_to_show, rand_pt(), rand_pt(), (255, 255, 0), 1)
        #cv2.imshow("result, key=r", image_to_show)
    elif key == ord('i'):   #line
        mode = 1
        print("key=i")
        #cv2.line(image_to_show, rand_pt(), rand_pt(), (0, 255, 0))
        #cv2.line(image_to_show, rand_pt(), rand_pt(), (0, 255, 0), 3, cv2.LINE_AA)
        #cv2.imshow("result, key=i", image_to_show)
    elif key == ord('a'):   #arrow
        mode = 2
        print("key=a")
        #cv2.arrowedLine(image_to_show, rand_pt(), rand_pt(), (0, 0, 255), 3, cv2.LINE_AA)
        #cv2.imshow("result, key=a", image_to_show)
    elif key == ord('c'):   #origin
        print("key=c")
        image_to_show = np.copy(orig)
    elif key == ord('w'):   #save
        print("key=w")
        save_img = np.copy(orig)        
        cv2.imwrite('Lena_compressed.png', save_img, [cv2.IMWRITE_PNG_COMPRESSION, 0])        
    elif key == 27:
        print("key=esc")
        finish = True

cv2.destroyAllWindows()