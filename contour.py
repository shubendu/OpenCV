import cv2 as cv
import numpy as np



img = cv.imread("Resources/Photos/cat.jpg")
# cv.imshow("cat",img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("gray",gray)

blank = np.zeros(img.shape, dtype = 'uint8')
cv.imshow('Blank', blank)

# blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
# # cv.imshow("blur",blur)

# canny = cv.Canny(blur, 125, 175)
# cv.imshow("canny edges ", canny)
#contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

#another way to get contours
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY) # it will binarize the image, if pixel is below 125 it will be 0(black) and if it is above 125 will be white
cv.imshow("thresh",thresh)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour(s) found')


cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow("Contours Drawn", blank)

cv.waitKey(0)