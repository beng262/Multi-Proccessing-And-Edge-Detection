import cv2
import numpy as np

camera = cv2.VideoCapture(0)

while True:
    _,frame = camera.read()

    laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    laplacian = np.uint8(laplacian)
    cv2.imshow('Laplacian', laplacian)

    edges = cv2.Canny(frame, 100, 100)
    cv2.imshow('Canny', edges)


    if cv2.waitKey(5) == ord('q'):
         break

camera. release ()
cv2.destroyAllWindows ()