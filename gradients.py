import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)



#laplacian
lap = cv.Laplacian(src = gray, ddepth = cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("Laplacian",lap)


#sobel
sobelx = cv.Sobel(src = gray, ddepth = cv.CV_64F, dx = 1, dy = 0 )
sobely = cv.Sobel(src = gray, ddepth = cv.CV_64F, dx = 0, dy = 1 )
combined_sobel = cv.bitwise_or(sobelx,sobely)

cv.imshow("Sobel X", sobelx)
cv.imshow("Sobel Y", sobely)
cv.imshow("Sobel Combined",combined_sobel)

#canny
canny = cv.Canny(image = gray, threshold1 = 150, threshold2 = 175)
cv.imshow("Canny",canny)


cv.waitKey(0)