import cv2 as cv
import numpy as np

img = cv.imread("Resources/Photos/cat.jpg")

cv.imshow("cat",img)

#translation==> x and y here number of pixels you want to shift along x and y axis
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# when negative values for x then translate images to left
# -y shifting up
#x = > Right
#y = > Down

translated  = translate(img, -100, 100)
cv.imshow("translated", translated)


#rotation
def rotate(img, angle, rotatePoint = None):
    (height,width) = img.shape[:2]
    
    if rotatePoint is None:
        rotpoint = (width//2, height//2)
        
    rotMat = cv.getRotationMatrix2D(rotpoint, angle, 1.0)
    dimensions = (width,height)
    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -45)
cv.imshow('Rotated', rotated)


#resize
resized = cv.resize(img,(500,500), interpolation = cv.INTER_AREA)
cv.imshow("resized", resized)

#flipping
flip = cv.flip(img, 0) # 0 => vertical, 1=>horizontally , -1 => both horizontal and vertical
cv.imshow("flip", flip)



cv.waitKey(0)