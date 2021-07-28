import cv2

def getContours(canny, img):
    contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for i in contours:
        cv2.drawContours(img, i, -1, (255,0,0),3)