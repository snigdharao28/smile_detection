#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 23:04:04 2018

@author: snigdharao
"""

import cv2
"""
import numpy as np
import sys
"""


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')

def detect(gray, frame):
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w] 
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.1, 3)
        for (sx,sy,sw,sh) in smiles:
            cv2.rectangle(roi_color, (sx,sy), (sx+sw,sy+sh), (255,0,0), 2)
    return frame

video_capture = cv2.VideoCapture(0)         # pass 1 if external webcam is plugged in. 0 for laptop's webcam

while True:
    _, frame = video_capture.read()         #getting the last frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)          #color transformations
    canvas = detect(gray, frame)        #output of our detect function
    cv2.imshow('Video', canvas)          #display the output
    if cv2.waitKey(1) & 0xFF == ord('q'):        #if key pressed, exit
        break
    
video_capture.release()          #webcam turned off
cv2.destroyAllWindows() 
