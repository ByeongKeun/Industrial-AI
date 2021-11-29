# 2. Matching
# - stitching.zip에서 각 영상셋(boat, budapest, newpaper, s1~s2)에서 두 장을 선택하고 
#   각 영상에서 각각 SIFT, SURF, ORB를 추출한 후에 매칭 및 RANSAC을 통해서 두 장의 영상간의 homography를 계산하고, 
#   이를 통해 한 장의 영상을 다른 한 장의 영상으로 warping 하는 코드를 작성하시오.

import cv2
import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.type_check import imag

#1. image load
img1 = cv2.imread('./Wed_ComputerVision/img/stitching/newspaper1.jpg', cv2.IMREAD_COLOR)
img2 = cv2.imread('./Wed_ComputerVision/img/stitching/newspaper2.jpg', cv2.IMREAD_COLOR)    #IMREAD_GRAYSCALE

#2. 각 영상에서 각각 SIFT, SURF, ORB를 추출한 후에
surf = cv2.xfeatures2d.SURF_create(10000)
surf.setExtended(True)
surf.setNOctaves(3)
surf.setNOctaveLayers(10)
surf.setUpright(False)

def SURF(img):    
    keyPoints, descriptors = surf.detectAndCompute(img, None)
    img_surf = cv2.drawKeypoints(img, keyPoints, None, (255, 0, 0),
                        cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    return img_surf

def BRIEF(img):
    keyPoints, descriptors = surf.detectAndCompute(img, None)
    brief = cv2.xfeatures2d.BriefDescriptorExtractor_create(32, True)
    keyPoints, descriptors = brief.compute(img, keyPoints)
    img_brief = cv2.drawKeypoints(img, keyPoints, None, (0, 255, 0),
                        cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    return img_brief

def SIFT(img):
    sift = cv2.xfeatures2d.SIFT_create()
    keyPoints, descriptors = sift.detectAndCompute(img,None)
    img_sift = cv2.drawKeypoints(img, keyPoints, None, (255, 0, 0),
                        cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    return img_sift

def ORB(img):    
    orb = cv2.ORB_create()
    orb.setMaxFeatures(200)

    keyPoints = orb.detect(img, None)
    keyPoints, descriptors = orb.compute(img, keyPoints)
    img_orb = cv2.drawKeypoints(img, keyPoints, None, (0, 0, 255),
                        cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    return img_orb

#mouse event
show_img = np.copy(img1)
selected_pts = []
def mouse_callback(event, x, y, flags, param):
    global selected_pts, show_img
    if event == cv2.EVENT_LBUTTONUP:
        selected_pts.append([x,y])
        cv2.circle(show_img, (x, y), 10, (0, 255, 0), 3)

def select_points(image, point_num):
    global selected_pts
    selected_pts = []
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', mouse_callback)

    while True:
        cv2.imshow('image', image)
        k = cv2.waitKey(1)
        if k == 27 or len(selected_pts) == point_num:
            break
    
    cv2.destroyAllWindows()
    return np.array(selected_pts, dtype = np.float32)

# src_pts = select_points(show_img, 3)
# dst_pts = np.array([[0,240], [0,0], [240,0]], dtype=np.float32)

# print("src_pts:", src_pts)


#match
def Match(img1, img2, type):
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    #3. 매칭 및 RANSAC을 통해서 두 장의 영상간의 homography를 계산하고,
    detector = cv2.ORB_create(100)
    kps1, fea1 = detector.detectAndCompute(img1, None)
    kps2, fea2 = detector.detectAndCompute(img2, None)
    matcher = cv2.BFMatcher_create(cv2.NORM_HAMMING, False)
    matches = matcher.match(fea1, fea2)
    
    #src, dst point
    pts1 = np.float32([kps1[m.queryIdx].pt for m in matches]).reshape(-1,1,2) #source point
    pts2 = np.float32([kps2[m.queryIdx].pt for m in matches]).reshape(-1,1,2) #destination point

    #4.  두 장의 영상간의 homography를 계산하고
    H, mask = cv2.findHomography(pts1, pts2, cv2.RANSAC, 3.0)
    dbg_img = cv2.drawMatches(img1, kps1, img2, kps2, matches, None)
    dbg_img1 = cv2.drawMatches(img1, kps1, img2, kps2, [m for i,m in enumerate(matches) if mask[i]], None)
   
    #이를 통해 한 장의 영상을 다른 한 장의 영상으로 warping
    dst = cv2.warpPerspective(dbg_img1, H,  (dbg_img.shape[1] * 2, dbg_img.shape[0] * 2))

    titles = ['image1_'+type,'image2_'+type,'All match', 'Filtered match', 'warped_img']
    images = [img1, img2, dbg_img[:,:,[2,1,0]], dbg_img1[:,:,[2,1,0]], dst]
    for i in range(5):    
        plt.subplot(3,2,i+1)
        plt.imshow(images[i],'gray')
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()

mi = input("SURF(S), BRIEF(B), ORB(O), SIFT(I): ").upper()
if mi == "S":
    img_surf1 = SURF(img1)
    img_surf2 = SURF(img2)
    Match(img_surf1, img_surf2, 'SURF')
elif mi == "I":
    img_sift1 = SIFT(img1)
    img_sift2 = SIFT(img2)
    Match(img_sift1, img_sift2, 'SIFT')
elif mi == "B":
    img_brief1 = BRIEF(img1)
    img_brief2 = BRIEF(img2)
    Match(img_brief1, img_brief2, 'BRIEF')
else:
    img_orb1 = ORB(img1)
    img_orb2 = ORB(img2)
    Match(img_orb1, img_orb2, 'ORB')
