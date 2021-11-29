import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

#1. 엣지(특징점)추출: Harris corner -------------------------------------------------------------------
# 이미지 위에 커널을 이동시키면서 그레디언트의 변화량을 구하고, 이 값을 적절한 기준값으로 구별하여 코너점을 찾는다.
def cornerHarris(img):
    corners = cv2.cornerHarris(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 2, 3, 0.04)
    corners = cv2.dilate(corners, None)

    show_img = np.copy(img)
    show_img[corners>0.1*corners.max()] = [0, 0, 255]

    # corners = cv2.normalize(corners, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
    # show_img = np.hstack((show_img, cv2.cvtColor(corners, cv2.COLOR_GRAY2BGR)))

    return show_img

#2. 코너추출(특징점): Canny Edge -------------------------------------------------------------------
# 그레디언트의 크기 뿐 아니라 방향도 사용한다
def CannyEdge(img):
    edges = cv2.Canny(img,100,200)

    return edges

#3. 특징점 추출 -------------------------------------------------------------------
# SURF(Speeded-Up Robust Features)는 
# 인텐서티 계산 방법을 간략화 하는 등의 방법으로 SIFT 방법의 속도와 안정성을 개선한 것이다
def SURF(img, detector):    
    keyPoints, descriptors = detector.detectAndCompute(img, None)
    img_surf = cv2.drawKeypoints(img, keyPoints, None, (255, 0, 0),
                        cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    return img_surf

def MatchSURF(img1, img2, detector):    
    #매칭 및 RANSAC을 통해서 두 장의 영상간의 homography를 계산하고,    
    # find the keypoints and descriptors with SIFT
    kp1, des1 = detector.detectAndCompute(img1,None)
    kp2, des2 = detector.detectAndCompute(img2,None)
    
    # FLANN parameters
    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks=50)   # or pass empty dictionary
    flann = cv2.FlannBasedMatcher(index_params,search_params)
    matches = flann.knnMatch(des1,des2,k=2)

    # Need to draw only good matches, so create a mask
    matchesMask = [[0,0] for i in range(len(matches))]
    # ratio test as per Lowe's paper
    for i,(m,n) in enumerate(matches):
        if m.distance < 0.3*n.distance:
            matchesMask[i]=[1,0]
    draw_params = dict(matchColor = (0,255,0),
                    singlePointColor = (255,0,0),
                    matchesMask = matchesMask,
                    flags = 0)
    matchAll = cv2.drawMatchesKnn(img1,kp1,img2,kp2,matches,None,**draw_params)
    
    images = [img1, img2, matchAll]
    ImageShow(images, 'SURF')

#SIFT(Scale-Invariant Feature Transform)은 
# 특징점의 크기와 각도까지 같이 계산하여 이미지의 크기가 변하거나 회전해도 동일한 특징점을 찾을 수 있도록 하는 방법
def SIFT(img, detector):
    keyPoints, descriptors = detector.detectAndCompute(img,None)
    img_sift = cv2.drawKeypoints(img, keyPoints, None, (255, 0, 0),
                        cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    return img_sift

def MatchSIFT(img1, img2, detector):
    
    #매칭 및 RANSAC을 통해서 두 장의 영상간의 homography를 계산하고,    
    kp1, des1 = detector.detectAndCompute(img1,None)
    kp2, des2 = detector.detectAndCompute(img2,None)
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1,des2, k=2)
    good = []
    for m,n in matches:
        if m.distance < 0.3*n.distance:
            good.append([m])
    
    matchAll = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=2)
    
    images = [img1, img2, matchAll]
    ImageShow(images, 'SIFT')

#ORB(Oriented FAST and Rotated BRIEF)는 
# FAST 와 BRIEF를 기반으로 만들어진 알고리즘이다.
def ORB(img, detector):
    keyPoints = detector.detect(img, None)
    keyPoints, descriptors = detector.compute(img, keyPoints)
    img_orb = cv2.drawKeypoints(img, keyPoints, None, (0, 0, 255),
                        cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    return img_orb

#match ---------------------------------------------------------------
def MatchORB(img1, img2, detector, type):
    
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    
    #매칭 및 RANSAC을 통해서 두 장의 영상간의 homography를 계산하고,    
    kps1, fea1 = detector.detectAndCompute(img1, None)
    kps2, fea2 = detector.detectAndCompute(img2, None)
    matcher = cv2.BFMatcher_create(cv2.NORM_HAMMING, False)
    matches = matcher.match(fea1, fea2)
    
    #src, dst point
    pts1 = np.float32([kps1[m.queryIdx].pt for m in matches]).reshape(-1,1,2) #source point
    pts2 = np.float32([kps2[m.queryIdx].pt for m in matches]).reshape(-1,1,2) #destination point

    #두 장의 영상간의 homography를 계산하고
    H, mask = cv2.findHomography(pts1, pts2, cv2.RANSAC, 3.0)
    dbg_img = cv2.drawMatches(img1, kps1, img2, kps2, matches, None)
    dbg_img1 = cv2.drawMatches(img1, kps1, img2, kps2, [m for i,m in enumerate(matches) if mask[i]], None)
      
    matchAll = dbg_img[:,:,[2,1,0]]
    matchFilter = dbg_img1[:,:,[2,1,0]]
    
    images = [img1, img2, matchAll, matchFilter]
    ImageShow(images, type)


def ImageShow(images, type):    
    titles = ['PCB ALL('+type+')', 'PCB NG('+type+')', 'Match All('+type+')', 'Match Filter('+type+')']
    
    for i in range(len(images)):
        plt.subplot(2,2,i+1)
        plt.imshow(images[i],'gray')
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()

    if cv2.waitKey(0) == 27:
        cv2.destroyAllWindows()