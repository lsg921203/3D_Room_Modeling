import tkinter as tk
import cv2
from PIL import Image
from PIL import ImageTk

class AppWindow(tk.Frame):#frame
    def __init__(self, master=None, size=None, path=None):
        super().__init__(master)
        self.master = master
        self.master.geometry(size)
        self.master.resizable(True, True)
        self.pack()#opencv frame
        self.sub_fr = None#frame
        self.src = None #tk의 label에 출력할 영상
        self.frame = None #tk의 영상을 출력할 레이블
        self.create_widgets(path)

    def make_img(self, path):
        src = cv2.imread(path)
        src = cv2.resize(src, (640, 400))
        img = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        self.src = ImageTk.PhotoImage(image=img)

    def create_widgets(self, path):
        self.make_img(path)
        self.frame = tk.Label(self.master, image=self.src)
        self.frame.pack()
        self.sub_fr = tk.Frame(self.master)#frame
        self.sub_fr.pack()

    def change_img(self, img):
        img = cv2.resize(res, (640, 400))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        self.src = ImageTk.PhotoImage(image=img)
        self.frame['image']=self.src