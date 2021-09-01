import cv2
import utilities as util

#filename = "images_t5/17.jpg"
img = cv2.imread("jpg/05.jpg")



#img = cv2.imread("images_doc_t4/*.jpeg")

img_Canny, img_resised = util.scaleAdjust(img, 100)

draw, pts1 = util.getContours(img_Canny, img_resised) 

output = util.adjustImage(img_resised, pts1)

#cv2.imshow("Output", output)
#cv2.imshow("Contours detected",draw)
#cv2.imshow("Canny",img_Canny)

#cv2.imwrite(filename, output)
 
dst = util.blendImages()
cv2.imshow("Output 2", dst)

#util.blendImages()

cv2.waitKey(0)