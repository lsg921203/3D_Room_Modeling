import numpy as np
import time
import cv2
import os
from points4 import Points4
from perspectiveTransform import perspective
# 아래있는거 전부 클래스로 변환처리

class object_detection:
	def __init__(self):

		self.yolo = 'yolo-coco'
		self.confi = 0.5
		self.threshold = 0.3

		labelsPath = os.path.sep.join([yolo, "coco.names"])
		self.LABELS = open(labelsPath).read().strip().split("\n")
		np.random.seed(42)
		self.COLORS = np.random.randint(0, 255, size=(len(LABELS), 3),
								   dtype="uint8")

		weightsPath = os.path.sep.join([yolo, "yolov3.weights"])
		configPath = os.path.sep.join([yolo, "yolov3.cfg"])

		print("[INFO] loading YOLO from disk...")
		self.net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)

		self.ln = self.net.getLayerNames()
		self.ln = [self.ln[i[0] - 1] for i in self.net.getUnconnectedOutLayers()]

	def detect(self,file_name):
		self.image = cv2.imread(file_name)
		(self.H, self.W) = self.image.shape[:2]
		self.blob = cv2.dnn.blobFromImage(self.image, 1 / 255.0, (416, 416),
									 swapRB=True, crop=False)
		self.net.setInput(self.blob)
		start = time.time()
		self.layerOutputs = net.forward(ln)  # 학습내용을 기반으로 이미지 판단
		end = time.time()
		
		### 여기까지 진행


#처리할 이미지 경로
image = 'images/room1.jpg'
#다양한 정보가 저장된 폴더 경로
yolo = 'yolo-coco'
#정확도 임계값
confi = 0.5

threshold = 0.3

labelsPath = os.path.sep.join([yolo, "coco.names"])
LABELS = open(labelsPath).read().strip().split("\n")

# 각 사물 별 박스 색 생성
np.random.seed(42)
COLORS = np.random.randint(0, 255, size=(len(LABELS), 3),
	dtype="uint8")

# 디텍트 설정 파일 로드
weightsPath = os.path.sep.join([yolo, "yolov3.weights"])
configPath = os.path.sep.join([yolo, "yolov3.cfg"])

# load our YOLO object detector trained on COCO dataset (80 classes)
print("[INFO] loading YOLO from disk...")
net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)

# load our input image and grab its spatial dimensions
image = cv2.imread(image)
(H, W) = image.shape[:2]

# determine only the *output* layer names that we need from YOLO
ln = net.getLayerNames()
ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]

# construct a blob from the input image and then perform a forward
# pass of the YOLO object detector, giving us our bounding boxes and
# associated probabilities
#opencv에서 사용했던 이미지를 신경망에서 사용할 수 있는 blob의 형태로 변환
blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416),
	swapRB=True, crop=False)
net.setInput(blob)
start = time.time()
layerOutputs = net.forward(ln) #학습내용을 기반으로 이미지 판단
end = time.time()

# show timing information on YOLO
print("[INFO] YOLO took {:.6f} seconds".format(end - start))

# initialize our lists of detected bounding boxes, confidences, and
# class IDs, respectively
boxes = []
confidences = []
classIDs = []
points = []
# loop over each of the layer outputs
for output in layerOutputs:
	# loop over each of the detections
	for detection in output:
		# extract the class ID and confidence (i.e., probability) of
		# the current object detection
		scores = detection[5:]
		classID = np.argmax(scores)# classID는 int
		confidence = scores[classID]

		# filter out weak predictions by ensuring the detected
		# probability is greater than the minimum probability
		if confidence > confi:
			print(LABELS[classID])
			# scale the bounding box coordinates back relative to the
			# size of the image, keeping in mind that YOLO actually
			# returns the center (x, y)-coordinates of the bounding
			# box followed by the boxes' width and height
			box = detection[0:4] * np.array([W, H, W, H])
			(centerX, centerY, width, height) = box.astype("int")
			points.append(Points4(x1=centerX,
								  y1=centerY,
								  x2=centerX + width,
								  y2=centerY,
								  x3=centerX + width,
								  y3=centerY + height,
								  x4=centerX,
								  y4=centerY + height))


			# use the center (x, y)-coordinates to derive the top and
			# and left corner of the bounding box
			x = int(centerX - (width / 2))
			y = int(centerY - (height / 2))

			# update our list of bounding box coordinates, confidences,
			# and class IDs
			boxes.append([x, y, int(width), int(height)])
			confidences.append(float(confidence))
			classIDs.append(classID)

p1 = Points4(232,214,538,214,736,394,44,393)
p2 = Points4(210,210,800,210,800,800,210,800)

pers = perspective(p1,p2)



# apply non-maxima suppression to suppress weak, overlapping bounding
# boxes
idxs = cv2.dnn.NMSBoxes(boxes, confidences, confi,threshold)

# ensure at least one detection exists
if len(idxs) > 0:
	# loop over the indexes we are keeping
	for i in idxs.flatten():
		# extract the bounding box coordinates
		(x, y) = (boxes[i][0], boxes[i][1])
		(w, h) = (boxes[i][2], boxes[i][3])

		# draw a bounding box rectangle and label on the image
		color = [int(c) for c in COLORS[classIDs[i]]]
		#cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
		cv2.line(image,(x,y+h),(x+w, y+h),color, 2)
		text = "{}: {:.4f}".format(LABELS[classIDs[i]], confidences[i])
		cv2.putText(image, text, (x, y+h - 5), cv2.FONT_HERSHEY_SIMPLEX,
			0.5, color, 2)

image = pers.warpImage(image)

# show the output image
cv2.imshow("Image", image)
cv2.waitKey(0)
