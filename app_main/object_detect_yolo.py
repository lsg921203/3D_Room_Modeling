import numpy as np
import time
import cv2
import os
from app_main.points4 import Points4


# 아래있는거 전부 클래스로 변환처리

class object_detection:
    def __init__(self):

        self.yolo = 'yolo-coco'
        self.confi = 0.5
        self.threshold = 0.3

        labelsPath = os.path.sep.join([self.yolo, "coco.names"])
        self.LABELS = open(labelsPath).read().strip().split("\n")
        np.random.seed(42)
        self.COLORS = np.random.randint(0, 255, size=(len(self.LABELS), 3),
                                        dtype="uint8")

        weightsPath = os.path.sep.join([self.yolo, "yolov3.weights"])
        configPath = os.path.sep.join([self.yolo, "yolov3.cfg"])

        print("[INFO] loading YOLO from disk...")
        self.net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)

        self.ln = self.net.getLayerNames()
        self.ln = [self.ln[i[0] - 1] for i in self.net.getUnconnectedOutLayers()]

    def detect(self, file_name):
        self.image = cv2.imread(file_name)
        (self.H, self.W) = self.image.shape[:2]
        self.blob = cv2.dnn.blobFromImage(self.image, 1 / 255.0, (416, 416),
                                          swapRB=True, crop=False)
        self.net.setInput(self.blob)
        start = time.time()
        self.layerOutputs = self.net.forward(self.ln)  # 학습내용을 기반으로 이미지 판단
        end = time.time()

        ### 여기까지 진행

        print("[INFO] YOLO took {:.6f} seconds".format(end - start))

        self.boxes = []
        self.confidences = []
        self.classIDs = []
        self.points = []

        for output in self.layerOutputs:
            # loop over each of the detections
            for detection in output:
                # extract the class ID and confidence (i.e., probability) of
                # the current object detection
                scores = detection[5:]
                classID = np.argmax(scores)  # classID는 int
                confidence = scores[classID]

                # filter out weak predictions by ensuring the detected
                # probability is greater than the minimum probability
                if confidence > self.confi:
                    #print(self.LABELS[classID])
                    # scale the bounding box coordinates back relative to the
                    # size of the image, keeping in mind that YOLO actually
                    # returns the center (x, y)-coordinates of the bounding
                    # box followed by the boxes' width and height
                    box = detection[0:4] * np.array([self.W, self.H, self.W, self.H])
                    (centerX, centerY, width, height) = box.astype("int")
                    x = int(centerX - (width / 2))
                    y = int(centerY - (height / 2))

                    self.points.append(Points4(x1=x,
                                               y1=y,
                                               x2=x + int(width),
                                               y2=y,
                                               x3=x + int(width),
                                               y3=y + int(height),
                                               x4=x,
                                               y4=y + int(height)))

                    # use the center (x, y)-coordinates to derive the top and
                    # and left corner of the bounding box


                    # update our list of bounding box coordinates, confidences,
                    # and class IDs
                    self.boxes.append([x, y, int(width), int(height)])
                    self.confidences.append(float(confidence))
                    self.classIDs.append(classID)
        self.idxs = cv2.dnn.NMSBoxes(self.boxes, self.confidences, self.confi, self.threshold)

        # ensure at least one detection exists
        if len(self.idxs) > 0:
            # loop over the indexes we are keeping
            for i in self.idxs.flatten():
                # extract the bounding box coordinates
                (x, y) = (self.boxes[i][0], self.boxes[i][1])
                (w, h) = (self.boxes[i][2], self.boxes[i][3])

                # draw a bounding box rectangle and label on the image
                color = [int(c) for c in self.COLORS[self.classIDs[i]]]
                # cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
                cv2.line(self.image, (x, y + h), (x + w, y + h), color, 2)
                text = "{}: {:.4f}".format(self.LABELS[self.classIDs[i]], self.confidences[i])
                cv2.putText(self.image, text, (x, y + h - 5), cv2.FONT_HERSHEY_SIMPLEX,
                            0.5, color, 2)
        # p1 = Points4(232, 214, 538, 214, 736, 394, 44, 393)
        # p2 = Points4(210, 210, 800, 210, 800, 800, 210, 800)

        # pers = perspective(p1, p2)
        # self.image = pers.warpImage(self.image)
        # show the output image
        #cv2.imshow("Image", self.image)
        #cv2.waitKey(0)

    def get_object_info(self):
        # 객체의 위치정보, 이름 반환
        object_names = []
        for i in self.classIDs:
            object_names.append(self.LABELS[i])

        return self.points, object_names


#od = object_detection()
#od.detect("images/room1.jpg")
