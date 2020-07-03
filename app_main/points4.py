class Points4:
    def __init__(self,x1=None,y1=None,x2=None,y2=None,x3=None,y3=None,x4=None,y4=None):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4

    def get_p1(self):
        return [self.x1, self.y1]

    def get_p2(self):
        return [self.x2, self.y2]

    def get_p3(self):
        return [self.x3, self.y3]

    def get_p4(self):
        return [self.x4, self.y4]

    def set_p1(self,x,y):
        self.x1 = x
        self.y1 = y

    def set_p2(self,x,y):
        self.x2 = x
        self.y2 = y

    def set_p3(self,x,y):
        self.x3 = x
        self.y3 = y

    def set_p4(self,x,y):
        self.x4 = x
        self.y4 = y

    def printPoints(self):
        print("x1:" + str(self.x1))
        print("y1:" + str(self.y1))
        print("x2:" + str(self.x2))
        print("y2:" + str(self.y2))
        print("x3:" + str(self.x3))
        print("y3:" + str(self.y3))
        print("x4:" + str(self.x4))
        print("y4:" + str(self.y4))
