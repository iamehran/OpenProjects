import cv2
import numpy as np

vid=cv2.VideoCapture(0)
webcam=cv2.imread("./image.jpg")

while True:
    success, webc=vid.read()
    if success:
        imghsv=cv2.cvtColor(webc,cv2.COLOR_BGR2HSV)
        low=np.array([0,120,170])
        upper=np.array([10,255,255])
        mask1=cv2.inRange(imghsv,low,upper)
        low=np.array([170,120,70])
        upper=np.array([180,255,255])
        mask2=cv2.inRange(imghsv,low,upper)
        mask_r=mask1+mask2

        kernal=np.ones((3,3),np.uint8)
        mask_r=cv2.morphologyEx(mask_r,cv2.MORPH_OPEN,kernal,iterations=10)
        mask_r = cv2.morphologyEx(mask_r, cv2.MORPH_DILATE, kernal, iterations=10)

        part1=cv2.bitwise_and(webcam,webcam,mask=mask_r)
        redn=cv2.bitwise_not(mask_r)
        part2=cv2.bitwise_and(webc,webc,mask=redn)

        cv2.imshow("Cloak",part1+part2)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break

vid.release()
cv2.destroyAllWindows()