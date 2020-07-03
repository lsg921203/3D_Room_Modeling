import tkinter as tk
import cv2
from functools import partial
import threading


def btn1_clicked(app, event):
    app.image_idx -= 1
    if (app.image_idx < 0):
        app.image_idx = len(app.image_list) - 1
    image = cv2.imread(app.image_list[app.image_idx])
    app.change_img(image)


def btn2_clicked(app, event):
    app.image_idx += 1
    if (app.image_idx >= len(app.image_list)):
        app.image_idx = 0
    image = cv2.imread(app.image_list[app.image_idx])

    app.change_img(image)

def btn3_clicked(app, event):
    pass

def make(app, service):
    app.ent = tk.Entry(app.sub_fr, width=60)
    app.ent = tk.Entry(app.sub_fr, width=60)
    app.btn1 = tk.Button(app.sub_fr, width=10, font=60, text='prev')#next
    app.btn2 = tk.Button(app.sub_fr, width=10, font=60, text='next')#prev
    app.btn3 = tk.Button(app.sub_fr, width=10, font=60, text='3D')#3D

    app.ent.grid(row=0, column=0, columnspan=3)
    app.btn1.grid(row=1, column=0)
    app.btn2.grid(row=1, column=1)
    app.btn3.grid(row=1, column=2)

    #app.btn1['command'] = btn1_clicked
    app.btn1.bind('<Button-1>', partial(btn1_clicked, app))
    app.btn2.bind('<Button-1>', partial(btn2_clicked, app))
    app.btn3.bind('<Button-1>', partial(btn3_clicked, app))