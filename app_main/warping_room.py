from app_main.perspectiveTransform import perspective
from app_main.points4 import Points4
import cv2
class Warping_room:
    def __init__(self):
        self.srcp4s = []
        self.dstp4s = []
        self.file_lists = []

        self.i = 0
        self.file_name = ""
        self.pers = None
        self.image = None

        self.srcp4s.append(Points4(450, 450, 1050, 450, 1050, 1050, 450, 1050))
        self.dstp4s.append(Points4(450, 450, 1050, 450, 1050, 1050, 450, 1050))
        self.file_lists.append('')

        self.srcp4s.append(Points4(232, 214, 538, 214, 736, 394, 44, 393))
        self.dstp4s.append(Points4(450, 450, 1050, 450, 1050, 1050, 450, 1050))
        self.file_lists.append('images/room1.jpg')

        self.srcp4s.append(Points4(312, 509, 821, 508, 1055, 753, 4, 753))
        self.dstp4s.append(Points4(450, 450, 1050, 450, 1050, 1050, 450, 1050))
        self.file_lists.append('images/room2.jpg')

        self.srcp4s.append(Points4(72, 294, 437, 227, 687, 323, -67, 716))
        self.dstp4s.append(Points4(450, 450, 1050, 450, 1050, 1050, 450, 1050))
        self.file_lists.append('images/room3.jpg')

        self.srcp4s.append(Points4(11, 425, 403, 271, 682, 313, 744, 1187))
        self.dstp4s.append(Points4(450, 450, 1050, 450, 1050, 1050, 450, 1050))
        self.file_lists.append('images/room4.jpg')

        self.srcp4s.append(Points4(262, 184, 441, 198, 756, 416, 69, 282))
        self.dstp4s.append(Points4(450, 450, 1050, 450, 1050, 1050, 450, 1050))
        self.file_lists.append('images/room5.jpg')

        self.srcp4s.append(Points4(311, 299, 727, 243, 1059, 396, 465, 553))
        self.dstp4s.append(Points4(450, 450, 1050, 450, 1050, 1050, 450, 1050))
        self.file_lists.append('images/soccer1.JPG')

        self.srcp4s.append(Points4(66, 272, 453, 244, 812, 289, 268, 383))
        self.dstp4s.append(Points4(450, 450, 1050, 450, 1050, 1050, 450, 1050))
        self.file_lists.append('images/crosswalk1.jpg')

        self.srcp4s.append(Points4(241, 109, 801, 262, 370, 426, -65, 165))
        self.dstp4s.append(Points4(250, 250, 1250, 250, 1250, 1250, 250, 1250))
        self.file_lists.append('images/crosswalk2.png')

        self.srcp4s.append(Points4(66, 263, 550, 150, 1097, 426, 222, 867))
        self.dstp4s.append(Points4(250, 250, 1250, 250, 1250, 1250, 250, 1250))
        self.file_lists.append('images/crosswalk3.jpg')

    def warping_img(self,filename):
        self.i = 0
        self.file_name = filename

        for fl in self.file_lists:
            if fl == filename:
                break
            else:
                self.i += 1

        if self.i >= len(self.file_lists):
            self.i = 0

        self.pers = perspective(self.srcp4s[self.i], self.dstp4s[self.i])

        self.image = cv2.imread(self.file_name)
        self.image = self.pers.warpImage(self.image)

        return self.image

    def warping_points(self, p4s):
        point4s = []
        for p4 in p4s:
            point4s.append(self.pers.warpPoints4(p4))

        return point4s