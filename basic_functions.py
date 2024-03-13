import cv2 as cv

img = cv.imread('Photos\Cats.jpeg')
# cv.imshow('Cats',img)

# Converting to grayscale

grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Cats_grey', grey)

# Bluring the image

blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
# cv.imshow('Blur_cat', blur)

# Edge cascade (Getting the edges from the image)

canny = cv.Canny(img, 125, 175)
cv.imshow('canny_edge', canny)

canny1 = cv.Canny(blur, 125, 175) #more edges can be reduced by passing blured image
# cv.imshow('blur_canny_edge', canny1)

# Dilating the image
dilated = cv.dilate(canny,(9,9), iterations=3)
# cv.imshow('dilated', dilated)

# Eroding
eroded = cv.erode(dilated, (9,9), iterations=3)
# cv.imshow('eroded', eroded)

# Resized
resized = cv.resize(eroded, (500,500), interpolation=cv.INTER_CUBIC)
# cv.imshow('resized', resized)

cropped = img[200:600, 250:600]
# cv.imshow('cropped', cropped)


cv.waitKey(0)