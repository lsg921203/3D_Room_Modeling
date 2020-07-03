import tkinter as tk
import cv2
from functools import partial

def btn1_clicked(app, event):
    print(event)
    img = cv2.imread('img/b.jpg')
    app.change_img(img)

def btn2_clicked():
    print('btn2 clicked')

def btn3_clicked():
    print('btn3 clicked')

def make(app, service):
    app.ent = tk.Entry(app.sub_fr, width=60)
    app.ent = tk.Entry(app.sub_fr, width=60)
    app.btn1 = tk.Button(app.sub_fr, width=10, font=60, text='그림변경')
    app.btn2 = tk.Button(app.sub_fr, width=10, font=60, text='btn2')
    app.btn3 = tk.Button(app.sub_fr, width=10, font=60, text='btn3')

    app.ent.grid(row=0, column=0, columnspan=3)
    app.btn1.grid(row=1, column=0)
    app.btn2.grid(row=1, column=1)
    app.btn3.grid(row=1, column=2)

    #app.btn1['command'] = btn1_clicked
    app.btn1.bind('<Button-1>', partial(btn1_clicked, app))
    app.btn2['command'] = btn2_clicked
    app.btn3['command'] = btn3_clicked