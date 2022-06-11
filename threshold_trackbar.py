import cv2
import numpy as np
import matplotlib.pyplot as plt

def nothing(x):
    pass

cv2.namedWindow('thr1')
cv2.createTrackbar('T','thr1', 0, 255, nothing)
cv2.setTrackbarPos('T', 'thr1', 127)

img = cv2.imread('redcircle.jpg',cv2.IMREAD_GRAYSCALE)
img_binary = img.copy()

while(True):
    pos = cv2.getTrackbarPos('T', 'thr1')

    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            if img[y][x] >= pos:
                img_binary[y][x] = 255
            else:
                img_binary[y][x] = 0
    cv2.imshow('thr1', img_binary)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
