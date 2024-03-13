import cv2 as cv
import numpy as np


img = cv.imread('Photos\Cats.jpeg')
img = cv.resize(img, (700, 900))
cv.putText(img, 'Fredi', (50,50), 3, 1.0, (0,0,255), thickness=2)
cv.putText(img, 'Willi', (400,800), 3, 1.0, (0,0,255), thickness=2)
# cv.imshow('Gmunden', img)
# cv.imwrite('Photos\Gmunden.jpg', img)


#
blank = np.zeros((800,800, 3), dtype='uint8')
# cv.imshow('blank image', blank)

# 1. Paint the image with certain colors
# blank[:] = 0,255,0     #yellow square inside the image

# blank[20:200, 20:500] = 0,255,255
# cv.imshow('blank_yellow', blank)

# 2. Draw a rectangle in the image

cv.rectangle(blank, (blank.shape[0]//2, blank.shape[0]//2), (800,800), (0,255,0), thickness=cv.FILLED, lineType=cv.LINE_AA) # cv.FILLED with fill the box with same color else use number for its thicklness
# cv.rectangle(blank, (21,21), (501,201), (0,255,0), thickness=-1, lineType=cv.LINE_AA) # same as above line
cv.rectangle(blank, (0,0), (blank.shape[0]//2, blank.shape[0]//2), (0,0,255), thickness=-1, lineType=cv.LINE_AA)
# cv.imshow('green_rectangle',blank)

# 3. Draw a circle
cv.circle(blank, (blank.shape[0]//2, blank.shape[0]//2), 80, (255,0,0), thickness=-1)
# cv.imshow('Circle', blank)

# 4. Draw a line
cv.line(blank, (0,0), (800,800), (255,255,255), thickness=3)
cv.line(blank, (0,800), (800,0), (255,255,255), thickness=3)
cv.imshow('Line', blank)

# 5. Write a text
cv.putText(blank, 'Hello Image', (297,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,45),2)
# cv.imshow('Created Image', blank)

# 6. Saving the image
# cv.imwrite('Photos\Created_Image.png', blank)
cv.waitKey(0)
cv.destroyAllWindows()