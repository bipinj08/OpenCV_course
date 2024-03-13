import cv2 as cv

img = cv.imread('Photos/group.webp')
cv.imwrite('Photos/group.png', img)

cv.waitKey(0)