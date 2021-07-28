import cv2
import numpy as np

def getContours(canny, img):
    draw = img.copy()
    
    contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for i in contours:
        doc_perimeter = cv2.arcLength(i, True)
        if doc_perimeter > 500:
            cv2.drawContours(draw, i, -1, (0,0,255),2)
            pts = cv2.approxPolyDP(i, 0.05*doc_perimeter, True)
            #if len(pts) == 4:
                #print("The 4 points were detected")
    
    return draw, pts

def adjustImage(img, pts):
    x_0, y_0, width, height = cv2.boundingRect(pts)
    pts2 = np.float64([ [0,0], [width, 0], [0,height], [width, height]])
    matrix = cv2.getPerspectiveTransform(pts,pts2)

    img_output = cv2.warpPerspective(img, matrix, (width, height))
    
    return img_output