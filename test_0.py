import cv2
import numpy as np

img = cv2.imread("assets.png")

width , height = 110, 100


pts1 = np.float32([ [450,160],  [560, 160], [450,260],  [560, 260]])
pts2 = np.float32([ [0,0],      [width, 0], [0,height], [width, height]])

matrix = cv2.getPerspectiveTransform(pts1,pts2)

img_output = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Output", img)
cv2.imshow("Output_crazy", img_output)

cv2.waitKey(0)