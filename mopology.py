import numpy as np
import cv2

img = cv2.imread('redcircle.jpg', cv2.IMREAD_GRAYSCALE)

# kernel = np.array([ [0,1,0],
#                     [1,1,1],
#                     [0,1,0] ], np.uint8)
kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
kernel3 = cv2.getStructuringElement(cv2.MORPH_RECT, (7,7))
kernel4 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
kernel5 = cv2.getStructuringElement(cv2.MORPH_CROSS, (5,5))

ret, thr1 = cv2.threshold(img, 97, 255, cv2.THRESH_BINARY_INV)
img_dilation1 = cv2.dilate(thr1, kernel1, iterations = 2)
img_dilation2 = cv2.dilate(thr1, kernel2, iterations = 2)
img_dilation3 = cv2.dilate(thr1, kernel3, iterations = 2)
img_dilation4 = cv2.dilate(thr1, kernel4, iterations = 2)
img_dilation5 = cv2.dilate(thr1, kernel5, iterations = 2)

cv2.imshow('binary', thr1)
cv2.imshow('dilationRECT3size', img_dilation1)
cv2.imshow('dilationRECT5size', img_dilation2)
cv2.imshow('dilationRECT7size', img_dilation3)
cv2.imshow('dilationELLIPSe5size', img_dilation4)
cv2.imshow('dilationCROSs5size', img_dilation5)

cv2.waitKey(0)
cv2.destroyAllWindows()
