import cv2
import numpy as np
import matplotlib.pylab as plt

drawing = False
ix, iy, w, h = -1, -1, -1, -1

def selec_roi(event, x, y, flags, param):
    global drawing, ix, iy, img
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix = x
        iy = y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            img_draw = img.copy()
            cv2.rectangle(img_draw, (ix, iy), (x,y), (255, 0, 0), 2)
            cv2.imshow('img', img_draw)
    elif event == cv2.EVENT_LBUTTONUP:
        if drawing:
            drawing = False
            w = x - ix
            h = y - iy
            if (w > 0 and h > 0):
                img_draw = img.copy()
                cv2.rectangle(img_draw, (ix,iy), (x,y), (255, 0, 0), 2)
                cv2.imshow('img', img_draw)
                img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                roi = img_gray[iy:iy+h, ix:ix+w]
                cv2.imshow('gray', roi)
                bitXor = cv2.bitwise_xor( roi, roi)
                cv2.imshow('XOR', bitXor)


cap = cv2.VideoCapture(0)
ret, img = cap.read()
cv2.imshow('img', img)
cv2.setMouseCallback('img', selec_roi)
while (True):
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cv2.destryoAllWindows()