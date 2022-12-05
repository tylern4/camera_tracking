# import the opencv library
import numpy as np
import cv2

width = 100


def move_left_right(center, face_center):
    if face_center > center+width:
        print("Left")
    elif face_center < center-width:
        print("Right")
    else:
        pass


# Load the cascade
# https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam.
cap = cv2.VideoCapture(0)
# To use a video file as input
# cap = cv2.VideoCapture('filename.mp4')
_, img = cap.read()

center = int(img.shape[1]/2)


while True:
    # Read the frame
    _, img = cap.read()
    cv2.line(img, (center, 0),
             (center, img.shape[0]),
             (255, 255, 255), 2)

    cv2.line(img, (center+width, 0),
             (center+width, img.shape[0]),
             (0, 0, 0), 1)

    cv2.line(img, (center-width, 0),
             (center-width, img.shape[0]),
             (0, 0, 0), 1)
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw the rectangle around each face
    for i, (x, y, w, h) in enumerate(faces):
        if i == 0:
            face_center = int((2*x+w)/2)
            move_left_right(center, face_center)
            cv2.line(img, (face_center, 0),
                     (face_center, img.shape[0]),
                     (255, 0, 0), 2)

    # Display
    cv2.imshow('img', img)
    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
# Release the VideoCapture object
cap.release()
