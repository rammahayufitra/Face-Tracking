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
            for val in data:
                cv2.circle(frame,(box.xywh[0]+int(box.xywh[2]/2),box.xywh[1]+int(box.xywh[3]/2)),5,[0,0,255],-1)
                cv2.putText(frame, str(val[3]),(box.xywh[0]+int(box.xywh[2]/2),box.xywh[1]+int(box.xywh[3]/2)), cv2.FONT_HERSHEY_SIMPLEX , 1, [0,0,255], 4, cv2.LINE_AA) 
                Draw(frame, box)
            cv2.imshow("webcam", frame)
            if cv2.waitKey(1) == 27:
                break
        except:
            cap = cv2.VideoCapture(0)