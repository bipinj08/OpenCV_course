import cv2 as cv
import os
import matplotlib.pyplot as plt
cwd = os.getcwd()
print(cwd)
img = cv.imread(r'Photos\gmunden.jpg')

# Convert BGR to RGB
img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

plt.imshow(img_rgb)
plt.axis('off')
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()

