import cv2 
from components.detector import Detector
from components.bbox import BBOX
from components.draw import Draw
from components.tracker import CentroidTracker


ct = CentroidTracker()
def streaming():
    cap = cv2.VideoCapture("/dev/video0")
    if cap.isOpened() == True:
        print("camera webcam active . . .")
    else:
        print("camera webcam deactiave . . .")
    while cap.isOpened():
        ret, frame = cap.read()
        try:
            results = Detector(frame)
            data = ct.Update(results)
            for object in results:
                box = BBOX(object)
            Draw(frame, box)
            cv2.imshow("webcam", frame)
            if cv2.waitKey(1) == 27:
                break
        except:
            cap = cv2.VideoCapture(0)