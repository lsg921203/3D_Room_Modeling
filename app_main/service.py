#이 함수 안에 기능을 구현하시오
#기능구현 클래스를 따로 만들고 그 객체를 생성하여 실행하는 코드를 넣으면 ok
from app_main.object_detect_yolo import object_detection
from app_main.warping_room import Warping_room
from app_main.construct_3D_room import const_3D_room
import cv2
import math
from matplotlib import pyplot

class service:
    def __init__(self):
        pass
    def const_3D(self,app,file_name,dbug):
        od = object_detection()
        od.detect(file_name)

        warping = Warping_room()
        image = warping.warping_img(file_name)

        model_house = const_3D_room()

        if dbug:
            cv2.rectangle(image, (400, 400), (1100, 1100), (0, 0, 255), thickness=5)

        points, names = od.get_object_info()
        points2 = warping.warping_points(points)

        for i in range(len(points2)):

            if names[i] == "bed" or \
                    names[i] == "sofa" or \
                    names[i] == "chair" or \
                    names[i] == "tvmonitor" or \
                    names[i] == "person" or \
                    names[i] == "car":  #
                centerX = (int)((points2[i].x3 + points2[i].x4) / 2)
                centerY = (int)((points2[i].y3 + points2[i].y4) / 2)
                centerX = (centerX)
                centerY = (1500 - centerY)
                length = math.sqrt(((points2[i].x3 - points2[i].x4) ** 2) + ((points2[i].y3 - points2[i].y4) ** 2)) / 2
                model_house.add_object(name=names[i],
                                       size=length,
                                       x=centerX,
                                       y=centerY,
                                       angle=0)

                if dbug:
                    print(names[i], ":", centerX, ",", centerY)
                    cv2.line(image, (points2[i].x3, points2[i].y3), (points2[i].x4, points2[i].y4), (255, 255, 0), 5)

        app.change_img(image)

        model_house.show()

        pyplot.close()





