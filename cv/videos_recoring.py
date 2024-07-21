import cv2

video = cv2.VideoCapture(0)
codec = cv2.VideoWriter_fourcc(*'DIVX')
output = cv2.VideoWriter("output.mp4",codec,20.0,(640,480))
while True:
    status, frame = video.read()
   # print(status,frame)
    if not status:
        break
    # make changes from this line 
    newframe =frame*10
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    output.write(gray)
    cv2.imshow("video frame", frame)
    cv2.imshow("new video frame", newframe)
    if cv2.waitKey(1) == 27:
        break
    output.release()
    video.release()
    cv2.destroyAllWindows()