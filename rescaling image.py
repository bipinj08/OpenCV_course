import cv2 as cv

img = cv.imread('Photos\gmunden.jpg')
cv.imshow('Duck',img)

def scaledframe(frame, scaled=0.2):
    width = int(frame.shape[0] * scaled)
    height = int(frame.shape[1] * scaled)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
resized_img = scaledframe(img)
cv.imshow('resized image', resized_img)
cv.imwrite('Photos\Duck.png', resized_img)

cv.waitKey(0)