import cv2
import utilities as util
import numpy as np

filename = "images_doc_t2/04.jpeg"
img = cv2.imread("images_doc/04.jpeg")

#img = cv2.resize(img, (1120, 630))

ret,thresh = cv2.threshold(img,127,255,0)
im2,contours,hierarchy = cv2.findContours(thresh, 1, 2)
cnt = contours[0]
M = cv2.moments(cnt)
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
cv2.drawContours(img,[box],0,(0,0,255),2)

print(box)


#cv2.imshow("Output", output)
#cv2.imshow("Contours detected",draw)
#cv2.imshow("Canny",img_Canny)

cv2.waitKey(0)