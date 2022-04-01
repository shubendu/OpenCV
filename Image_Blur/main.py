import cv2 as cv
import numpy as np

def resize(img,new_width = 500):
    height,width,_ = img.shape
    ratio = height/width
    new_height = int(ratio* new_width)
    return cv.resize(img,(new_width,new_height))



face_cascade = cv.CascadeClassifier("haar_face.xml")

#img = cv.imread("D:\OPENCV\OpenCV\Resources\Photos\group.jpg")
#for video
# cap = cv.VideoCapture("D:\OPENCV\OpenCV\Resources\Videos\example.mp4")
cap = cv.VideoCapture(0)
while True:
    _,frame = cap.read()
    frame = resize(frame)
    detections = face_cascade.detectMultiScale(frame,scaleFactor=1.1, minNeighbors = 6)

    for face in detections:
        x,y,w,h = face
        frame[y:y+h,x:x+w] = cv.GaussianBlur(frame[y:y+h,x:x+w],(15,15),cv.BORDER_DEFAULT)
        cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        cv.imshow("output",frame)

        if cv.waitKey(1) == 27:
            break

cap.release()
cv.destroyAllWindows()