from tkinter import *
import tkinter.messagebox
import datetime
import time
import string
import random
import Sqlite3_Backend


class Pay_Farmer:
    def __init__(self):
        self.uid = StringVar()
        self.surname = StringVar()
        self.iDNo = StringVar()
        self.services = StringVar()
        self.fert = StringVar()
        self.farmin = StringVar()
        self.tax = StringVar()
        self.total = StringVar()
        self.weight = StringVar()
        self.totalCash = StringVar()
        self.payMe = StringVar()
        self.pay_farmer_amount = DoubleVar()
        self.income = DoubleVar()
        self.expenses = DoubleVar()
        self.paidAmount = DoubleVar()
        self.paymentRef = StringVar()
        self.paymentDate = StringVar()
        self.searchDate = StringVar()

        self.services.set(0.00)
        self.fert.set(0.00)
        self.farmin.set(0.00)
        self.tax.set(0.00)
        self.total.set(0.00)
        self.weight.set(0.00)
        self.totalCash.set(0.00)
        self.payMe.set(0.00)
        self.pay_farmer_amount = 0.00
        self.income = 0.00
        self.expenses = 0.00
        self.paidAmount.set(0.00)

    def iExit(self):
        confirm = tkinter.messagebox.askyesno("RFA Farmer Status", "Confirm to Exit")
        if confirm > 0:
            self.root18.destroy()
            return
        else:
            return

    def iClear(self):
        self.uid.set('')
        self.surname.set('')
        self.iDNo.set('')
        self.services.set(0.00)
        self.fert.set(0.00)
        self.farmin.set(0.00)
        self.tax.set(0.00)
        self.total.set(0.00)
        self.weight.set(0.00)
        self.totalCash.set(0.00)
        self.payMe.set(0.00)
        self.pay_farmer_amount = 0.00
        self.income = 0.00
        self.expenses = 0.00
        self.paidAmount.set(0.00)
        self.paymentRef.set('')
        self.txtref.delete('1.0', END)
        self.fuidEntry.focus()

    def generateRef(self, size, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))

    def iView(self):
        self.surname.set('')
        self.iDNo.set('')
        self.services.set(0.00)
        self.fert.set(0.00)
        self.farmin.set(0.00)
        self.tax.set(0.00)
        self.total.set(0.00)
        self.weight.set(0.00)
        self.totalCash.set(0.00)
        self.payMe.set(0.00)
        self.pay_farmer_amount = 0.00
        self.income = 0.00
        self.expenses = 0.00
        self.paidAmount.set(0.00)
        self.paymentRef.set('')
        self.txtref.delete('1.0', END)
        self.fuidEntry.focus()

        self.payRefEntry.config(state=DISABLED)
        self.paymentRef.set('')
        self.searchDate.set('')
        data1 = Sqlite3_Backend.getsurid(self.uid.get())
        if data1 == []:
            self.surname.set('')
            self.iDNo.set("")
            tkinter.messagebox.showinfo("Records", "FUID Entered doesn't Exist\nDouble Check and Try Again")
            return
        else:
            for datum in data1:
                self.surname.set(datum[0])
                self.iDNo.set(datum[1])
                break
        data2 = Sqlite3_Backend.viewServiceStatus(self.uid.get())
        for datum in data2:
            if datum[0] == None:
                self.services.set(0.00)
            else:
                self.services.set(('KShs ' + str(datum[0])))
        data3 = Sqlite3_Backend.viewFertilizerStatus(self.uid.get())
        for datum in data3:
            if datum[0] == None:
                self.fert.set(0.00)
            else:
                self.fert.set(('KShs ' + str(datum[0])))
        data4 = Sqlite3_Backend.viewFarmInStatus(self.uid.get())
        for datum in data4:
            if datum[0] == None:
                self.farmin.set(0.00)
            else:
                self.farmin.set(('KShs ' + str(datum[0])))
        data5 = Sqlite3_Backend.viewTaxStatus(self.uid.get())
        for datum in data5:
            if datum[0] == None:
                self.farmin.set(0.00)
            else:
                self.tax.set(('KShs ' + str(datum[0])))
        data6 = Sqlite3_Backend.viewTotalStatus(self.uid.get())
        for datum in data6:
            if datum[0] == None:
                self.total.set(0.00)
            else:
                self.expenses = float(datum[0])
                self.total.set(('KShs ' + str(datum[0])))
        data7 = Sqlite3_Backend.viewWeightStatus(self.uid.get())
        for datum in data7:
            if datum[0] == None:
                self.weight.set(0.00)
            else:
                self.weight.set((str(datum[0]) + ' Kilos'))
        data8 = Sqlite3_Backend.viewTotalCashStatus(self.uid.get())
        for datum in data8:
            if datum[0] == None:
                self.totalCash.set(0.00)
            else:
                self.income = float(datum[0])
                self.totalCash.set(('KShs ' + str(datum[0])))
        if self.income == 0.0 or self.income < 0.0:
            self.paidAmount.set(0.00)
        if self.income < self.expenses:
            self.paidAmount.set(0.00)
        elif self.income == self.expenses:
            self.paidAmount.set(0.00)
        elif self.income > self.expenses:
            self.pay_farmer_amount = float(self.income - self.expenses)
            self.payMe.set(('KShs ' + str(self.pay_farmer_amount)))
            self.paidAmount.set(self.pay_farmer_amount)
            self.paidAmountEntry.focus()
            self.paymentRef.set(self.generateRef(10, 'QWERTYUIOPASDFGHJKLZXCVBNM123456789'))
        self.btnApprove.config(state=NORMAL)

    def reportRec(self):
        self.searchDate.set('Enter Date Here')
        self.payRefEntry.config(state=NORMAL)
        self.paymentRef.set('Enter Ref Here')

    def iPayFarmer(self):
        self.paymentDate = time.strftime("%d/%m/%Y")
        Sqlite3_Backend.paymentTable()
        Sqlite3_Backend.serviceArchiveTable()
        Sqlite3_Backend.DeliveryArchiveTable()
        if self.paidAmount.get() > 0.00 and float(self.paidAmount.get()) == self.pay_farmer_amount:
            if (len(self.surname.get()) != 0 and len(self.uid.get()) != 0 and len(self.paymentRef.get()) != 0):
                confirm = tkinter.messagebox.askyesno("Finalize Payment", "Confirm To Finalize Payment")
                if confirm > 0:
                    Sqlite3_Backend.addPaymentRec(self.paymentRef.get(), self.paymentDate, self.uid.get(),
                                                  self.surname.get(), self.paidAmount.get())
                    Sqlite3_Backend.copyService(self.uid.get())
                    Sqlite3_Backend.copyDelivery(self.uid.get())
                    Sqlite3_Backend.deleteServiceCopy(self.uid.get())
                    Sqlite3_Backend.deleteDeliveryCopy(self.uid.get())
                    tkinter.messagebox.showinfo("Finalize Payment", "Payment Successfully Finalized")
                    self.printReceipt()
                    self.btnApprove.config(state=DISABLED)
                else:
                    return
            else:
                tkinter.messagebox.showerror('Pay Farmer', 'All Fields Must be Filled')
                return
        else:
            tkinter.messagebox.showerror("Zero Payment", "Farmer Not Elligible For Payment")

    def printReceipt(self):
        self.txtref.delete('1.0', END)
        self.paymentDate = time.strftime("%d/%m/%Y")
        self.txtref.insert(END, "\tRFA FULL PAYMENT RECEIPT\n")
        self.txtref.insert(END, " Ref No: " + self.paymentRef.get() + "\t\t\t" + "\tDate: " + self.paymentDate + "\n")
        self.txtref.insert(END,
                           " FUID: " + self.uid.get() + "\t       Surname: " + self.surname.get() + "\t            IDNo: " + self.iDNo.get() + "\n")
        self.txtref.insert(END,
                           "--------------------------------------------------------------------------------------\n")
        self.txtref.insert(END,
                           "\tServices: \t      " + self.services.get() + "\n\tFertilizer: \t      " + self.fert.get() + "\n")
        self.txtref.insert(END,
                           "\tFarm Inputs: \t" + self.farmin.get() + "\n\tTax Paid: \t      " + self.tax.get() + "\n")
        self.txtref.insert(END, "\t--------------------------------------------\n")
        self.txtref.insert(END, "\tTotal Cost:     " + self.total.get() + "\n\n")
        self.txtref.insert(END, "\tWeight: \t       " + self.weight.get() + "\n")
        self.txtref.insert(END, "\tTotal Cash: \t  " + self.totalCash.get() + "\n")
        self.txtref.insert(END, "\t--------------------------------------------\n")
        self.txtref.insert(END, "\tPaid Total:     " + "KShs " + str(self.paidAmount.get()) + "\n")
        self.txtref.insert(END, "\tBalance:     " + "    KShs 0.00")

    def displayAll(self):
        self.txtref.delete('1.0', END)
        data = Sqlite3_Backend.displayPayment()
        for datum in data:
            self.txtref.insert(END, datum)
            self.txtref.insert(END, "\n")

    def searchPayment(self):
        self.txtref.delete('1.0', END)
        data = Sqlite3_Backend.searchPayment(self.uid.get(), self.paymentRef.get(), self.searchDate.get())
        for datum in data:
            self.txtref.insert(END, datum)
            self.txtref.insert(END, '\n')

    def widgets(self, root18):
        self.root18 = root18
        self.root18.title("Farmer Status")
        self.root18.geometry("1350x750+0+0")
        self.root18.config(bg='light green')

        self.mainframe = Frame(self.root18, bd=20, bg='light green')
        self.mainframe.pack()

        self.titleframe = Frame(self.mainframe, bd=10, padx=54)
        self.titleframe.grid(row=0, column=0)

        self.dataFrame = Frame(self.mainframe, bd=10, bg='#95C8D8')
        self.dataFrame.grid(row=1, column=0, pady=10)

        self.btnFrame = Frame(self.mainframe, bd=10)
        self.btnFrame.grid(row=2, column=0)

        self.detailsFrame = Frame(self.dataFrame, bg='#95C8D8')
        self.detailsFrame.grid(row=0, column=0, columnspan=2)

        self.detailsFrameLeft = Frame(self.dataFrame, bg='powder blue', padx=10)
        self.detailsFrameLeft.grid(row=1, column=0, sticky=W, pady=15)

        self.detailsFrameRight = Frame(self.dataFrame, bg='powder blue')
        self.detailsFrameRight.grid(row=1, column=1)

        # ____________________________ Title Label _________________________
        self.titlelbl = Label(self.titleframe, text='RFA Payment', font=('arial', 50, 'bold'), justify=CENTER)
        self.titlelbl.grid(row=0, column=0, padx=0, pady=0)

        # ____________________________ Details Label _________________________
        self.fuidlbl = Label(self.detailsFrame, text='FUID', font=('arial', 20, 'bold'), bg='#95C8D8')
        self.fuidlbl.grid(row=0, column=0)

        self.surnamelbl = Label(self.detailsFrame, text='Surname', font=('arial', 20, 'bold'), bg='#95C8D8')
        self.surnamelbl.grid(row=0, column=2)

        self.idlbl = Label(self.detailsFrame, text='IDNo', font=('arial', 20, 'bold'), bg='#95C8D8')
        self.idlbl.grid(row=0, column=4)

        # ____________________________ Details Entries _________________________
        self.fuidEntry = Entry(self.detailsFrame, font=('arial', 18, 'bold'), textvariable=self.uid)
        self.fuidEntry.grid(row=0, column=1, padx=10)

        self.surnameEntry = Entry(self.detailsFrame, font=('arial', 18, 'bold'), textvariable=self.surname,
                                  state=DISABLED)
        self.surnameEntry.grid(row=0, column=3, padx=10)

        self.idEntry = Entry(self.detailsFrame, font=('arial', 18, 'bold'), textvariable=self.iDNo, state=DISABLED)
        self.idEntry.grid(row=0, column=5, padx=10)

        # ____________________________ Services Labels and Entries _________________________
        self.svclbl = Label(self.detailsFrameLeft, text='Services', font=('ALGERIAN', 19, 'bold'), bg='powder blue')
        self.svclbl.grid(row=0, column=0, sticky=W)

        self.serviceslbl = Label(self.detailsFrameLeft, text='     Cost of Services:', font=('arial', 20, 'bold'),
                                 bg='powder blue')
        self.serviceslbl.grid(row=1, column=0)

        self.fertlbl = Label(self.detailsFrameLeft, text='     Cost of Fertilizer:', font=('arial', 20, 'bold'),
                             bg='powder blue')
        self.fertlbl.grid(row=2, column=0)

        self.farminlbl = Label(self.detailsFrameLeft, text='     Farm Inputs Cost:', font=('arial', 20, 'bold'),
                               bg='powder blue')
        self.farminlbl.grid(row=3, column=0)

        self.taxlbl = Label(self.detailsFrameLeft, text='     Paid Tax:', font=('arial', 20, 'bold'), bg='powder blue')
        self.taxlbl.grid(row=4, column=0)

        self.totallbl = Label(self.detailsFrameLeft, text='     Total Cost:', font=('arial', 20, 'bold'),
                              bg='powder blue')
        self.totallbl.grid(row=5, column=0)

        # ________ Entries________
        self.servicesEntry = Entry(self.detailsFrameLeft, font=('arial', 18, 'bold'), textvariable=self.services,
                                   state=DISABLED)
        self.servicesEntry.grid(row=1, column=1, padx=10, pady=5)

        self.fertEntry = Entry(self.detailsFrameLeft, font=('arial', 18, 'bold'), textvariable=self.fert,
                               state=DISABLED)
        self.fertEntry.grid(row=2, column=1, padx=10, pady=5)

        self.farminEntry = Entry(self.detailsFrameLeft, font=('arial', 18, 'bold'), textvariable=self.farmin,
                                 state=DISABLED)
        self.farminEntry.grid(row=3, column=1, padx=10, pady=5)

        self.taxEntry = Entry(self.detailsFrameLeft, font=('arial', 18, 'bold'), textvariable=self.tax, state=DISABLED)
        self.taxEntry.grid(row=4, column=1, padx=10, pady=5)

        self.totalEntry = Entry(self.detailsFrameLeft, font=('arial', 18, 'bold'), textvariable=self.total,
                                state=DISABLED)
        self.totalEntry.grid(row=5, column=1, padx=10, pady=5)

        # ____________________________ Delivery Labels and Entries _________________________
        self.dellbl = Label(self.detailsFrameLeft, text='Produce Delivery', font=('ALGERIAN', 19, 'bold'),
                            bg='powder blue')
        self.dellbl.grid(row=6, column=0, sticky=W)

        self.weightlbl = Label(self.detailsFrameLeft, text='     Total Weight:', font=('arial', 20, 'bold'),
                               bg='powder blue')
        self.weightlbl.grid(row=7, column=0)

        self.cashlbl = Label(self.detailsFrameLeft, text='     Total Cash:', font=('arial', 20, 'bold'),
                             bg='powder blue')
        self.cashlbl.grid(row=8, column=0)
        # _____ Expected Payment Label _______
        self.paylbl = Label(self.detailsFrameLeft, text='Expected Payment', font=('ALGERIAN', 20, 'bold'),
                            bg='powder blue')
        self.paylbl.grid(row=9, column=0)

        # ________ Entries________
        self.weightEntry = Entry(self.detailsFrameLeft, textvariable=self.weight, font=('arial', 18, 'bold'),
                                 state=DISABLED)
        self.weightEntry.grid(row=7, column=1, padx=10, pady=5)

        self.cashEntry = Entry(self.detailsFrameLeft, textvariable=self.totalCash, font=('arial', 18, 'bold'),
                               state=DISABLED)
        self.cashEntry.grid(row=8, column=1, padx=10, pady=5)
        # _____ Expected Payment Entry _____
        self.payEntry = Entry(self.detailsFrameLeft, textvariable=self.payMe, font=('ALGERIAN', 19, 'bold'),
                              state=DISABLED)
        self.payEntry.grid(row=9, column=1, padx=10, pady=6)

        # ______________ Payment Ref and Amount _____________
        # _____ Labels _______
        self.payReflbl = Label(self.detailsFrameRight, text='Payment Ref:', font=('arial', 20, 'bold'),
                               bg='powder blue')
        self.payReflbl.grid(row=0, column=0, sticky=W)

        self.paidAmountlbl = Label(self.detailsFrameRight, text='Amount:', font=('arial', 20, 'bold'), bg='powder blue')
        self.paidAmountlbl.grid(row=1, column=0, sticky=W)

        # _____ Entries ______
        self.payRefEntry = Entry(self.detailsFrameRight, font=('arial', 18, 'bold'), textvariable=self.paymentRef,
                                 state=DISABLED)
        self.payRefEntry.grid(row=0, column=1, pady=5, padx=5)

        self.paidAmountEntry = Entry(self.detailsFrameRight, textvariable=self.paidAmount, font=('arial', 18, 'bold'),
                                     state=DISABLED)
        self.paidAmountEntry.grid(row=1, column=1, pady=5, padx=5)

        # _______________ Receipt and Reports TextBox __________________
        self.dellbl = Label(self.detailsFrameRight, text='Receipt and Reports', font=('ALGERIAN', 19, 'bold'),
                            bg='powder blue')
        self.dellbl.grid(row=2, column=0, sticky=W)

        self.paydateEntry = Entry(self.detailsFrameRight, textvariable=self.searchDate, font=('arial', 18, 'bold'),
                                  bd=0, bg='powder blue')
        self.paydateEntry.grid(row=2, column=1, pady=5, padx=5)

        self.txtref = Text(self.detailsFrameRight, font=('arial', 14, 'bold'), height=12, width=47, bd=4)
        self.txtref.grid(row=3, column=0, pady=10, columnspan=2, sticky=E, padx=5)

        # ____________________________ Buttons ___________________________________
        self.btnView = Button(self.btnFrame, text="View", font=('arial', 18, 'bold'), width=10, bd=3,
                              command=self.iView)
        self.btnView.grid(row=0, column=0, padx=5)

        self.btnApprove = Button(self.btnFrame, text="Approve Payment", font=('arial', 18, 'bold'), width=15, bd=3,
                                 bg='powder blue', \
                                 command=self.iPayFarmer)
        self.btnApprove.grid(row=0, column=1, padx=5)

        self.btnClear = Button(self.btnFrame, text="Clear", font=('arial', 18, 'bold'), width=10, bd=3,
                               command=self.iClear)
        self.btnClear.grid(row=0, column=2, padx=5)

        self.btnReports = Button(self.btnFrame, text="Reports", font=('arial', 18, 'bold'), width=10, bd=3,
                                 command=self.reportRec)
        self.btnReports.grid(row=0, column=3, padx=5)

        self.btnSearch = Button(self.btnFrame, text="Search Record", font=('arial', 18, 'bold'), width=12, bd=3,
                                command=self.searchPayment)
        self.btnSearch.grid(row=0, column=4, padx=5)

        self.btnDisplay = Button(self.btnFrame, text="Display All", font=('arial', 18, 'bold'), width=10, bd=3,
                                 command=self.displayAll)
        self.btnDisplay.grid(row=0, column=5, padx=5)

        self.btnExit = Button(self.btnFrame, text="Exit Window", font=('arial', 18, 'bold'), width=10, bd=3,
                              command=self.iExit)
        self.btnExit.grid(row=0, column=6, padx=5)


def main():
    root = Tk()
    runx = Pay_Farmer()
    runx.widgets(root)
    root.mainloop()


main()