import cv2
import utilities as util

cap = cv2.VideoCapture(0)

def WebCam():
    flag_row = False
    MAX_IMAGE_NUMBER = 30

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        raise IOError("Cannot open webcam")
    i=0
    
    while True:
        ret, frame = cap.read()
        frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
        cv2.imshow('Input', frame)
        c = cv2.waitKey(1)
        if c == 32 and flag_row == False: # space bar to start taking pictures
            flag_row = True
            i = 0
        
        if flag_row == True:
            cv2.imwrite("images/" + str(i) + ".jpg", frame)
            i+=1
            if i == MAX_IMAGE_NUMBER:
                flag_row = False

        if c == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


#menu
menu = input("1: Webcam: \n2: ")
if menu == '1':
    WebCam()