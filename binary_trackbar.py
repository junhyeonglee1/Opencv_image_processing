#이진화 트랙바설정
import cv2


def nothing(x):
    pass


cv2.namedWindow('Binary')
cv2.createTrackbar('threshold', 'Binary', 0, 255, nothing)
cv2.setTrackbarPos('threshold', 'Binary', 127)

img_color = cv2.imread('fing.jpg')
img_gray = cv2.imread('fing.jpg', cv2.IMREAD_GRAYSCALE)

while(True):
    low = cv2.getTrackbarPos('threshold', 'Binary')
    ret,img_binary = cv2.threshold(img_gray, low, 255, cv2.THRESH_BINARY)

    cv2.imshow('Binary', img_binary)

    img_result = cv2.bitwise_and(img_color, img_color, mask = img_binary)
    cv2.imshow('Result', img_result)


    if cv2.waitKey(1)&0xFF == 27:
        break


cv2.destroyAllWindows()