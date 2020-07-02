from object_detect_yolo import object_detection
from perspectiveTransform import perspective
from points4 import Points4
from warping_room import Warping_room
from construct_3D_room import const_3D_room
import numpy as np
import cv2
import math

def main(dbug):

    file_name = "images/room1.jpg"
    od = object_detection()
    od.detect(file_name)

    warping = Warping_room()
    image = warping.warping_img(file_name)

    model_house = const_3D_room()

    if dbug:
        cv2.rectangle(image,(400,400),(1100,1100),(0,0,255),thickness=5)


    points, names = od.get_object_info()
    points2 = warping.warping_points(points)
    #points2 = points

    if dbug:
        for i in range(len(points2)):
            #print(names[i])
            if names[i] == "bed" or names[i] == "sofa" or names[i] == "chair" :#or names[i] == "tvmonitor"
                cv2.line(image, (points2[i].x3,points2[i].y3),(points2[i].x4,points2[i].y4),(255,255,0),5)

    for i in range(len(points2)):
        #print(names[i])
        if names[i] == "bed" or names[i] == "sofa" or names[i] == "chair":   #or names[i] == "tvmonitor"
            centerX = (int)((points2[i].x3 + points2[i].x4)/2)
            centerY = (int)((points2[i].y3 + points2[i].y4)/2)
            centerX = (centerX)
            centerY = (1500 - centerY)
            length = math.sqrt(((points2[i].x3 - points2[i].x4)**2) + ((points2[i].y3 - points2[i].y4)**2)) / 2
            model_house.add_object(name=names[i],
                                   size=length,
                                   x=centerX,
                                   y=centerY,
                                   angle=0)


            if dbug:
                print(names[i],":", centerX,",", centerY)
                cv2.line(image, (points2[i].x3, points2[i].y3), (points2[i].x4, points2[i].y4), (255, 255, 0), 5)
    model_house.show()
    if dbug:
        image = cv2.resize(image, dsize=None, fx=0.5, fy=0.5)
        cv2.imshow("image", image)
        cv2.waitKey(0)

main(True)