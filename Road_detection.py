
import cv2
import numpy as np

#number gives 1 if you use a webcam 0 if it is built in
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    # hue saturation value, different way to represent colours
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #defining upper and lower blue for presentation , first digit determines hue, to have a different colour use a different range for upper and lower
    lower_blue = np.array([60, 40, 40])
    upper_blue = np.array([150, 255, 255])
    #Changing the parameters, smaller numbers give more edges but also noise

    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    edges = cv2.Canny(mask, 50, 50)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)

    cv2.imshow('res', res)
    cv2.imshow('edges', edges)



    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
# release webcam or it cannot be used in other applications

cap.release()
