import tkinter as tk
import app_main.main_ui as win
import app_main.make_widgets as mkw
import app_main.service as s



def main():
    img_path = '../images/room1.jpg'

    root = tk.Tk()
    app = win.AppWindow(root, '650x500+100+100', img_path)
    serv = s.service()
    mkw.make(app, s)

    app.mainloop()

main()