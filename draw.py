import cv2 as cv
import numpy as np 

blank = np.zeros((500,500,3), dtype='uint8')
# cv.imshow("blank",blank)

#paint the image at cetain column
# blank[:] = 0,255,0
# cv.imshow("Green",blank)

#draw a rectangle
# cv.rectangle( blank, (0,0),(300,300),(0,255,0), thickness = -1)#cv.FILLED or 2
# cv.rectangle( blank, (0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0), thickness = -1)#cv.FILLED or 2
# cv.imshow('Rec',blank)

# #draw a circle
# cv.circle(blank, (blank.shape[1]//2,blank.shape[0]//2), 40, (0,0,255), thickness=3)
# cv.imshow('Circle',blank)

# #draw a line
# cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,255,0), thickness = 3)
# cv.imshow("line",blank)

#write text
cv.putText(blank,'Hello', (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0 ,(0,255,0), 2)
cv.imshow("blank",blank)
cv.waitKey(0) 
