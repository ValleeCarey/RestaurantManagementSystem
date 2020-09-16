import tkinter as tk 
from tkinter import Label, Button
import time

localtime = time.asctime(time.localtime(time. time()))



class App1:
    def __init__(self, top):
        self.top = top 
        top.title("Restaurant Management")
        top.geometry("1028x500")
        top.configure(background="#354e71")

        font10 = "{Courier New} 10 normal"
        font11 = "{U.S. 101} 30 bold"
        font12 = "Al-Aramco 11 bold "
        font13 = "{Courier New} 10 bold "
        font14 = "{Segoe UI} 15 bold "
        font15 = "Arial 13 bold "
        font16 = "{Segoe UI} 13 bold"

        self.Label1 = tk.Label(master=top, text="Restaurant Management System", background="#354e71", font=font11, foreground="#f2a343")
        self.Label1.place(relx= 0.268, rely= 0.02, height=51, width=507)

        localtime1 = Label(master=top, text=localtime, background="#354e71", font=font16, fg="steel blue")
        localtime1.place(relx= 0.420, rely= 0.12)

root = tk.Tk()
myGui = App1(root)
root.mainloop()