import cv2

img = cv2.imread("j.png")
while True:
    cv2.imshow("Output", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
