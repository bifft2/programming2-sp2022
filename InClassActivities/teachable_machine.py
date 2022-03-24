import cv2

# https://stackoverflow.com/questions/34588464/python-how-to-capture-image-from-webcam-on-click-using-opencv

cam = cv2.VideoCapture(0)
cv2.namedWindow("Camera Window")

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")

    cv2.imshow("Camera Window", frame)
    k = cv2.waitKey(1)

    if k%256 == 32:
        # SPACE pressed
        cv2.imwrite("opencv_photo.png", frame)

        cam.release()
        cv2.destroyAllWindows()
        exit()
