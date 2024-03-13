import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Photos\gmunden.jpg')
img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
capture = cv.VideoCapture('Videos\Willi_chilling.mp4')




#resize image and video
def rescaleFrame(frame, scale = 0.5):
    #works for images, videos and live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width, height)

    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)


resized_img = rescaleFrame(img_rgb)

plt.imshow(img_rgb)
plt.axis('off')
plt.title('Original_image')
plt.show()

plt.imshow(resized_img)
plt.axis('off')
plt.title('Resized Image')
plt.show()

plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.imshow(img_rgb)
plt.axis('off')
plt.title('Ori image')

plt.subplot(1,2,2)
plt.imshow(resized_img)
plt.axis('off')
plt.title('resize img')

plt.tight_layout()
plt.show()

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)

    cv.imshow('Willi_Video', frame)
    cv.imshow('Willi_Video_resized', frame_resized)

    if cv.waitKey(20) & 0xFF ==ord('d'):
        break
capture.release()

cv.destroyAllWindows()
