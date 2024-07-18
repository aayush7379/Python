import cv2

video = cv2.VideoCapture(r"D:\note 10\Screenrecorder-2023-09-08-18-37-56-881.mp4")
while True:
    status, frame = video.read()
    print(status,frame)
    if not status:
        break
    cv2.imshow("video frame", frame)
    if cv2.waitKey(1) == 27:
        break
    video.release()
    cv2.destroyAllWindows()