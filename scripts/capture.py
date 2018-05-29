import numpy as np
import cv2 as cv
import os
import recognize as rgz
import time


def sim1(img1, img2):
    h, w = img1.shape
    total = h*w
    diff = cv.absdiff(img1,img2)
    num = (diff<10).sum()
    return num*1.0/total


flag = 0
cap = cv.VideoCapture(0)

firstRun=0


while(True):
    ret, frame = cap.read()
    timeNow = time.time()
    gray = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)

    if firstRun == 0:
    	lastTime = timeNow
#
        lastFrame = gray
        firstRun = 1
    else:
        sim = sim1(lastFrame, gray)
        if sim < 0.8:
            if timeNow - lastTime > 5:
                cv.imwrite('../data/test/captured.jpg', gray)
                rgz.read_data('../data/test/captured.jpg', 'test')
    lastFrame = gray
    

    cv.imshow('frame',gray)

        

    if cv.waitKey(1) & 0xFF == ord('q'):
        cv.imwrite('../data/test/captured.jpg', gray)
        rgz.read_data('../data/test/captured.jpg', 'test')
        break

cap.release()
cv.destroyAllWindows()
