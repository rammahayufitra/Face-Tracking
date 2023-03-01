import cv2 
from components.cascade import Cascade
from components.nms import NMS



def streaming():
    path = "./weights/cascade.xml"
    cd = Cascade(path)
    nms = NMS()
    cap = cv2.VideoCapture(0)
    if cap.isOpened() == True:
        print("camera webcam active . . .")
    else:
        print("camera webcam deactiave . . .")
    while cap.isOpened():
        ret, frame = cap.read()
        try:
            detection = cd.get_detections(frame)

            for val in detection:
                cv2.rectangle(frame,(val[0],val[1]),(val[0]+val[2],val[1]+val[3]),[0,255,0],1)
            
            detection_nms = nms.non_maximum_surpression(detection, THRESHOLD=0.1)
            for val in detection_nms:
                cv2.rectangle(frame,(val[0],val[1]),(val[0]+val[2],val[1]+val[3]),[0,255,0],1)
            

            cv2.imshow("webcam", frame)
            if cv2.waitKey(1) == 27:
                break
        except:
            print("HAHAHA")
            pass