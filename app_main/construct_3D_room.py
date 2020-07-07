from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot
import math
import numpy as np

class const_3D_room:
    #방안에 3D 모형을 배치하고 보여주는 클래스

    def __init__(self):
        self.figure = pyplot.figure()
        self.axes = mplot3d.Axes3D(self.figure)

        self.your_mesh = None
        self.meshes = []

    def add_object(self,name,size,x,y,angle):
        # 추가될 객체의 종류를 파악하여 해당 종류의 3D 객체 파일을 염
        file_name=""
        original_size_x = 0
        original_size_y = 0
        if name == "bed":
            file_name = '../stl_files/bed1.stl'
            original_size_x = 100
            original_size_y = 200
        elif name == "chair":
            file_name = '../stl_files/chair1.stl'
            original_size_x = 40
            original_size_y = 40
        elif name == "sofa":
            file_name = '../stl_files/sofa1.stl'
            original_size_x = 200
            original_size_y = 50
        elif name == "tvmonitor":
            file_name = '../stl_files/TV.stl'
            original_size_x = 120
            original_size_y = 10
        elif name == "person":
            file_name = '../stl_files/cookie.stl'
            original_size_x = 60
            original_size_y = 30
        elif name == "car":
            file_name = '../stl_files/car.stl'
            original_size_x = 60
            original_size_y = 30
        else:
            return False

        # 객체를 해당위치에 배치후 3D 객체 리스트와 전체 모델에 추가
        rate = 1.5 #size / original_size_x

        self.your_mesh = mesh.Mesh.from_file(file_name)

        self.your_mesh.rotate([0.0, 0.0, 1.0], math.radians(angle), [original_size_x / 2, original_size_y / 2,0])

        self.your_mesh.x *= rate
        self.your_mesh.y *= rate
        self.your_mesh.z *= rate

        self.your_mesh.x += x
        self.your_mesh.y += y

        self.axes.add_collection3d(mplot3d.art3d.Poly3DCollection(self.your_mesh.vectors))

        self.meshes.append(mesh.Mesh(self.your_mesh.data.copy()))
        return True


    def show(self):
        # 지금까지 쌓인 객체들을 모두 보여줌
        scale = np.concatenate([m.points for m in self.meshes]).flatten('K')
        self.axes.auto_scale_xyz(scale, scale, scale)
        pyplot.show()


