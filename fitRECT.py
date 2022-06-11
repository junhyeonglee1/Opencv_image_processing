#fing파일 이진화 보정해놓고 firRECT중 하나 적용해놓은것
import cv2
import numpy as np

img = cv2.imread('fing.jpg')
img_copy = img.copy()
img_copy2 = img.copy()
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT, (7,7))

ret, thr = cv2.threshold(img_gray, 163, 255, 0)

opening = cv2.morphologyEx( thr, cv2.MORPH_OPEN, kernel2)

img_erode = cv2.erode(opening, kernel2, iterations= 1)
img_dilation = cv2.dilate(img_erode, kernel2, iterations = 2)

contours, hierarchy = cv2.findContours(img_dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cnt = max(contours[:], key = lambda x:cv2.contourArea(x))

rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
cv2.drawContours(img_copy,[box],0,(0,255,0),3)
cv2.imshow('minAreaRect',img_copy)

cv2.waitKey(0)
cv2.destroyAllWindows()