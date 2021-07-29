import cv2
import utilities as util

filename = "images_doc_t2/04.jpeg"
img = cv2.imread("images_doc/04.jpeg")

#img = cv2.resize(img, (1120, 630))


img_Gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_Blur = cv2.GaussianBlur(img_Gray, (25,25), 1)
img_Canny = cv2.Canny(img_Blur, 100, 100)


draw, pts1 = util.getContours(img_Canny, img) 
#origin = pts1[0]


#for i in range(0, 4):
#        if (pts1[i].any() < origin.any()):
#            origin = pts1[i]


#print(len(pts1))
#print(pts1)

output = util.adjustImage(img, pts1)


#cv2.imshow("Output", output)
#cv2.imshow("Contours detected",draw)
#cv2.imshow("Canny",img_Canny)

cv2.imwrite(filename, output)
cv2.waitKey(0)