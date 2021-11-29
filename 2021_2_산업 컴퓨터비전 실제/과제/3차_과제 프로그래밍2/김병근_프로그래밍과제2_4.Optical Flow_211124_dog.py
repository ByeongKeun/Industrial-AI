# 4. Optical Flow
# - dog 영상을 이용해서 Good Feature to Tracking을 추출하고 Pyramid Lucas-Kanade 알고리즘을 적용해서 Optical Flow를 구하는 코드를 작성하시오.
# - dog 영상을 이용해서 Farneback과 DualTVL1 Optical Flow 알고리즘을 구하는 코드를 작성하시오.
import cv2
import numpy as np
import matplotlib.pyplot as plt

imgDog1 = cv2.imread('./Wed_ComputerVision/img/stitching/dog_b.jpg', cv2.IMREAD_COLOR)
imgDog2 = cv2.imread('./Wed_ComputerVision/img/stitching/dog_a.jpg', cv2.IMREAD_COLOR)

frame = np.copy(imgDog1)    #video를 frame 형태로 1장씩
gray_frame = cv2.cvtColor(imgDog1, cv2.COLOR_BGR2GRAY)    #bgr -> gray
prev_gray_frame = cv2.cvtColor(imgDog2, cv2.COLOR_BGR2GRAY)

pts = cv2.goodFeaturesToTrack(gray_frame, 500, 0.05, 10)
pts = pts.reshape(-1, 1, 2)

#피라미드 루카스 카나데 algorithm
#dog 영상을 이용해서 Good Feature to Tracking을 추출하고 Pyramid Lucas-Kanade 알고리즘을 적용해서 Optical Flow를 구하는 코드를 작성하시오.
pts, status, erros = cv2.calcOpticalFlowPyrLK(prev_gray_frame, gray_frame, pts, None, 
                                winSize=(15,15), maxLevel=5, criteria=(cv2.TERM_CRITERIA_EPS | cv2.cv2.TERM_CRITERIA_COUNT, 10, 0.03))
good_pts = pts[status == 1]

tracks = good_pts
tracks = np.vstack((tracks, good_pts))
for p in tracks:
    cv2.circle(frame, (p[0], p[1]), 3, (0, 255, 0), -1)

titles = ['imgDog1', 'imgDog2', 'frame']
images = [imgDog2, imgDog1, frame]
for i in range(3):
    plt.subplot(1,3,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.tight_layout()
plt.show()

#diplay function
def display_flow(img, flow, stride=40):
    for index in np.ndindex(flow[::stride, ::stride].shape[:2]):    #40개 stride 마다 화살표
        pt1 = tuple(i*stride for i in index)
        delta = flow[pt1].astype(np.int32)[::-1]
        pt2 = tuple(pt1 + 10*delta) #10==

        if 2 <= cv2.norm(delta) <= 10:
            cv2.arrowedLine(img, pt1[::-1], pt2[::-1], (0,0,255), 5, cv2.LINE_AA, 0, 0.4)

    norm_opt_flow = np.linalg.norm(flow, axis=2)
    norm_opt_flow = cv2.normalize(norm_opt_flow, None, 0, 1, cv2.NORM_MINMAX)

    cv2.imshow('optical flow',img)
    cv2.imshow('optical flow magnitude', norm_opt_flow)

    k = cv2.waitKey(1)

    if k == 27: return 1
    else: return 0

#2-1. dog 영상을 이용해서 Farneback 알고리즘을 구하는 코드를 작성하시오.
frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
gray_frame = cv2.resize(frame, (0,0), None, 0.5, 0.5)   
prev_gray_frame = cv2.resize(prev_gray_frame, (0,0), None, 0.5, 0.5)

opt_flow = cv2.calcOpticalFlowFarneback(prev_gray_frame, gray_frame, None, 0.5, 5, 13, 10, 5, 1.1, cv2.OPTFLOW_USE_INITIAL_FLOW)
opt_flow = cv2.calcOpticalFlowFarneback(prev_gray_frame, gray_frame, opt_flow, 0.5, 5, 13,10, 5, 1.1, cv2.OPTFLOW_USE_INITIAL_FLOW)

display_flow(frame, opt_flow)
cv2.waitKey()
cv2.destroyAllWindows()

#2-2. dog 영상을 이용해서 DualTVL1 Optical Flow 알고리즘을 구하는 코드를 작성하시오.
flow_DualTVL1 = cv2.createOptFlow_DualTVL1()
opt_flow = flow_DualTVL1.calc(prev_gray_frame, gray_frame, None)
flow_DualTVL1.setUseInitialFlow(True)
opt_flow = flow_DualTVL1.calc(prev_gray_frame, gray_frame, opt_flow)

display_flow(frame, opt_flow)
cv2.waitKey()
cv2.destroyAllWindows()