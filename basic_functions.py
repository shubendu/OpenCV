import cv2 as cv

img = cv.imread("Resources/Photos/cat.jpg")

cv.imshow("cat",img)

#converting to greyscale ==> to look for color intensity
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)


#blur ==> removes some noise from image 
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow("blur",blur)

#edge cascade=> canny edge detection => bluring+gradient computation
canny = cv.Canny(blur, 125, 175) #passing blur image to get less edges
cv.imshow('canny',canny)

#dilating the image
dilated = cv.dilate(canny, (7,7), iterations = 3)
cv.imshow('Dilated',dilated)

#eroding 
eroded = cv.erode(dilated,  (7,7), iterations = 3)
cv.imshow("eroded", eroded)

#resize
resized = cv.resize(img, (500,500), interpolation = cv.INTER_AREA) #read interpolation
cv.imshow("resized",resized)

# cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped',cropped)



cv.waitKey(0)