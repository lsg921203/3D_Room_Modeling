import tkinter as tk
import app_main.main_ui as win
import app_main.make_widgets as mkw
import app_main.service as s
import os


def main():
    img_path = "images/"+os.listdir("images")[0]

    root = tk.Tk()
    app = win.AppWindow(root, '650x500+100+100', img_path)
    serv = s.service()
    mkw.make(app, serv)

    app.mainloop()


main()