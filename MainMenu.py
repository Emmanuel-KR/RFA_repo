import sqlite3
from tkinter import *
from PIL import ImageTk, Image
import tkinter.messagebox
import Sqlite3_Backend
import os

menu = Tk()
menu.title("The Main Menu")
menu.geometry("1366x768")
menu.config(bg="grey")


class MainMenu:
    def __init__(self, top=None):
        top.geometry("1170x550+100-100")
        top.title("Main Menu")

        self.label = Label(menu)
        self.label.place(relx=0, rely=0, width=1170, height=550)
        self.img = PhotoImage(file="./resources/Background.png")
        self.label.configure(image=self.img)

        registerimg = PhotoImage(file=r"./resources/Register.png")
        self.registerbtn = Button(menu, image=registerimg, font=('arial', 20, 'bold'), bd=0, highlightthickness=0,
                                cursor='hand2')
        self.registerbtn.place(relx=0.135, rely=0.250)
        self.registerbtn.photo = registerimg

        deliveryimg = PhotoImage(file=r"./resources/Delivery1.png")
        self.deliverybtn = Button(menu, image=deliveryimg, font=('arial', 20, 'bold'), bd=0, highlightthickness=0,
                                  cursor='hand2')
        self.deliverybtn.place(relx=0.45, rely=0.250)
        self.deliverybtn.photo = deliveryimg


page1 = MainMenu(menu)
menu.mainloop()