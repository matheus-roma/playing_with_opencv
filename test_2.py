import cv2
import utilities as util

img = cv2.imread("images_doc/01.jpeg")

img_Gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_Blur = cv2.GaussianBlur(img_Gray, (25,25), 1)
img_Canny = cv2.Canny(img_Blur, 100, 100)


draw, pts1 = util.getContours(img_Canny, img) 
#print(len(pts1))
#print(pts1)

output = util.adjustImage(img, pts1)

cv2.imshow("Output", output)
#cv2.imshow("Contours detected",img)
#cv2.imshow("Canny",img_Canny)

cv2.waitKey(0)