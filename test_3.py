import cv2
import utilities as util

#filename = "images_doc_t2/04.jpeg"
img = cv2.imread("images_doc/07.jpeg")

scale_percent = 60 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)


img_Gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_Blur = cv2.GaussianBlur(img_Gray, (25,25), 1)
img_Canny = cv2.Canny(img_Blur, 100, 100)


draw, pts1 = util.getContours(img_Canny, img) 

output = util.adjustImage(img, pts1)

cv2.imshow("Output", output)
cv2.imshow("Contours detected",draw)
cv2.imshow("Canny",img_Canny)

#cv2.imwrite(filename, output)
cv2.waitKey(0)