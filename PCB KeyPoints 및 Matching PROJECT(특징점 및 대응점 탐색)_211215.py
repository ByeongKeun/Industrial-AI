import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import Lib_KeyPointAndMatch as km

img1 = cv2.imread('./Wed_ComputerVision/img/final/pcb_all.JPG', cv2.IMREAD_COLOR)
img2 = cv2.imread('./Wed_ComputerVision/img/final/pcb_ng1.JPG', cv2.IMREAD_COLOR)
img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

#특징점 추출: ORB(Oriented FAST and Rotated BRIEF)
detector_orb = cv2.ORB_create(100)
detector_orb.setMaxFeatures(200)

img_orb1 = km.ORB(img1, detector_orb)
img_orb2 = km.ORB(img2, detector_orb)
km.MatchORB(img_orb1, img_orb2, detector_orb, 'ORB')

#특징점 추출: SIFT(Oriented FAST and Rotated BRIEF)
detector_sift = cv2.xfeatures2d.SIFT_create()

img_sift1 = km.SIFT(img1, detector_sift)
img_sift2 = km.SIFT(img2, detector_sift)
km.MatchSIFT(img_sift1, img_sift2, detector_sift)

#특징점 추출: SURF(Speeded-Up Robust Features)
detector_surf = cv2.xfeatures2d.SURF_create(100)
detector_surf.setExtended(True)
detector_surf.setNOctaves(3)
detector_surf.setNOctaveLayers(10)
detector_surf.setUpright(False)

img_surf1 = km.SIFT(img1, detector_surf)
img_surf2 = km.SIFT(img2, detector_surf)
km.MatchSURF(img_surf1, img_surf2, detector_surf)

# 엣지(특징점)추출: Harris corner
img_harris1 = km.cornerHarris(img1)
img_harris2 = km.cornerHarris(img2)
km.MatchORB(img_harris1, img_harris2, detector_orb, 'Harris Corner')

#코너추출(특징점): Canny Edge
img_canny1 = km.CannyEdge(img1)
img_canny2 = km.CannyEdge(img2)
km.MatchORB(img_canny1, img_canny2, detector_orb, 'Canny Edge')
