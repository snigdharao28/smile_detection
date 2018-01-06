#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 23:04:04 2018

@author: snigdharao
"""
#importing the necessary libraries
import cv2

#loading the cascades
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')     #loading the cascades for the face
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')          #loading the cascades for the smile
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')          #loading the cascades for the eyes


#defining a func to do the detections
def detect(gray, frame):
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)             #applying detectMultiScale method to detect one or several faces in the image
    
    for (x,y,w,h) in faces:         #for every face detected
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), 2)            #co-ordinates of the rectangles drawn around the face #color is red (0,0,red)
        roi_gray = gray[y:y+h, x:x+w]           #getting region of interest in b&w image
        roi_color = frame[y:y+h, x:x+w]         #getting region of interest in colored image
        """
        can ignore the enclosed code for eye detection if not necessary
        
        starting from here
        """
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 3)            #applying detectMultiScale method to detect one or several eyes in the image
        for (ex,ey,ew,eh) in eyes :         #for every eye detected
            cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,255,0), 2)             #co-ordinates of rectangles drawn around the eyes  #color is green (0,green,0)
        """
        till here
        """
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.7, 22)          #applying detectMultiScale method to detect one or several smiles in the image
        for (sx,sy,sw,sh) in smiles:            #for every smile detected
            cv2.rectangle(roi_color, (sx,sy), (sx+sw,sy+sh), (255,0,0), 2)          #co-ordinates of rectangles drawn around the eyes #color is blue (blue, 0, 0)
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
cv2.destroyAllWindows()             #destroy all windows in which images were displayed
