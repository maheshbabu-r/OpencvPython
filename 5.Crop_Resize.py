import cv2
import numpy as np

img = cv2.imread("Resourse/lambo.png")
print(img.shape)

# in resize it is x,y but for cropping inside a list it is y,x starts from top

imgResize = cv2.resize(img, (1000, 500))
print(imgResize.shape)

imgCropped = img[0:200, 200:500]

cv2.imshow("Image", img)
cv2.imshow("Image Resize",imgResize)
cv2.imshow("Image Cropped", imgCropped)

cv2.waitKey(0)