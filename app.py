import tkinter as tk 
from tkinter import Label, Button


class App1:
    def __init__(self, top):
        self.top = top 
        top.title("Restaurant Management")
        top.geometry("1028x500")
        top.configure(background="#354e71")

root = tk.Tk()
myGui = App1(root)
root.mainloop()