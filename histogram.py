import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('Photos\Fredi & Wilma.png')
# cv.imshow('cats', img)

# converting the gray scale image
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

# Creating the mask
blank = np.zeros(img.shape[:2], dtype='uint8')
circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1) #use gray image shape for gray image mask


mask = cv.bitwise_and(img, img, mask=circle)
cv.imshow('mask', mask)

#Grayscale Histogram
# gray_hist = cv.calcHist([gray], [0], mask, [256], [0, 256])
# plt.figure()
# plt.title("Histogram")
# plt.xlabel('Bins')
# plt.ylabel('Number of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()


# computing the color histogram
plt.figure()
plt.title("Color Histogram")
plt.xlabel('Bins')
plt.ylabel('Number of pixels')
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], circle, [256], [0, 256]) #passing circle as mask as we need gray scale for masking
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()
cv.waitKey(0)
cv.destroyAllWindows()