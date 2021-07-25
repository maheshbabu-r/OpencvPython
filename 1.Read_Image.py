# Read Image
import cv2
# LOAD AN IMAGE USING 'IMREAD'
img = cv2.imread("Resourse/lena.png")
# DISPLAY
cv2.imshow("Lena Soderberg",img)
cv2.waitKey(0)