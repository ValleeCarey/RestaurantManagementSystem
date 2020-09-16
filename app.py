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

        #----Info Food -------

        self.Label1 = tk.Label(master=top, text="Restaurant Management System", background="#354e71", font=font11, foreground="#f2a343")
        self.Label1.place(relx= 0.268, rely= 0.02, height=51, width=507)

        localtime1 = Label(master=top, text=localtime, background="#354e71", font=font16, fg="steel blue")
        localtime1.place(relx= 0.420, rely= 0.12)

        #----Label Food --------
        self.Label12= tk.Label(master=top, text="Order Num : ", foreground="#bac8bd", font=font12, background="#354e71")
        self.Label12.place(relx=0.054, rely=0.25)

        self.Label12= tk.Label(master=top, text="Fried Potato : ", foreground="#bac8bd", font=font12, background="#354e71")
        self.Label12.place(relx=0.049, rely=0.32)

        self.Label12= tk.Label(master=top, text="Chk Burger : ", foreground="#bac8bd", font=font12, background="#354e71")
        self.Label12.place(relx=0.053, rely=0.4)

        self.Label12= tk.Label(master=top, text="Big King : ", foreground="#bac8bd", font=font12, background="#354e71")
        self.Label12.place(relx=0.068, rely=0.48)

        self.Label12= tk.Label(master=top, text="Chk Royale : ", foreground="#bac8bd", font=font12, background="#354e71")
        self.Label12.place(relx=0.053, rely=0.56)

        self.Label12= tk.Label(master=top, text="Veg Salad : ", foreground="#bac8bd", font=font12, background="#354e71")
        self.Label12.place(relx=0.060, rely=0.64)

        self.Label12= tk.Label(master=top, text="Drinks : ", foreground="#00ff00", font=font12, background="#354e71")
        self.Label12.place(relx=0.078, rely=0.72)

        #---- Entry Food ------

        self.entry1 = tk.Entry(master=top, background="#d9d9d9", foreground="#c60000",selectbackground="#f2a343", font=font13)
        self.entry1.place(relx=0.14, rely=0.25)

        self.entry1 = tk.Entry(master=top, background="#d9d9d9", foreground="#c60000",selectbackground="#f2a343", font=font13)
        self.entry1.place(relx=0.14, rely=0.33)

        self.entry1 = tk.Entry(master=top, background="#d9d9d9", foreground="#c60000",selectbackground="#f2a343", font=font13)
        self.entry1.place(relx=0.14, rely=0.41)

        self.entry1 = tk.Entry(master=top, background="#d9d9d9", foreground="#c60000",selectbackground="#f2a343", font=font13)
        self.entry1.place(relx=0.14, rely=0.49)

        self.entry1 = tk.Entry(master=top, background="#d9d9d9", foreground="#c60000",selectbackground="#f2a343", font=font13)
        self.entry1.place(relx=0.14, rely=0.57)

        self.entry1 = tk.Entry(master=top, background="#d9d9d9", foreground="#c60000",selectbackground="#f2a343", font=font13)
        self.entry1.place(relx=0.14, rely=0.65)

        self.entry1 = tk.Entry(master=top, background="#d9d9d9", foreground="#c60000",selectbackground="#f2a343", font=font13)
        self.entry1.place(relx=0.14, rely=0.73)

        #------Calculator -------

        self.entry1 = tk.Entry(master=top, background="#d9d9d9", foreground="#c60000",selectbackground="#f2a343", font=font13)
        self.entry1.place(relx=0.705, rely=0.24, height=35, relwidth= 0.267)

        self.Button1 = tk.Button(master=top, text='''7''', background='#122c63', font=font14, foreground='#f2a343', borderwidth='0')
        self.Button1.place(relx=0.705, rely=0.34, height=44, width=67)

        self.Button1 = tk.Button(master=top, text='''8''', background='#122c63', font=font14, foreground='#f2a343', borderwidth='0')
        self.Button1.place(relx=0.780, rely=0.34, height=44, width=67)

        self.Button1 = tk.Button(master=top, text='''9''', background='#122c63', font=font14, foreground='#f2a343', borderwidth='0')
        self.Button1.place(relx=0.856, rely=0.34, height=44, width=67)

        self.Button1 = tk.Button(master=top, text='''/''', background='#122c63', font=font14, foreground='#f2a343', borderwidth='0')
        self.Button1.place(relx=0.934, rely=0.34, height=44, width=37)

        self.Button1 = tk.Button(master=top, text='''4''', background='#122c63', font=font14, foreground='#f2a343', borderwidth='0')
        self.Button1.place(relx=0.705, rely=0.44, height=44, width=67)

        self.Button1 = tk.Button(master=top, text='''5''', background='#122c63', font=font14, foreground='#f2a343', borderwidth='0')
        self.Button1.place(relx=0.780, rely=0.44, height=44, width=67)

        self.Button1 = tk.Button(master=top, text='''6''', background='#122c63', font=font14, foreground='#f2a343', borderwidth='0')
        self.Button1.place(relx=0.856, rely=0.44, height=44, width=67)

        self.Button1 = tk.Button(master=top, text='''*''', background='#122c63', font=font14, foreground='#f2a343', borderwidth='0')
        self.Button1.place(relx=0.934, rely=0.44, height=44, width=37)





root = tk.Tk()
myGui = App1(root)
root.mainloop()