from tkinter import *
import tkinter as tk 

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
        font12 = "Al-Aramco 12 bold "
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

        self.Button1 = tk.Button(master=top, text='''1''', background='#122c63', font=font14, foreground='#f2a343', borderwidth='0')
        self.Button1.place(relx=0.705, rely=0.54, height=44, width=67)

        self.Button1 = tk.Button(master=top, text='''2''', background='#122c63', font=font14, foreground='#f2a343', borderwidth='0')
        self.Button1.place(relx=0.780, rely=0.54, height=44, width=67)

        self.Button1 = tk.Button(master=top, text='''3''', background='#122c63', font=font14, foreground='#f2a343', borderwidth='0')
        self.Button1.place(relx=0.856, rely=0.54, height=44, width=67)

        self.Button1 = tk.Button(master=top, text='''-''', background='#122c63', font=font14, foreground='#f2a343', borderwidth='0')
        self.Button1.place(relx=0.934, rely=0.54, height=44, width=37)

        self.Button1 = tk.Button(master=top, text='''0''', background='#122c63', font=font14, foreground='#f2a343', borderwidth='0')
        self.Button1.place(relx=0.705, rely=0.64, height=35, width=147)

        self.Button1 = tk.Button(master=top, text='''.''', background='#122c63', font=font14, foreground='#f2a343', borderwidth='0')
        self.Button1.place(relx=0.856, rely=0.64, height=35, width=67)

        self.Button1 = tk.Button(master=top, text='''+''', background='#122c63', font=font14, foreground='#f2a343', borderwidth='0')
        self.Button1.place(relx=0.934, rely=0.64, height=35, width=37)

        self.Button1 = tk.Button(master=top, text='''=''', background='#f2a343', font=font14, foreground='#f2a343', borderwidth='0')
        self.Button1.place(relx=0.705, rely=0.72, height=34, width=272)

        #-----Cost ----------------
        self.Label12= tk.Label(master=top, text="Cost : ", foreground="#e16740", font=font12, background="#354e71")
        self.Label12.place(relx=0.35, rely=0.32)

        self.Label12= tk.Label(master=top, text="Service Charge : ", foreground="#bac8bd", font=font12, background="#354e71")
        self.Label12.place(relx=0.29, rely=0.4)

        self.Label12= tk.Label(master=top, text="Tax : ", foreground="#bac8bd", font=font12, background="#354e71")
        self.Label12.place(relx=0.36, rely=0.48)
        self.Label12= tk.Label(master=top, text="Subtotal : ", foreground="#bac8bd", font=font12, background="#354e71")
        self.Label12.place(relx=0.33, rely=0.56)

        self.Label12= tk.Label(master=top, text="Total : ", foreground="#bac8bd", font=font12, background="#354e71")
        self.Label12.place(relx=0.35, rely=0.64)

        #-----Entry Cost --------

        self.entry13 = tk.Entry(master=top, background="#d9d9d9", foreground="#c60000",selectbackground="#f2a343", font=font13)
        self.entry13.place(relx=0.40, rely=0.31, height=35, relwidth= 0.237)

        self.entry13 = tk.Entry(master=top, background="#d9d9d9", foreground="#c60000",selectbackground="#f2a343", font=font13)
        self.entry13.place(relx=0.40, rely=0.39, height=35, relwidth= 0.237)

        self.entry13 = tk.Entry(master=top, background="#d9d9d9", foreground="#c60000",selectbackground="#f2a343", font=font13)
        self.entry13.place(relx=0.40, rely=0.47, height=33, relwidth= 0.237)

        self.entry13 = tk.Entry(master=top, background="#d9d9d9", foreground="#c60000",selectbackground="#f2a343", font=font13)
        self.entry13.place(relx=0.40, rely=0.55, height=33, relwidth= 0.237)
        
        self.entry13 = tk.Entry(master=top, background="#d9d9d9", foreground="#c60000",selectbackground="#f2a343", font=font13)
        self.entry13.place(relx=0.40, rely=0.63, height=33, relwidth= 0.237)

        #----Control Button -----

        self.Button2 = tk.Button(master=top, text='''Price''', highlightbackground="#e16740", font=font16, command=list1)
        self.Button2.place(relx=0.039, rely=0.86, height=34, width=107)

        self.Button2 = tk.Button(master=top, text='''TOTAL''', highlightbackground="#e16740", font=font16,)
        self.Button2.place(relx=0.156, rely=0.86, height=34, width=107)

        self.Button2 = tk.Button(master=top, text='''RESET''', highlightbackground="#e16740", font=font16,)
        self.Button2.place(relx=0.272, rely=0.86, height=34, width=107)

        self.Button2 = tk.Button(master=top, text='''EXIT''', highlightbackground="#e16740", font=font16,)
        self.Button2.place(relx=0.389, rely=0.86, height=34, width=107)

def list1():
    price = Tk()
    price.geometry("300x250+350+200")
    price.title("Price List")
    price.configure(background="#031833")

    labelInfo = Label(price, text="ITEM", foreground="#bac8db", font="Al-Aramco 19 bold", background="#091833")
    labelInfo.grid(row=0 , column=0)

    labelInfo = Label(price, text="PRICE", foreground="#f28343", font="Al-Aramco 19 bold", background="#091833")
    labelInfo.grid(row=0 , column=1)

    labelInfo = Label(price, text="Fried Potato", foreground="#bac8db", font="Al-Aramco 19 bold", background="#091833")
    labelInfo.grid(row=1 , column=0)

    labelInfo = Label(price, text="30", foreground="#f28343", font="Al-Aramco 19 bold", background="#091833")
    labelInfo.grid(row=1 , column=1)

    labelInfo = Label(price, text="Chk Burger", foreground="#bac8db", font="Al-Aramco 19 bold", background="#091833")
    labelInfo.grid(row=2 , column=0)

    labelInfo = Label(price, text="30", foreground="#f28343", font="Al-Aramco 19 bold", background="#091833")
    labelInfo.grid(row=2 , column=1)

    labelInfo = Label(price, text="Big King", foreground="#bac8db", font="Al-Aramco 19 bold", background="#091833")
    labelInfo.grid(row=3 , column=0)

    labelInfo = Label(price, text="35", foreground="#f28343", font="Al-Aramco 19 bold", background="#091833")
    labelInfo.grid(row=3 , column=1)

    labelInfo = Label(price, text="Chk Royale", foreground="#bac8db", font="Al-Aramco 19 bold", background="#091833")
    labelInfo.grid(row=4 , column=0)

    labelInfo = Label(price, text="45", foreground="#f28343", font="Al-Aramco 19 bold", background="#091833")
    labelInfo.grid(row=4 , column=1)

    labelInfo = Label(price, text="Veg Salad", foreground="#bac8db", font="Al-Aramco 19 bold", background="#091833")
    labelInfo.grid(row=5 , column=0)

    labelInfo = Label(price, text="25", foreground="#f28343", font="Al-Aramco 19 bold", background="#091833")
    labelInfo.grid(row=5 , column=1)

    labelInfo = Label(price, text="Drinks", foreground="#bac8db", font="Al-Aramco 19 bold", background="#091833")
    labelInfo.grid(row=6 , column=0)

    labelInfo = Label(price, text="20", foreground="#f28343", font="Al-Aramco 19 bold", background="#091833")
    labelInfo.grid(row=6 , column=1)


root = tk.Tk()
myGui = App1(root)
root.mainloop()