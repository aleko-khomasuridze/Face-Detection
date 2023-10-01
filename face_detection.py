"""
Real-time Face Detection and Visualization

Description:
This Python script uses OpenCV for real-time face detection through the Haar Cascade classifier. Detected faces are outlined, and additional visual elements are added, such as crosshairs at the center of the face, labels displaying a person's name, and a line connecting the face center to the frame center. The script continuously captures frames from the webcam, processes them for face detection, and displays the augmented frames.

Dependencies:
- OpenCV (cv2)
- faceDraw module (assumed to be available in the same directory)

Color Definitions:
- frame_f: Bright green for face outline
- frame_b: Darker green
- label_color: Purple
- blue, green, red, purple, yellow, cyan, white: Basic color constants

Author: Your Name
Date: December 4, 2022
"""


import cv2
from faceDraw import faceDraw

cap = cv2.VideoCapture(0)

# design colors
frame_f     = (240,  85,  60)   # bright green 
frame_b     = (248,  181, 50)   # darker green
label_color = (90,   72, 240)   # purple

# basic colors
blue   = (0xFF, 0x00, 0x00)
green  = (0x00, 0xFF, 0x00)
red    = (0x00, 0x00, 0xFF)
purple = (0xFF, 0x00, 0xFF)
yellow = (0x00, 0xFF, 0xFF)
cyan   = (0xFF, 0xFF, 0x00)
white  = (0xFF, 0xFF, 0xFF)


def findFace(img):
    faceCascade = cv2.CascadeClassifier("cascades\\data\\haarcascade_frontalface_default.xml")
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.2, 8)

    for(x,y,w,h) in faces:
        faceDraw.frame(img, x, y, w, h, label_color, 20, 2)                   # draw outline
        faceDraw.center(img, x, y, w, h, frame_f, "crossHair", 15)            # draw croshair on the center of a face 
        faceDraw.label(img,  x, y, w, h, frame_f, "person".upper(), white)   # draw label to display persons name

        width = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))//2
        height = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))//2

        line_color  = yellow  # line that connects face center with frame center

        # darw a line that connects face center with frame center
        cv2.line(img, (x+w//2, y+h//2), (width, height), line_color, 2)
        


while True:
    middle_box_height = 30  

    width = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))//2
    height = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))//2

    _, img = cap.read()

    findFace(img)
   
    cv2.rectangle(img, (width-middle_box_height//2, height-middle_box_height//2), 
                  (width+middle_box_height//2, height+middle_box_height//2), green,  2)
    cv2.imshow("frame", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

