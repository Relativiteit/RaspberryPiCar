import cv2
import numpy as np
import time as tp

capturetimes = []
starttime = tp.time()
procestimes = []
filtertimes = []
gaussiantimes = []
mediantimes = []
bilateraltimes = []

def getAverage(alist):
    duration = 0
    for i in alist:
        duration = duration + i

    duration = duration / len(alist)
    return duration

#number gives 1 if you use a webcam 0 if it is built in
cap = cv2.VideoCapture(0)

while True:
    startcapturetime = tp.time()
    _, frame = cap.read()
    capturetimes.append(tp.time()- startcapturetime)

    startprocestime = tp.time()
    # hue saturation value, different way to represent colours
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #defining upper and lower yellow, first digit determines hue, to have a different colour use a different range for upper and lower
    lower_blue = np.array([60, 40, 40])
    upper_blue = np.array([150, 255, 255])


    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    res = cv2.bitwise_and(frame, frame, mask = mask)

    s1 = tp.time()
    kernel = np.ones((15, 15), np.float32) / 225
    smoothed = cv2.filter2D(res, -1, kernel)
    filtertimes.append(tp.time() - s1)

    s1 = tp.time()
    #different blur filters
    blur = cv2.GaussianBlur(res,(15,15), 0)
    gaussiantimes.append(tp.time() - s1)

    s1 = tp.time()
    median = cv2.medianBlur(res,15)
    mediantimes.append(tp.time() - s1)

    s1 = tp.time()
    bilateral = cv2.bilateralFilter(res, 15, 75, 75)
    bilateraltimes.append(tp.time() - s1)

    procestimes.append(tp.time() - startprocestime)

    #commented out the filters if not used, due to limited computing power

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)

    cv2.imshow('res', res )
    cv2.imshow('smoothed', smoothed)
    cv2.imshow('blur', blur)
    cv2.imshow('median', median)
    cv2.imshow('bilateral', bilateral)

    if cv2.waitKey(5) != -1:
        break

cv2.destroyAllWindows()
#release webcam or it cannot be used in other applications

cap.release()

#total time of script
endtime = tp.time()
duration = endtime - starttime

print(duration, ",", getAverage(capturetimes), ",", getAverage(procestimes), ",",getAverage(filtertimes), ",", getAverage(gaussiantimes), ",", getAverage(mediantimes), ",", getAverage(bilateraltimes))



