from tarfile import BLOCKSIZE
import cv2 as cv

img = cv.imread("Resources/Photos/cats 2.jpg")
cv.imshow("cat",img)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)

#simple threshold
threshold, thresh = cv.threshold(gray, thresh = 150, maxval = 255, type = cv.THRESH_BINARY )
cv.imshow("Thresh",thresh)

#simple threshold
threshold, thresh_inv = cv.threshold(gray, thresh = 150, maxval = 255, type = cv.THRESH_BINARY_INV )
cv.imshow("Thresh Inverse",thresh_inv)


#Adoptive Threshold                                                                   ADAPTIVE_THRESH_MEAN_C
adaptive_thresh = cv.adaptiveThreshold(src = gray, maxValue = 255, adaptiveMethod = cv.ADAPTIVE_THRESH_GAUSSIAN_C, thresholdType = cv.THRESH_BINARY, blockSize = 11, C = 3) # for inverse ==>cv.THRESH_BINARY_INV
cv.imshow("Adaptive Threshold",adaptive_thresh)



cv.waitKey(0)