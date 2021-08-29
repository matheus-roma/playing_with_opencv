import cv2
import glob
import numpy as np
from numpy.core.fromnumeric import size



def scaleAdjust(img, scale_percent):
    

    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    
    img_resised = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    
    img_Gray = cv2.cvtColor(img_resised, cv2.COLOR_BGR2GRAY)
    img_Blur = cv2.GaussianBlur(img_Gray, (5,5), 1)
    img_Canny = cv2.Canny(img_Blur, 100 , 100)


    return img_Canny, img_resised

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
 
    pts2 = np.float32([ [0,0], [width, 0], [0,height], [width, height]])
    matrix = cv2.getPerspectiveTransform(myPointsNew,pts2)

    img_output = cv2.warpPerspective(img, matrix, (width, height))
    return img_output

def blendImages():    
    # Import all image files with the .jpg extension
    files = glob.glob ("*.jpg")
    image_data = []
    for my_file in files:
        this_image = cv2.imread(my_file, 1)
        image_data.append(this_image)
    
    # Calculate blended image
    dst = image_data[0]
    for i in range(len(image_data)):
        if i == 0:
            pass
        else:
            alpha = 1.0/(i + 1)
            beta = 1.0 - alpha
            dst = cv2.addWeighted(image_data[i], alpha, dst, beta, 0.0)
    
    # Save blended image
    #cv2.imwrite('weather_forecast.png', dst)
    #cv2.imshow("Output", dst)
    return dst