
import cv2
import numpy as np
import time as tp

capturetimes = []
starttime = tp.time()
procestimes = []
inrangetimes = []
bitwisetimes = []
cannytimes = []

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
    #defining upper and lower blue for presentation , first digit determines hue, to have a different colour use a different range for upper and lower
    lower_blue = np.array([60, 40, 40])
    upper_blue = np.array([150, 255, 255])
    #Changing the parameters, smaller numbers give more edges but also noise
    #Ik zal slagen

    s1 = tp.time()
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    inrangetimes.append(tp.time() - s1)

    s1 = tp.time()
    res = cv2.bitwise_and(frame, frame, mask=mask)
    bitwisetimes.append(tp.time() - s1)

    s1 = tp.time()
    edges = cv2.Canny(mask, 50, 50)
    cannytimes.append(tp.time() - s1)

    procestimes.append(tp.time()- startprocestime)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)

    cv2.imshow('res', res)
    cv2.imshow('edges', edges)

    #k = cv2.waitKey(5) & 0xFF
    #if k == 27:
    #   break
    if cv2.waitKey(5) != -1:
        break

cv2.destroyAllWindows()
# release webcam or it cannot be used in other applications
# ik ga slagen !!!
cap.release()

#total time of script
endtime = tp.time()
duration = endtime - starttime

#this is for the list avarages of the capturetime

# duration = total time, getaverage(ct) = avarage to catch an image, getaverage(pt) = averagetime to process a image
print(duration, ",", getAverage(capturetimes), ",", getAverage(procestimes), ",", getAverage(inrangetimes), ",", getAverage(bitwisetimes), ",", getAverage(cannytimes))

