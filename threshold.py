import cv2 as cv

# Thresholding is the binarization of an image. i.e:, image pixels are either (zero or black) or (255 or white)
img = cv.imread('Photos/Cats.jpeg')
# cv.imshow('Gmunden', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)


# Simple thresholding
threshold, thresh = cv.threshold(gray, 120, 255, cv.THRESH_BINARY)
cv.imshow('Simple Thresholding', thresh)

# Inverse threshold
threshold_inv, threshold_inv = cv.threshold(gray, 120, 255, cv.THRESH_BINARY_INV)
# cv.imshow('Thresholded Inverse', threshold_inv)

# Adaptive threshold- FInding the optimal threshold value itself. Mostly used in advance thresholding
'''
***ADAPTIVE THRESHOLDING PARAMERETERS***
cv.ADAPTIVE_THRESH_MEAN_C : used to take of mean of neighbourhood pixels. Also we can use GaussianThreshold(cv.ADAPTIVE_THRESH_GAUSSIAN_C) instead of mean.
cv.ADAPTIVE_THRESH_GAUSSIAN_C: It basically add a weight to each pixels and then compute the mean across all pixels
cv.THRESH_BINARY : Convert to binary image
blockSize = 11 : size of the block for taking mean of neighbourhood pixels
C = 9 : For fine tuning and subtracting from the mean of neighbourhood pixels
'''
adaptive_thresh = cv.adaptiveThreshold(gray, 150, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 9)
cv.imshow('Adaptive Threshold', adaptive_thresh)

cv.waitKey(0)