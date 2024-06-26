import numpy as np
import cv2 as cv

img = cv.imread('Photos\Cats.jpeg')
cv.imshow('Cats', img)
print(img.shape)

# To add and extra layer on photo
border_size = 30
border_color = (0, 0, 0)  # RGB color for black

# Add the border
image_with_border = cv.copyMakeBorder(
    img,
    top=border_size,  # Top border
    bottom=border_size,  # Bottom border
    left=border_size,  # Left border
    right=border_size,  # Right border
    borderType=cv.BORDER_CONSTANT,
    value=border_color
)

# Save or display the new image with border
cv.imwrite('image_with_border.jpg', image_with_border)
cv.imshow('layer added', image_with_border)



# Translation
def translation(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# +X --- Right
# -X --- Left
# +Y --- Down
# -Y --- Up
translated = translation(img, 100, 100)
# cv.imshow('translated_image', translated)

# Rotate
def rotation(img, angle, rot_point= None):
    (height, width) = img.shape[:2]

    if rot_point is None:
        rot_point = (width//2, height//2) # assigning the centre as a rotating point
    rotMat = cv.getRotationMatrix2D(rot_point, angle, 1.0) # 1.0 is a scaling factor
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotation(img, 90, (200,600))
# cv.imshow('rotated', rotated)


# Flipping an image
flip_img = cv.flip(img, -1)
# cv.imshow('flipped_img', flip_img)

#Cropping an image
# cropped = img[25:25, 50:50]
# cv.imshow('cropped_img', cropped)
#
#


cv.waitKey(0)
cv.destroyAllWindows()