import tkinter as tk
import app_main.main_ui as win
import app_main.make_widgets as mkw
import app_main.service as s

def main():
    img_path = 'images/a.jpg'
    root = tk.Tk()
    app = win.AppWindow(root, '650x500+100+100', img_path)
    mkw.make(app)
    s.service() #ui 이벤트와 상관없이 수행해야하는 기능
    app.mainloop()
