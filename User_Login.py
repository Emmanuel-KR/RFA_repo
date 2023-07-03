import sqlite3
from tkinter import *
from PIL import ImageTk, Image
import tkinter.messagebox
import Sqlite3_Backend
import os

iconn = sqlite3.connect("Users.db")
yc = iconn.cursor()
yc.execute("""CREATE TABLE IF NOT EXISTS cred(
Username TEXT NOT NULL UNIQUE,
Password TEXT NOT NULL UNIQUE
)""")
iconn.commit()
iconn.close()


class UserLogin:
    def __init__(self, root4):
        self.Username = StringVar()
        self.Password = StringVar()

        self.root4 = root4
        self.root4.title("User Login")
        self.root4.geometry("1170x550+100-100")
        self.root4.config(bg='grey')

        self.mainframe = Frame(self.root4, bg='light green')
        self.mainframe.grid(pady=10, padx=10)

        self.lblTitle = Label(self.mainframe, text='RFA System User Login', font=('arial', 50, 'bold'),
                              bg='light green', fg='black')
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=40)

        self.btnLogout = Button(self.mainframe, text='Logout', font=('arial', 10, 'bold'), width=10,
                               command=self.logout_system, state=DISABLED)
        self.btnLogout.place(relx=0.015, rely=0.040)

        # ===============================================================
        self.LoginFrame1 = LabelFrame(self.mainframe, width=1300, height=550, font=('arial', 20, 'bold'),
                                      bg='light green', bd=0)
        self.LoginFrame1.grid(row=1, column=0)

        self.LoginFrame2 = LabelFrame(self.mainframe, width=950, height=550, font=('arial', 20, 'bold'),
                                      bg='light green', bd=0)
        self.LoginFrame2.grid(row=2, column=0)

        self.ButtonFrame = LabelFrame(self.mainframe, bd=1)
        self.ButtonFrame.grid(row=3, column=0)

        # ================================Label and Entry===============================
        self.lblUsername = Label(self.LoginFrame1, text='Username', font=('arial', 20, 'bold'), bd=22, bg='light green',
                                 fg='Cornsilk')
        self.lblUsername.grid(row=0, column=0)
        self.txtUsername = Entry(self.LoginFrame1, font=('arial', 20, 'bold'), bd=7, width=20,
                                 textvariable=self.Username)
        self.txtUsername.grid(row=0, column=1, padx=119)

        self.lblPassword = Label(self.LoginFrame1, text='Password', font=('arial', 20, 'bold'), bd=22, bg='light green',
                                 fg='Cornsilk')
        self.lblPassword.grid(row=1, column=0)
        self.txtPassword = Entry(self.LoginFrame1, font=('arial', 20, 'bold'), show='*', bd=7, width=20,
                                 textvariable=self.Password)
        self.txtPassword.grid(row=1, column=1, padx=30, columnspan=2)

        # ================================Buttons===============================

        self.btnLogin = Button(self.LoginFrame2, text='Login', font=('arial', 20, 'bold'), width=17,
                               command=self.login_system)
        self.btnLogin.grid(row=3, column=0, pady=20, padx=8)

        self.btnReset = Button(self.LoginFrame2, text='Reset', font=('arial', 20, 'bold'), width=17, command=self.reset)
        self.btnReset.grid(row=3, column=1, pady=20, padx=8)

        self.btnExit = Button(self.LoginFrame2, text='Exit Window', font=('arial', 20, 'bold'), width=17,
                              command=self.exitWin)
        self.btnExit.grid(row=3, column=2, pady=20, padx=8)

        # ===============================================================================
        self.btnreg = Button(self.ButtonFrame, text='Register/Update\nFarmer Details', font=('arial', 15, 'bold'),
                             width=17, state=DISABLED, command=self.run_register)
        self.btnreg.grid(row=0, column=0, pady=20, padx=8)

        self.btndel = Button(self.ButtonFrame, text='Produce Delivery/\nDelivery Reports', font=('arial', 15, 'bold'),
                             width=17, state=DISABLED, command=self.delivery)
        self.btndel.grid(row=0, column=1, pady=20, padx=8)

        self.btnsta = Button(self.ButtonFrame, text='Farmer Status', font=('arial', 15, 'bold'), width=17, height=2,
                             state=DISABLED, command=self.Farmer_Status)
        self.btnsta.grid(row=0, column=2, pady=20, padx=8)

        self.btnser = Button(self.ButtonFrame, text='Service Provision', font=('arial', 15, 'bold'), width=17, height=2,
                             state=DISABLED, command=self.Service_Provision)
        self.btnser.grid(row=0, column=3, pady=20, padx=8)

        self.btnpay = Button(self.ButtonFrame, text='Payment', font=('arial', 15, 'bold'), width=17, height=2,
                             state=DISABLED, command=self.Payment_Module)
        self.btnpay.grid(row=0, column=4, pady=20, padx=8)

    def login_system(self):
        conn = sqlite3.connect("Users.db")
        c = conn.cursor()
        c.execute("SELECT * FROM cred WHERE Username = ? OR Password = ?", (self.Username.get(), self.Password.get()))
        details = c.fetchall()
        conn.close()
        if details == []:
            tkinter.messagebox.showinfo("User doesn't exist", "Contact System Admin")

        elif (details[0][0] == self.Username.get() and details[0][1] != self.Password.get()) or \
                (details[0][0] != self.Username.get() and details[0][1] == self.Password.get()):
            tkinter.messagebox.showerror("Wrong Credentials", "Try Again")

        elif (details[0][0] == self.Username.get() and details[0][1] == self.Password.get()):
            self.btnLogout.config(state=NORMAL)
            self.btnreg.config(state=NORMAL)
            self.btndel.config(state=NORMAL)
            self.btnsta.config(state=NORMAL)
            self.btnser.config(state=NORMAL)
            self.btnpay.config(state=NORMAL)
            self.reset()
            self.btnLogin.config(state=DISABLED)
            self.btnReset.config(state=DISABLED)

    def reset(self):
        self.Username.set("")
        self.Password.set("")
        self.txtUsername.focus()

    def logout_system(self):
        self.btnLogout.config(state=DISABLED)
        self.btnreg.config(state=DISABLED)
        self.btndel.config(state=DISABLED)
        self.btnsta.config(state=DISABLED)
        self.btnser.config(state=DISABLED)
        self.btnpay.config(state=DISABLED)
        self.reset()
        self.btnLogin.config(state=NORMAL)
        self.btnReset.config(state=NORMAL)

    def exitWin(self):
        exitwin = tkinter.messagebox.askyesno("RFA Login", "Confirm you want to exit")
        if exitwin > 0:
            self.root4.destroy()
        else:
            return

    def run_register(self):
        self.root4.withdraw()
        os.system('python Register_Update_Module.py')
        self.root4.deiconify()

    def delivery(self):
        self.root4.withdraw()
        os.system('python Produce_Delivery.py')
        self.root4.deiconify()

    def Farmer_Status(self):
        self.root4.withdraw()
        os.system('python Farmer_Status.py')
        self.root4.deiconify()

    def Service_Provision(self):
        self.root4.withdraw()
        os.system('python Service_Provision.py')
        self.root4.deiconify()

    def Payment_Module(self):
        self.root4.withdraw()
        os.system('python Payment_Module.py')
        self.root4.deiconify()


root = Tk()
runx = UserLogin(root)
root.mainloop()
