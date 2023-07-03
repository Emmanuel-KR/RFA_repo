from tkinter import *
import tkinter.messagebox
import datetime
import time
import Sqlite3_Backend


class Farmer_Status:
    def __init__(self):
        self.uid = StringVar()
        self.surname = StringVar()
        self.iDNo = StringVar()
        self.services = DoubleVar()
        self.fert = DoubleVar()
        self.farmin = DoubleVar()
        self.tax = DoubleVar()
        self.total = DoubleVar()
        self.weight = DoubleVar()
        self.totalCash = DoubleVar()
        self.payMe = DoubleVar()

    def iExit(self):
        confirm = tkinter.messagebox.askyesno("RFA Farmer Status", "Confirm to Exit")
        if confirm > 0:
            self.root17.destroy()
            return
        else:
            return

    def iReceipt(self):
        self.txtref.delete('1.0', END)
        self.txtref.insert(END, '  SERVICES REFERENCES :\n')
        data0 = Sqlite3_Backend.viewServiceRefStatus(self.uid.get())
        for datum in data0:
            self.txtref.insert(END, '\t')
            self.txtref.insert(END, datum)
            self.txtref.insert(END, '\n')
        self.txtref.insert(END, '\n  PRODUCE DELIVERY REFERENCES :\n')
        data = Sqlite3_Backend.viewDeliveryRefStatus(self.uid.get())
        for datum in data:
            self.txtref.insert(END, '\t')
            self.txtref.insert(END, datum)
            self.txtref.insert(END, '\n')

    def iView(self):
        self.iDNo.set('')
        self.surname.set('')
        self.services.set('0')
        self.fert.set('0')
        self.farmin.set('0')
        self.tax.set('0')
        self.total.set('0')
        self.weight.set('0')
        self.totalCash.set('0')
        self.payMe.set('0')
        self.txtref.delete('1.0', END)

        data1 = Sqlite3_Backend.getsurid(self.uid.get())
        for datum in data1:
            self.surname.set(datum[0])
            self.iDNo.set(datum[1])
            break
        data2 = Sqlite3_Backend.viewServiceStatus(self.uid.get())
        for datum in data2:
            self.services.set(('KShs ' + str(datum[0])))
        data3 = Sqlite3_Backend.viewFertilizerStatus(self.uid.get())
        if data3 == []:
            self.fert.set('KShs 0.00')
        else:
            for datum in data3:
                self.fert.set(('KShs ' + str(datum[0])))
        data4 = Sqlite3_Backend.viewFarmInStatus(self.uid.get())
        for datum in data4:
            self.farmin.set(('KShs ' + str(datum[0])))
        data5 = Sqlite3_Backend.viewTaxStatus(self.uid.get())
        for datum in data5:
            self.tax.set(('KShs ' + str(datum[0])))
        data6 = Sqlite3_Backend.viewTotalStatus(self.uid.get())
        for datum in data6:
            self.total.set(('KShs ' + str(datum[0])))
        data7 = Sqlite3_Backend.viewWeightStatus(self.uid.get())
        for datum in data7:
            self.weight.set(('KShs ' + str(datum[0])))
        data8 = Sqlite3_Backend.viewTotalCashStatus(self.uid.get())
        for datum in data8:
            self.totalCash.set(('KShs ' + str(datum[0])))
        for datum in data6:
            expenses = datum[0]
        for datum in data8:
            income = datum[0]
        if (expenses == 0 or expenses == NONE) and (income != NONE or income != 0):
            self.payMe.set(('KShs ' + str(income)))
        elif (income == 0 or income == NONE) and (expenses != NONE or expenses != 0):
            self.payMe.set(('KShs ' + str(- expenses)))
            tkinter.messagebox.showinfo("Farmer Status", "Overdrawn Account")
        elif (income == 0 or income == NONE) and (expenses == 0 or expenses == NONE):
            self.payMe.set('KShs 0.00')
        elif income != 0 and expenses != 0:
            self.payMe.set(('KShs ' + str(float(income) - float(expenses))))
        self.iReceipt()

    def iClear(self):
        self.uid.set('')
        self.iDNo.set('')
        self.surname.set('')
        self.services.set('0')
        self.fert.set('0')
        self.farmin.set('0')
        self.tax.set('0')
        self.total.set('0')
        self.weight.set('0')
        self.totalCash.set('0')
        self.payMe.set('0')
        self.txtref.delete('1.0', END)

    def widgets(self, root17):
        self.root17 = root17
        self.root17.title("Farmer Status")
        self.root17.geometry("1350x750+0+0")
        self.root17.config(bg='light green')

        self.mainframe = Frame(self.root17, bd=20, bg='light green')
        self.mainframe.pack()

        self.titleframe = Frame(self.mainframe, bd=10, padx=54)
        self.titleframe.grid(row=0, column=0)

        self.dataFrame = Frame(self.mainframe, bd=20)
        self.dataFrame.grid(row=1, column=0, pady=10)

        self.btnFrame = Frame(self.mainframe, bd=10)
        self.btnFrame.grid(row=2, column=0)

        self.detailsFrame = Frame(self.dataFrame)
        self.detailsFrame.grid(row=0, column=0, columnspan=2)

        self.datailsFrameLeft = Frame(self.dataFrame, bg='Ghost White', padx=10)
        self.datailsFrameLeft.grid(row=1, column=0, sticky=W, pady=15)

        self.datailsFrameRight = Frame(self.dataFrame, bg='Ghost White')
        self.datailsFrameRight.grid(row=1, column=1)

        # ____________________________ Title Label _________________________
        self.titlelbl = Label(self.titleframe, text='Farmer Status', font=('arial', 50, 'bold'), justify=CENTER)
        self.titlelbl.grid(row=0, column=0, padx=0, pady=0)

        # ____________________________ Details Label _________________________
        self.fuidlbl = Label(self.detailsFrame, text='FUID', font=('arial', 20, 'bold'))
        self.fuidlbl.grid(row=0, column=0)

        self.surnamelbl = Label(self.detailsFrame, text='Surname', font=('arial', 20, 'bold'))
        self.surnamelbl.grid(row=0, column=2)

        self.idlbl = Label(self.detailsFrame, text='IDNo', font=('arial', 20, 'bold'))
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
        self.svclbl = Label(self.datailsFrameLeft, text='Services', font=('ALGERIAN', 19, 'bold'), bg='Ghost White')
        self.svclbl.grid(row=0, column=0, sticky=W)

        self.serviceslbl = Label(self.datailsFrameLeft, text='     Cost of Services:', font=('arial', 20, 'bold'),
                                 bg='Ghost White')
        self.serviceslbl.grid(row=1, column=0)

        self.fertlbl = Label(self.datailsFrameLeft, text='     Cost of Fertilizer:', font=('arial', 20, 'bold'),
                             bg='Ghost White')
        self.fertlbl.grid(row=2, column=0)

        self.farminlbl = Label(self.datailsFrameLeft, text='     Farm Inputs Cost:', font=('arial', 20, 'bold'),
                               bg='Ghost White')
        self.farminlbl.grid(row=3, column=0)

        self.taxlbl = Label(self.datailsFrameLeft, text='     Paid Tax:', font=('arial', 20, 'bold'), bg='Ghost White')
        self.taxlbl.grid(row=4, column=0)

        self.totallbl = Label(self.datailsFrameLeft, text='     Total Cost:', font=('arial', 20, 'bold'),
                              bg='Ghost White')
        self.totallbl.grid(row=5, column=0)

        # ________ Entries________
        self.servicesEntry = Entry(self.datailsFrameLeft, font=('arial', 18, 'bold'), textvariable=self.services,
                                   state=DISABLED)
        self.servicesEntry.grid(row=1, column=1, padx=10, pady=5)

        self.fertEntry = Entry(self.datailsFrameLeft, font=('arial', 18, 'bold'), textvariable=self.fert,
                               state=DISABLED)
        self.fertEntry.grid(row=2, column=1, padx=10, pady=5)

        self.farminEntry = Entry(self.datailsFrameLeft, font=('arial', 18, 'bold'), textvariable=self.farmin,
                                 state=DISABLED)
        self.farminEntry.grid(row=3, column=1, padx=10, pady=5)

        self.taxEntry = Entry(self.datailsFrameLeft, font=('arial', 18, 'bold'), textvariable=self.tax, state=DISABLED)
        self.taxEntry.grid(row=4, column=1, padx=10, pady=5)

        self.totalEntry = Entry(self.datailsFrameLeft, font=('arial', 18, 'bold'), textvariable=self.total,
                                state=DISABLED)
        self.totalEntry.grid(row=5, column=1, padx=10, pady=5)

        # ____________________________ Delivery Labels and Entries _________________________
        self.dellbl = Label(self.datailsFrameLeft, text='Produce Delivery', font=('ALGERIAN', 19, 'bold'),
                            bg='Ghost White')
        self.dellbl.grid(row=6, column=0, sticky=W)

        self.weightlbl = Label(self.datailsFrameLeft, text='     Total Weight:', font=('arial', 20, 'bold'),
                               bg='Ghost White')
        self.weightlbl.grid(row=7, column=0)

        self.cashlbl = Label(self.datailsFrameLeft, text='     Total Cash:', font=('arial', 20, 'bold'),
                             bg='Ghost White')
        self.cashlbl.grid(row=8, column=0)

        # ________ Entries________
        self.weightEntry = Entry(self.datailsFrameLeft, textvariable=self.weight, font=('arial', 18, 'bold'),
                                 state=DISABLED)
        self.weightEntry.grid(row=7, column=1, padx=10, pady=5)

        self.cashEntry = Entry(self.datailsFrameLeft, textvariable=self.totalCash, font=('arial', 18, 'bold'),
                               state=DISABLED)
        self.cashEntry.grid(row=8, column=1, padx=10, pady=5)

        # _______ References TextBox ________
        self.reflbl = Label(self.datailsFrameRight, text='References', font=('ALGERIAN', 19, 'bold'), bg='Ghost White')
        self.reflbl.grid(row=0, column=0, sticky=W)

        self.txtref = Text(self.datailsFrameRight, font=('arial', 14, 'bold'), height=14, width=45, bd=4)
        self.txtref.grid(row=1, column=0, padx=15, pady=10)

        # ____________________________ Expected Payment Labels and Entries _________________________
        self.paylbl = Label(self.dataFrame, text='Expected Payment', font=('ALGERIAN', 20, 'bold'))
        self.paylbl.grid(row=2, column=0, sticky=E, padx=10)

        self.payEntry = Entry(self.dataFrame, textvariable=self.payMe, font=('ALGERIAN', 20, 'bold'), state=DISABLED)
        self.payEntry.grid(row=2, column=1, padx=10, sticky=W)

        # ____________________________ Buttons ___________________________________
        self.btnView = Button(self.btnFrame, text="View Status", font=('arial', 18, 'bold'), width=15, bd=3,
                              command=self.iView)
        self.btnView.grid(row=0, column=0)

        self.btnClear = Button(self.btnFrame, text="Clear", font=('arial', 18, 'bold'), width=15, bd=3,
                               command=self.iClear)
        self.btnClear.grid(row=0, column=1, padx=10)

        self.btnExit = Button(self.btnFrame, text="Exit Window", font=('arial', 18, 'bold'), width=15, bd=3,
                              command=self.iExit)
        self.btnExit.grid(row=0, column=2)


def main():
    root = Tk()
    runx = Farmer_Status()
    runx.widgets(root)
    root.mainloop()


main()