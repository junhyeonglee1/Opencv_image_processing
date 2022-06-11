import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('coin.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('coin', img)

histogram = cv2.calcHist([img], [0], None, [256], [0,256])
plt.hist(img.ravel(), 256, [0, 256])

img_stretch = img.copy()

hist = sum_hist = np.zeros(256, np.int32)

for y in range(img.shape[0]):
    for x in range(img.shape[1]):
        k = img[y][x]
        hist[k] = hist[k]+1

lowest = hist[0]
highest = hist[0]
for i in range(hist.size):
    if lowest >= hist[i]:
        lowest = hist[i]
    elif highest <= hist[i]:
        highest = hist[i]

print('최대 %d', highest)
print('최소 %d', lowest)

for c in range(hist.size):

    out = ((hist[c]-lowest)/(highest - lowest)*255.0)
    if out < 0:
        sum_hist[c] = 0
    elif out > 255:
        sum_hist[c] = 255
    else:
        sum_hist[c] = int(out)


for y in range(img.shape[0]):
    for x in range(img.shape[1]):

        img_stretch[y][x] = np.int8(sum_hist[img[y][x]])

cv2.imshow('stretching', img_stretch)

histogram1 = cv2.calcHist([img_stretch], [0], None, [256], [0, 256])

plt.hist(img_stretch.ravel(), 256, [0, 256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()