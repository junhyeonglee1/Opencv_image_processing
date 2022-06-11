# 동전 검출 허프변환
import cv2

img = cv2.imread('Coin.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, img_binary = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)

edge = cv2.Canny(img_binary, 50, 200)

circles = cv2.HoughCircles(edge, method = cv2.HOUGH_GRADIENT, dp=1, minDist = 25,
                           param1 = 30, param2 = 15, minRadius = 30, maxRadius = 100)

for circle in circles[0,:]:
    cx,cy,r = circle
    cx = int(cx)
    cy = int(cy)
    r = int(r)
    cv2.circle(img, (cx,cy),r,(0,255,255),2)
    print(cx,cy,r)

cv2.imshow('hough', img )

cv2.waitKey(0)
cv2.destroyAllWindows()
