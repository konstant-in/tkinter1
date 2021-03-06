# for python 3.x use 'tkinter' rather than 'Tkinter'
import tkinter as tk
import time


class App():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('200x20')
        self.label = tk.Label(text="")
        self.label.pack()
        self.update_clock()
        self.root.mainloop()

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        self.root.after(1000, self.update_clock)


app = App()
