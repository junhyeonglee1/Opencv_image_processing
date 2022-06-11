import cv2
import numpy as np
cap = cv2.VideoCapture(0) #캠활용

while True:
    ret, frame = cap.read()
    YCrCb = cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb) # HSV변환
    lowest = np.array([0, 133, 77], dtype = "uint8") #피부색 저점 범위 설정
    highest = np.array([255, 173, 127], dtype = "uint8") #피부색 고점 범위 설정
    skinYCbCr = cv2.inRange(YCrCb, lowest, highest) #피부색 범위 저장
    blurring = cv2.GaussianBlur(skinYCbCr, (7, 7), 3) #흐릿하게 하기위한 블러링
    ret,thresh = cv2.threshold(blurring,0,255,cv2.THRESH_BINARY) #이진화

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7)) #모폴로지연산을 위한 커널
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel) # 오프닝 연산

    img_erode = cv2.erode(opening, kernel, iterations=1) # 침식 연산
    img_dilation = cv2.dilate(img_erode, kernel, iterations=2) # 팽창연산

    contours, hierarchy = cv2.findContours(img_dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #컨투어 설정
    contours = max(contours, key=lambda x: cv2.contourArea(x))
    cv2.drawContours(frame, [contours], -1, (255,255,0), 2) #손 테두리 설정

    rect = cv2.minAreaRect(contours) # 손 추적할 사각형 생성
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    cv2.drawContours(frame, [box], 0, (0, 255, 0), 3)

    hull = cv2.convexHull(contours) #컨벡스홀 설정
    cv2.drawContours(frame, [hull], -1, (0, 255, 255), 2)

    hull = cv2.convexHull(contours, returnPoints=False)
    defects = cv2.convexityDefects(contours, hull) #볼록결함 생성

    if defects is not None:
      cnt = 0
    for i in range(defects.shape[0]):
      s, e, f, d = defects[i][0]
      start = tuple(contours[s][0]) #볼록결함 시작점 끝점 멀리있는 점설정
      end = tuple(contours[e][0])
      far = tuple(contours[f][0])
      a = np.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2) #손가락의 길이 수로 저장
      b = np.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
      c = np.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
      angle = np.arccos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)) #코사인법칙활용
      if angle <= np.pi / 2: #90도가 되지않으면 손가락인식 카운트
        cnt += 1
        cv2.circle(frame, far, 4, [0, 0, 255], -1)
    if cnt > 0:
      cnt = cnt+1 #각이 하나가 나오면 손가락이 2개이므로 하나 추가
    cv2.putText(frame, str(cnt), (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)  # 손가락 개수 표현
    cv2.imshow('final_result', frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
