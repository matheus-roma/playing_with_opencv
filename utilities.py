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
    return draw, pts


def adjustImage(img, pts):
    x_0, y_0, width, height = cv2.boundingRect(pts)

    myPoints = pts.reshape((4,2))
    myPointsNew = np.zeros((4,1,2),np.float32)
    add = myPoints.sum(1)

    myPointsNew[0] = myPoints[np.argmin(add)]
    myPointsNew[3] = myPoints[np.argmax(add)]
    diff = np.diff(myPoints,axis=1)
    myPointsNew[1]= myPoints[np.argmin(diff)]
    myPointsNew[2] = myPoints[np.argmax(diff)]
    print("NewPoints",myPointsNew)
 
    pts2 = np.float32([ [0,0], [width, 0], [0,height], [width, height]])
    matrix = cv2.getPerspectiveTransform(myPointsNew,pts2)

    img_output = cv2.warpPerspective(img, matrix, (width, height))
    return img_output
