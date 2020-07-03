from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot
import math
import numpy as np

class const_3D_room:
    def __init__(self):
        self.figure = pyplot.figure()
        self.axes = mplot3d.Axes3D(self.figure)

        self.your_mesh = None
        self.meshes = []

    def add_object(self,name,size,x,y,angle):
        file_name=""
        original_size_x = 0
        original_size_y = 0
        if name == "bed":
            file_name = 'stl_files/bed1.stl'
            original_size_x = 100
            original_size_y = 200
        elif name == "chair":
            file_name = 'stl_files/chair1.stl'
            original_size_x = 40
            original_size_y = 40
        elif name == "sofa":
            file_name = 'stl_files/sofa1.stl'
            original_size_x = 200
            original_size_y = 50
        elif name == "tvmonitor":
            file_name = 'stl_files/TV.stl'
            original_size_x = 120
            original_size_y = 0
        else:
            return False

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

        scale = np.concatenate([m.points for m in self.meshes]).flatten('K')
        self.axes.auto_scale_xyz(scale, scale, scale)
        pyplot.show()


#test = const_3D_room()
#test.add_object("bed",40,10,60,0)
#test.add_object("bed",60,10,-60,0)
#test.show()
