import cv2

vid=cv2.VideoCapture(0)
while True:
    success, webcam=vid.read()
    cv2.imshow("Image",webcam)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        cv2.imwrite("image.jpg",webcam)
        break

vid.release()
cv2.destroyAllWindows()