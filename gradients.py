import cv2 as cv
import numpy as np

img = cv.imread('Photos/Cats.jpeg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray Cats', gray)


'''
The Laplacian operator is a commonly used image processing technique for edge detection. 
It calculates the second derivative of the image intensity, which highlights regions of rapid intensity change.
Typically corresponding to edges in the image.


np.absolute(lap): This takes the absolute value of the Laplacian image. 
The Laplacian operator can produce negative values in areas where the intensity decreases rapidly, which would appear as dark regions in the output. 
Taking the absolute value ensures that all edges are represented as positive intensities.
'''
# Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)


# Sobel gradients
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0,1)

combined_sobel = cv.bitwise_or(sobelx, sobely)
# cv.imshow('Sobel X', sobelx)
# cv.imshow('Sobel Y', sobely)
cv.imshow('Combined sobel', combined_sobel)

# compare above laplacian and sobel images to canny edge detector
canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny)

cv.waitKey(0)