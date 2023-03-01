import cv2 

face_detector = cv2.CascadeClassifier('./weights/cascade.xml')

def streaming():
    cap = cv2.VideoCapture(0)
    if cap.isOpened() == True:
        print("camera webcam active . . .")
    else:
        print("camera webcam deactiave . . .")
    while cap.isOpened():
        ret, frame = cap.read()
        try:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            results = face_detector.detectMultiScale(gray, 1.3, 5)
            for (x,y,w,h) in results:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.imshow("webcam", frame)
            if cv2.waitKey(1) == 27:
                break
        except:
            cap = cv2.VideoCapture(0)