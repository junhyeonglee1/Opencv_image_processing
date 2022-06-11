import cv2
import numpy as np

image = cv2.imread("lena.png", cv2.IMREAD_GRAYSCALE)

gaus = cv2.GaussianBlur(image, (7, 7), 0, 0)
dst1 = cv2.Laplacian(gaus, cv2.CV_16S, 7)

gaus1 = cv2.GaussianBlur(image, (3, 3), 0)
gaus2 = cv2.GaussianBlur(image, (9, 9), 0)
dst2 = gaus1 - gaus2

cv2.imshow("image", image)
cv2.imshow("Log", dst1)
cv2.imshow("Dog", dst2)
cv2.waitKey(0)
