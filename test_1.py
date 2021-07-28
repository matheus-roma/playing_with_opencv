import cv2
import numpy as np
import utilities

img = cv2.imread("shapes.png")

img_Gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_Canny = cv2.Canny(img_Gray, 50, 50)


utilities.getContours(img_Canny, img) 


cv2.imshow("Contours detected",img)

cv2.waitKey(0)