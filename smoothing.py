import cv2 as cv
import numpy as np

img = cv.imread("Resources/Photos/cats.jpg")
cv.imshow("cat",img)

#averaging
average = cv.blur(img,(3,3))
cv.imshow("Average Blur", average)


#gaussian blur==> instead of computing the average each surrounding pixels give some particular weight instead of averaging
gauss = cv.GaussianBlur(img, (3,3),0)
cv.imshow("Gaussian Blur",gauss)


#median blur
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur',median)

#bilateral blur
bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow("bilateral",bilateral)

cv.waitKey(0)