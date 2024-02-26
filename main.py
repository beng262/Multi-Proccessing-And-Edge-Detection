import numpy as np
import cv2

rtsp_link = ''#You can add your rtsp link

orange_lower = np.array([0, 120, 80])
orange_upper = np.array([20, 255, 255])

blue_lower = np.array([100, 100, 100])
blue_upper = np.array([130, 255, 255])

cap = cv2.VideoCapture(rtsp_link)


while True:
    ret, frame = cap.read()

    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    orange_mask = cv2.inRange(hsv, orange_lower, orange_upper)

    blue_mask = cv2.inRange(hsv, blue_lower, blue_upper)

    combined_mask = cv2.bitwise_or(orange_mask, blue_mask)

    contours, _ = cv2.findContours(combined_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    mask = np.zeros_like(combined_mask)
    cv2.drawContours(mask, contours, -1, color=(255, 255, 255), thickness=cv2.FILLED)

    masked_img = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('Inside of Contours', masked_img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
