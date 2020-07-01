from points4 import Points4
import numpy as np
import cv2
class perspective:
    def __init__(self,point41, point42):

        p1 = point41.get_p1()
        p2 = point41.get_p2()
        p3 = point41.get_p3()
        p4 = point41.get_p4()
        self.pst1 = np.float32([p1,p2,p3,p4])

        p1 = point42.get_p1()
        p2 = point42.get_p2()
        p3 = point42.get_p3()
        p4 = point42.get_p4()
        self.pst2 = np.float32([p1, p2, p3, p4])

        self.M = cv2.getPerspectiveTransform(self.pst1, self.pst2)
        #print(self.M)

    def warpImage(self,img):
        res = cv2.warpPerspective(img, self.M, (1100, 1100))

        return res

    def warpPoint(self, x, y):

        h11 = self.M[0][0]
        h12 = self.M[0][1]
        h13 = self.M[0][2]
        h21 = self.M[1][0]
        h22 = self.M[1][1]
        h23 = self.M[1][2]
        h31 = self.M[2][0]
        h32 = self.M[2][1]
        h33 = self.M[2][2]

        mom = h31*x + h32*y + h33
        xp = (h11*x + h12*y + h13) / mom
        yp = (h21*x + h22*y + h23) / mom

        return xp, yp

    def warpPoints4(self, points4):

        p1 = points4.get_p1()
        x1, y1 = self.warpPoint(p1[0], p1[1])

        p2 = points4.get_p2()
        x2, y2 = self.warpPoint(p2[0], p2[1])

        p3 = points4.get_p3()
        x3, y3 = self.warpPoint(p3[0], p3[1])

        p4 = points4.get_p4()
        x4, y4 = self.warpPoint(p4[0], p4[1])

        res = Points4(x1=x1, y1=y1,
                      x2=x2, y2=y2,
                      x3=x3, y3=y3,
                      x4=x4, y4=y4)

        return res


p1 = Points4(232,214,538,214,736,394,44,393)
p2 = Points4(210,210,800,210,800,800,210,800)

pers = perspective(p1,p2)

P = Points4(300,300,
            400,300,
            400,400,
            300,400)

PP = pers.warpPoints4(P)

PP.printPoints()