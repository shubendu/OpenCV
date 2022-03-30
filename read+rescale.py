from configparser import Interpolation
import cv2 as cv

# reading images
# img = cv.imread('Resources/Photos/cat_large.jpg')
# cv.imshow('Cat',img)
# cv.waitKey(0)

def rescaleFrame(frame, scale = 0.75):
    #will work for images videos and live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] *scale)
    dimensions= (width,height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)



def changeRes(width,height):
    #only works for live video
    capture.set(3,width)
    capture.set(4,height)




# reading videos

capture = cv.VideoCapture('Resources/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow("Resized frame",frame_resized)
    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break
capture.release()
cv.destroyAllWindows()