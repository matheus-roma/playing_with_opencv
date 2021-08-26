import cv2
import utilities as util

filename = "images_doc_t4/06.jpg"
img = cv2.imread("images_t4/06.jpg")

img_Canny, img_resised = util.scaleAdjust(img, 90)

draw, pts1 = util.getContours(img_Canny, img_resised) 

output = util.adjustImage(img_resised, pts1)

cv2.imshow("Output", output)
#cv2.imshow("Contours detected",draw)
#cv2.imshow("Canny",img_Canny)

#cv2.imwrite(filename, output)

#dst = util.blendImages()
#cv2.imshow("Output 2", dst)
cv2.waitKey(0)