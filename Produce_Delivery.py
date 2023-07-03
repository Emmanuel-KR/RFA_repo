from tkinter import *
import random
import string
import time
import datetime
import tkinter.messagebox
import Sqlite3_Backend


class Produce_delivery:
    def __init__(self, root14):
        self.var1 = IntVar()
        self.var2 = IntVar()
        self.var3 = IntVar()
        self.deliveryPrice = StringVar()
        self.deliveryRef = StringVar()
        self.deliveryDate = StringVar()
        self.surname = StringVar()
        self.uid = StringVar()
        self.weight = IntVar()
        self.TotalCash = StringVar()
        self.totalcash = DoubleVar()  # _____ The Value to be added to the database____
        self.vrepref = StringVar()
        self.vfuid = StringVar()
        self.vdate = StringVar()

        self.root14 = root14
        self.root14.geometry("1320x620+15-70")
        self.root14.config(bg='light green')
        self.root14.title("Produce Delivery and Reports")

        # _________ Frames ___________________________
        self.MainFrame = Frame(self.root14, bg='light green', bd=5, relief=RIDGE)
        self.MainFrame.pack()

        self.titleFrame = Frame(self.MainFrame, padx=54, pady=15, relief=RIDGE, bg='light green')
        self.titleFrame.grid(row=0, column=0, columnspan=2)

        self.delFrame = Frame(self.MainFrame, bd=3, padx=8, pady=6, relief=RIDGE, bg="powder blue")
        self.delFrame.grid(row=1, column=0, sticky=W)

        self.repFrame = Frame(self.MainFrame, bd=3, padx=8, pady=6, relief=RIDGE, bg="powder blue")
        self.repFrame.grid(row=1, column=1, sticky=E)

        self.repFrame1 = Frame(self.repFrame, bd=1, bg="powder blue")
        self.repFrame1.grid(row=4, column=0, columnspan=2)

        self.delFrame1 = Frame(self.delFrame, bd=0, bg="powder blue", pady=4)
        self.delFrame1.grid(row=6, column=0, columnspan=2)

        self.delFrame2 = Frame(self.delFrame, bd=1, bg="Ghost White", pady=4)
        self.delFrame2.grid(row=7, column=0, columnspan=2)

        # ============================== Label ==================================================
        self.titlelbl = Label(self.titleFrame, font=("arial", 50, "bold"), bg='light green',
                              text="Produce Delivery and Reports", justify=CENTER)
        self.titlelbl.pack()

        # _________ Delivery Details Labels________
        self.deldetails = Label(self.delFrame, font=("ALGERIAN", 25, "bold"), text="Delivery Details ",
                                bg="powder blue")
        self.deldetails.grid(row=0, column=0, sticky=W, pady=7)

        self.refNolbl = Label(self.delFrame, text="Reference No:", font=("arial", 20, "bold"), bg="powder blue")
        self.refNolbl.grid(row=1, column=0)
        self.delDate = Label(self.delFrame, text="Delivery Date:", font=("arial", 20, "bold"), bg="powder blue")
        self.delDate.grid(row=2, column=0)
        self.fuid = Label(self.delFrame, text="Farmer UID:", font=("arial", 20, "bold"), bg="powder blue")
        self.fuid.grid(row=3, column=0)
        self.surName = Label(self.delFrame, text="Surname:", font=("arial", 20, "bold"), bg="powder blue")
        self.surName.grid(row=4, column=0)
        self.weightlbl = Label(self.delFrame, text="Weight (Kgs):", font=("arial", 20, "bold"), bg="powder blue")
        self.weightlbl.grid(row=5, column=0)

        self.pricelbl = Label(self.delFrame1, text="Price on Delivery", font=("arial", 20, "bold"), bg="powder blue")
        self.pricelbl.grid(row=0, column=0, sticky=W, padx=0)
        self.cashlbl = Label(self.delFrame1, text="Total Cash", font=("arial", 20, "bold"), bg="powder blue")
        self.cashlbl.grid(row=0, column=2, sticky=W, padx=5)

        # _________ Delivery Details Entries________
        self.refNoEntry = Entry(self.delFrame, font=("arial", 20), textvariable=self.deliveryRef, width=25,
                                state=DISABLED)
        self.refNoEntry.grid(row=1, column=1, pady=5)
        self.delDateEntry = Entry(self.delFrame, font=("arial", 20), textvariable=self.deliveryDate, width=25,
                                  state=DISABLED)
        self.delDateEntry.grid(row=2, column=1, pady=5)
        self.FUIDEntry = Entry(self.delFrame, font=("arial", 20), width=25, textvariable=self.uid)
        self.FUIDEntry.grid(row=3, column=1, pady=5)
        self.surNameEntry = Entry(self.delFrame, font=("arial", 20), textvariable=self.surname, width=25,
                                  state=DISABLED)
        self.surNameEntry.grid(row=4, column=1, pady=5)
        self.weightEntry = Entry(self.delFrame, font=("arial", 20), textvariable=self.weight, width=25)
        self.weightEntry.grid(row=5, column=1, pady=5)

        self.priceEntry = Entry(self.delFrame1, font=("arial", 20), textvariable=self.deliveryPrice, width=7,
                                state=DISABLED)
        self.priceEntry.grid(row=0, column=1, pady=5, padx=4)
        self.cashEntry = Entry(self.delFrame1, font=("arial", 20), textvariable=self.TotalCash, width=15,
                               state=DISABLED)
        self.cashEntry.grid(row=0, column=3, pady=5)

        # _________ Delivery Details Buttons________
        self.viewbtn = Button(self.delFrame2, text="View", width=11, font=("arial", 19, 'bold'), bd=4,
                              command=self.iView)
        self.viewbtn.grid(row=0, column=0, padx=5)
        self.receivebtn = Button(self.delFrame2, text="Receive", width=11, font=("arial", 19, 'bold'), bd=4,
                                 command=self.iReceive)
        self.receivebtn.grid(row=0, column=1, padx=5)
        self.receiptbtn = Button(self.delFrame2, text="Receipt", width=11, font=("arial", 19, 'bold'), bd=4,
                                 command=self.iReceipt)
        self.receiptbtn.grid(row=0, column=2, padx=5)
        self.resetbtn = Button(self.delFrame2, text="Reset", width=11, font=("arial", 19, 'bold'), bd=4,
                               command=self.iReset)
        self.resetbtn.grid(row=0, column=4, padx=5)

        self.displaybtn = Button(self.delFrame2, text="Display All Records", width=24, font=("arial", 19, 'bold'), bd=4,
                                 command=self.displayDelivery)
        self.displaybtn.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        self.searchbtn = Button(self.delFrame2, text="Enquire", width=11, font=("arial", 19, 'bold'), bd=4,
                                command=self.searchDelivery)
        self.searchbtn.grid(row=1, column=2, padx=5)
        self.exitbtn = Button(self.delFrame2, text="Exit", width=11, font=("arial", 19, 'bold'), bd=4,
                              command=self.iExit)
        self.exitbtn.grid(row=1, column=4, padx=5)

        # _________ Report Widgets _______________
        self.replbl = Label(self.repFrame, font=("ALGERIAN", 25, "bold"), text="Search Reports By: ", bg="powder blue")
        self.replbl.grid(row=0, column=0, sticky=W, pady=7, columnspan=2)

        # _________ Report Widgets CheckButtons _______________
        self.repref = Checkbutton(self.repFrame, text="Reference No", font=('arial', 17, 'bold'), bg='powder blue',
                                  variable=self.var1, \
                                  onvalue=1, offvalue=0, command=self.chkrepref)
        self.repref.grid(row=1, sticky=W, padx=30)
        self.datelbl = Checkbutton(self.repFrame, text="Date of Delivery", font=('arial', 17, 'bold'), bg='powder blue',
                                   variable=self.var2, \
                                   onvalue=1, offvalue=0, command=self.chkdatelbl)
        self.datelbl.grid(row=2, sticky=W, padx=30)
        self.fuidlbl = Checkbutton(self.repFrame, text="Farmer UID", font=('arial', 17, 'bold'), bg='powder blue',
                                   variable=self.var3, \
                                   onvalue=1, offvalue=0, command=self.chkfuidlbl)
        self.fuidlbl.grid(row=3, sticky=W, padx=30)
        # _________ Checkbuttons Entries _______________________
        self.reprefEntry = Entry(self.repFrame, font=('arial', 17, 'bold'), textvariable=self.vrepref, width=15,
                                 state=DISABLED)
        self.reprefEntry.grid(row=1, column=1, sticky=W)
        self.dateEntry = Entry(self.repFrame, font=('arial', 17, 'bold'), textvariable=self.vdate, width=15,
                               state=DISABLED)
        self.dateEntry.grid(row=2, column=1, sticky=W)
        self.fuidEntry = Entry(self.repFrame, font=('arial', 17, 'bold'), textvariable=self.vfuid, width=15,
                               state=DISABLED)
        self.fuidEntry.grid(row=3, column=1, sticky=W)

        # ___________ Receipt and Reports TextArea ______________
        self.txtRepRec = Text(self.repFrame1, width=54, height=15, bg='white', bd=4, font=('arial', 12, 'bold'))
        self.txtRepRec.pack()

    def iExit(self):
        confirm = tkinter.messagebox.askyesno("Deliveries and Reports", "Confirm to exit Window")
        if confirm > 0:
            self.root14.destroy()
            return
        else:
            return

    def generateRef(self, size, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))

    def iView(self):
        self.deliveryRef.set(self.generateRef(9, 'QWERTYUIOPASDFGHJKLZXCVBNM123456789'))
        self.deliveryDate.set(time.strftime("%d/%m/%Y"))
        data1 = Sqlite3_Backend.selectSurname(self.uid.get())
        for datum in data1:
            self.surname.set(datum[0])
        Sqlite3_Backend.OtherPricesTable()
        data2 = Sqlite3_Backend.selectPrice()
        for datum in data2:
            self.deliveryPrice.set(datum[0])
            break
        self.totalcash = float(self.deliveryPrice.get()) * float(self.weight.get())
        ftotalcash = "Kshs " + str("%.2f" % (self.totalcash))
        self.TotalCash.set(ftotalcash)

    def iReset(self):
        self.deliveryPrice.set("")
        self.deliveryRef.set("")
        self.deliveryDate.set("")
        self.surname.set("")
        self.uid.set("")
        self.weight.set("")
        self.TotalCash.set("")
        self.txtRepRec.delete("1.0", END)
        self.var1.set(0)
        self.var2.set(0)
        self.var3.set(0)
        self.chkdatelbl()
        self.chkfuidlbl()
        self.chkrepref()

    def iReceipt(self):
        self.txtRepRec.delete("1.0", END)
        self.txtRepRec.insert(END, "\t\tRFA Produce Delivery Receipt\n")
        self.txtRepRec.insert(END,
                              "     Ref No: \t" + self.deliveryRef.get() + "\t\t\tDate: \t" + self.deliveryDate.get() + "\n")
        self.txtRepRec.insert(END, "FUID:   \t" + self.uid.get() + "\nSurname: \t" + self.surname.get() + "\n")
        self.txtRepRec.insert(END, "Total Weight: \t" + str(self.weight.get()) + " Kilograms" + "\n")
        self.txtRepRec.insert(END, "Price on Delivery: \t" + "KShs " + self.deliveryPrice.get() + " per Kg" + "\n")
        self.txtRepRec.insert(END, "Total Cash at RFA: \t" + self.TotalCash.get() + "\n")

    def iReceive(self):
        Sqlite3_Backend.DeliveryTable()
        if (self.deliveryRef.get() != 0) and (self.deliveryDate.get() != 0) and (self.uid.get() != 0) and (
                self.surname.get() != 0) and \
                (self.weight.get() != 0) and (self.TotalCash.get() != 0):
            confirm = tkinter.messagebox.askyesno("Add Delivery", "Confirm\nTo add Produce Delivery Record")
            if confirm > 0:
                Sqlite3_Backend.addDelivery(self.deliveryRef.get(), self.deliveryDate.get(), self.uid.get(),
                                            self.surname.get(), self.weight.get(), self.totalcash)
                tkinter.messagebox.showinfo("Successful", "Delivery Record Added Successfully")
            else:
                return
        else:
            tkinter.messagebox.showinfo("Null Fields", "All Fields must be filled")
            return

    def searchDelivery(self):
        if self.var1.get() == 1 and self.var2.get() == 0 and self.var3.get() == 0:
            data1 = Sqlite3_Backend.refSearchDelivery(self.vrepref.get())
            if data1 == []:
                tkinter.messagebox.showinfo("Records", "Record doesn't exist")
                return
            else:
                self.txtRepRec.delete("1.0", END)
                for datum in data1:
                    self.txtRepRec.insert(END, datum)
                    self.txtRepRec.insert(END, "\n")
        elif self.var2.get() == 1 and self.var1.get() == 0 and self.var3.get() == 0:
            data2 = Sqlite3_Backend.dateSearchDelivery(self.vdate.get())
            if data2 == []:
                tkinter.messagebox.showinfo("Records", "Record doesn't exist")
                return
            else:
                self.txtRepRec.delete("1.0", END)
                for datum in data2:
                    self.txtRepRec.insert(END, datum)
                    self.txtRepRec.insert(END, "\n")
        elif self.var3.get() == 1 and self.var2.get() == 0 and self.var1.get() == 0:
            data3 = Sqlite3_Backend.fuidSearchDelivery(self.vfuid.get())
            if data3 == []:
                tkinter.messagebox.showinfo("Records", "Record doesn't exist")
                return
            else:
                self.txtRepRec.delete("1.0", END)
                for datum in data3:
                    self.txtRepRec.insert(END, datum)
                    self.txtRepRec.insert(END, "\n")
        elif self.var1.get() == 1 and self.var2.get() == 1 and self.var3.get() == 1:
            data4 = Sqlite3_Backend.rdfSearchDelivery(self.vrepref.get(), self.vdate.get(), self.vfuid.get())
            if data4 == []:
                tkinter.messagebox.showinfo("Records", "Record doesn't exist")
                return
            else:
                self.txtRepRec.delete("1.0", END)
                for datum in data4:
                    self.txtRepRec.insert(END, datum)
                    self.txtRepRec.insert(END, "\n")

    def displayDelivery(self):
        data5 = Sqlite3_Backend.displayDeliveryData()
        if data5 == []:
            tkinter.messagebox.showinfo("Records", "No Delivery Record")
            return
        else:
            self.txtRepRec.delete("1.0", END)
            for datum in data5:
                self.txtRepRec.insert(END, datum)
                self.txtRepRec.insert(END, '\n')

    def chkrepref(self):
        if self.var1.get() == 1:
            self.reprefEntry.config(state=NORMAL)
            self.reprefEntry.focus()
        elif self.var1.get() == 0:
            self.reprefEntry.config(state=DISABLED)
            self.vrepref.set("")

    def chkdatelbl(self):
        if self.var2.get() == 1:
            self.dateEntry.config(state=NORMAL)
            self.dateEntry.focus()
        elif self.var2.get() == 0:
            self.dateEntry.config(state=DISABLED)
            self.vdate.set("")

    def chkfuidlbl(self):
        if self.var3.get() == 1:
            self.fuidEntry.config(state=NORMAL)
            self.fuidEntry.focus()
        elif self.var3.get() == 0:
            self.fuidEntry.config(state=DISABLED)
            self.vfuid.set("")


def main():
    root = Tk()
    run = Produce_delivery(root)
    root.mainloop()


main()