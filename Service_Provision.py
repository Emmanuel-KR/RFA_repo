from tkinter import *
import random
import string
import time
import datetime
import tkinter.messagebox
import Sqlite3_Backend


class Service_Provision:
    def __init__(self):
        self.harvest = StringVar()
        self.rotav = StringVar()
        self.transport = StringVar()
        self.seed = StringVar()
        self.escort = StringVar()
        self.dicoper = StringVar()
        self.regent = StringVar()
        self.opal = StringVar()
        self.npk = StringVar()
        self.zs = StringVar()
        self.can = StringVar()
        self.tsp = StringVar()
        self.ssp = StringVar()
        self.sa = StringVar()

        self.harvest.set("0")
        self.rotav.set("0")
        self.transport.set("0")
        self.seed.set("0")
        self.escort.set("0")
        self.dicoper.set("0")
        self.regent.set("0")
        self.opal.set("0")
        self.npk.set("0")
        self.zs.set("0")
        self.can.set("0")
        self.tsp.set("0")
        self.ssp.set("0")
        self.sa.set("0")

        self.provision_date = StringVar()
        self.repfuid = StringVar()
        self.repref = StringVar()

        self.Reference = StringVar()
        self.fuid = StringVar()
        self.surname = StringVar()
        self.iDNo = StringVar()
        self.var1 = IntVar()
        self.var2 = IntVar()
        self.var3 = IntVar()
        self.var4 = IntVar()
        self.var5 = IntVar()
        self.var6 = IntVar()
        self.var7 = IntVar()
        self.var8 = IntVar()
        self.var9 = IntVar()
        self.var10 = IntVar()
        self.var11 = IntVar()
        self.var12 = IntVar()
        self.var13 = IntVar()
        self.var14 = IntVar()
        self.var15 = IntVar()
        self.var16 = IntVar()
        self.var17 = IntVar()
        self.var18 = IntVar()
        self.var19 = IntVar()

        self.Cost_of_Fertilizer = StringVar()
        self.Cost_of_Services = StringVar()
        self.Cost_of_FarmIn = StringVar()
        self.SubTotal = StringVar()
        self.Tax = StringVar()
        self.Total = StringVar()

        # ____ Variables to be inserted in the database____
        self.priceofServices = DoubleVar()
        self.priceofFarmIn = DoubleVar()
        self.priceofFert = DoubleVar()
        self.tax = DoubleVar()
        self.ttl = DoubleVar()

    def iReset(self):
        self.fuid.set("")
        self.surname.set("")
        self.iDNo.set("")
        self.Reference.set("")

        self.harvest.set("0")
        self.rotav.set("0")
        self.transport.set("0")
        self.seed.set("0")
        self.escort.set("0")
        self.dicoper.set("0")
        self.regent.set("0")
        self.opal.set("0")
        self.npk.set("0")
        self.zs.set("0")
        self.can.set("0")
        self.tsp.set("0")
        self.ssp.set("0")
        self.sa.set("0")

        self.Cost_of_Fertilizer.set("")
        self.Cost_of_Services.set("")
        self.Cost_of_FarmIn.set("")
        self.SubTotal.set("")
        self.Tax.set("")
        self.Total.set("")

        self.var1.set(0)
        self.var2.set(0)
        self.var3.set(0)
        self.var4.set(0)
        self.var5.set(0)
        self.var6.set(0)
        self.var7.set(0)
        self.var8.set(0)
        self.var9.set(0)
        self.var10.set(0)
        self.var11.set(0)
        self.var12.set(0)
        self.var13.set(0)
        self.var14.set(0)
        self.var15.set(0)
        self.var16.set(0)
        self.var17.set(0)
        self.var18.set(0)
        self.var19.set(0)

        self.harvesEntry.config(state=DISABLED)
        self.rotavEntry.config(state=DISABLED)
        self.transEntry.config(state=DISABLED)
        self.seedEntry.config(state=DISABLED)
        self.escortEntry.config(state=DISABLED)
        self.dicoperEntry.config(state=DISABLED)
        self.regentEntry.config(state=DISABLED)
        self.opalEntry.config(state=DISABLED)
        self.NPKEntry.config(state=DISABLED)
        self.ZSEntry.config(state=DISABLED)
        self.CANEntry.config(state=DISABLED)
        self.TSPEntry.config(state=DISABLED)
        self.SSPEntry.config(state=DISABLED)
        self.SAEntry.config(state=DISABLED)

        self.txtReceipt.delete("1.0", END)

    def generateRef(self, size, chars=string.ascii_uppercase + string.digits):
        Sqlite3_Backend.getCashRef()
        Sqlite3_Backend.getRef()
        return ''.join(random.choice(chars) for x in range(size))

    def Cost_of_Items(self):
        # Sqlite3_Backend.ServicePricesTable()
        # Sqlite3_Backend.FarmInPricesTable()
        # Sqlite3_Backend.FertPricesTable()
        # Sqlite3_Backend.OtherPricesTable()
        # _____________ Cost of Services _____
        item1 = float(self.harvest.get())
        item2 = float(self.rotavEntry.get())
        item3 = float(self.transport.get())
        item4 = float(self.seed.get())

        pricedata1 = Sqlite3_Backend.selectHarvest()
        for datum in pricedata1:
            priceitem1 = float(datum[0])
            break
        pricedata2 = Sqlite3_Backend.selectRotav()
        for datum in pricedata2:
            priceitem2 = float(datum[0])
            break
        pricedata3 = Sqlite3_Backend.selectTransport()
        for datum in pricedata3:
            priceitem3 = float(datum[0])
            break
        pricedata4 = Sqlite3_Backend.selectSeed()
        for datum in pricedata4:
            priceitem4 = float(datum[0])
            break
        # _____________ Cost of Farm Inputs ____
        item5 = float(self.escort.get())
        item6 = float(self.dicoper.get())
        item7 = float(self.regent.get())
        item8 = float(self.opal.get())

        pricedata5 = Sqlite3_Backend.selectEscort()
        for datum in pricedata5:
            priceitem5 = float(datum[0])
            break
        pricedata6 = Sqlite3_Backend.selectDicoper()
        for datum in pricedata6:
            priceitem6 = float(datum[0])
            break
        pricedata7 = Sqlite3_Backend.selectRegent()
        for datum in pricedata7:
            priceitem7 = float(datum[0])
            break
        pricedata8 = Sqlite3_Backend.selectOpal()
        for datum in pricedata8:
            priceitem8 = float(datum[0])
            break
        # _____________ Cost of Fertilizer _____
        item9 = float(self.npk.get())
        item10 = float(self.zs.get())
        item11 = float(self.can.get())
        item12 = float(self.tsp.get())
        item13 = float(self.ssp.get())
        item14 = float(self.sa.get())

        pricedata9 = Sqlite3_Backend.selectNPK()
        for datum in pricedata9:
            priceitem9 = float(datum[0])
            break
        pricedata10 = Sqlite3_Backend.selectZS()
        for datum in pricedata10:
            priceitem10 = float(datum[0])
            break
        pricedata11 = Sqlite3_Backend.selectCAN()
        for datum in pricedata11:
            priceitem11 = float(datum[0])
            break
        pricedata12 = Sqlite3_Backend.selectTSP()
        for datum in pricedata12:
            priceitem12 = float(datum[0])
            break
        pricedata13 = Sqlite3_Backend.selectSSP()
        for datum in pricedata13:
            priceitem13 = float(datum[0])
            break
        pricedata14 = Sqlite3_Backend.selectSA()
        for datum in pricedata14:
            priceitem14 = float(datum[0])
            break

        self.priceofServices = (item1 * priceitem1) + (item2 * priceitem2) + (item3 * priceitem3) + (item4 * priceitem4)
        self.priceofFarmIn = (item5 * priceitem5) + (item6 * priceitem6) + (item7 * priceitem7) + (item8 * priceitem8)
        self.priceofFert = (item9 * priceitem9) + (item10 * priceitem10) + (item11 * priceitem11) + (
                item12 * priceitem12) + (item13 * priceitem13) + (item14 * priceitem14)

        servicesPrice = "KShs " + str("%.2f" % (self.priceofServices))
        farminPrice = "KShs " + str("%.2f" % (self.priceofFarmIn))
        fertPrice = "KShs " + str("%.2f" % (self.priceofFert))

        self.Cost_of_Services.set(servicesPrice)
        self.Cost_of_Fertilizer.set(fertPrice)
        self.Cost_of_FarmIn.set(fertPrice)

        pricedata15 = Sqlite3_Backend.selectTax()
        for datum in pricedata15:
            priceitem15 = float(datum[0])
            break

        self.tax = ((self.priceofServices + self.priceofFert + self.priceofFarmIn) * priceitem15)
        paidtax = "KShs " + str("%.2f" % (self.tax))
        self.Tax.set(paidtax)

        subttl = (self.priceofServices + self.priceofFert + self.priceofFarmIn)
        subto = "KShs " + str("%.2f" % (subttl))
        self.SubTotal.set(subto)

        self.ttl = (self.priceofServices + self.priceofFert + self.priceofFarmIn + self.tax)
        tl = "KShs " + str("%.2f" % (self.ttl))
        self.Total.set(tl)

        self.Reference.set(self.generateRef(8, "QWERTYUIOPLKJHGFDASZXCVBNM0123456789"))

    def chkharvest(self):
        if (self.var1.get() == 1):
            self.harvesEntry.config(state=NORMAL)
            self.harvesEntry.focus()
            self.harvesEntry.delete('0', END)
            self.harvest.set("")
        elif (self.var1.get() == 0):
            self.harvesEntry.config(state=DISABLED)
            self.harvest.set("0")

    def chkrotav(self):
        if (self.var2.get() == 1):
            self.rotavEntry.config(state=NORMAL)
            self.rotavEntry.focus()
            self.rotavEntry.delete('0', END)
            self.rotav.set("")
        elif (self.var2.get() == 0):
            self.rotavEntry.config(state=DISABLED)
            self.rotav.set("0")

    def chktrans(self):
        if (self.var3.get() == 1):
            self.transEntry.config(state=NORMAL)
            self.transEntry.focus()
            self.transEntry.delete('0', END)
            self.transport.set("")
        elif (self.var3.get() == 0):
            self.transEntry.config(state=DISABLED)
            self.transport.set("0")

    def chkseed(self):
        if (self.var4.get() == 1):
            self.seedEntry.config(state=NORMAL)
            self.seedEntry.focus()
            self.seedEntry.delete('0', END)
            self.seed.set("")
        elif (self.var4.get() == 0):
            self.seedEntry.config(state=DISABLED)
            self.seed.set("0")

    def chkescort(self):
        if (self.var5.get() == 1):
            self.escortEntry.config(state=NORMAL)
            self.escortEntry.focus()
            self.escortEntry.delete('0', END)
            self.escort.set("")
        elif (self.var5.get() == 0):
            self.escortEntry.config(state=DISABLED)
            self.escort.set("0")

    def chkdicoper(self):
        if (self.var6.get() == 1):
            self.dicoperEntry.config(state=NORMAL)
            self.dicoperEntry.focus()
            self.dicoperEntry.delete('0', END)
            self.dicoper.set("")
        elif (self.var6.get() == 0):
            self.dicoperEntry.config(state=DISABLED)
            self.dicoper.set("0")

    def chkregent(self):
        if (self.var7.get() == 1):
            self.regentEntry.config(state=NORMAL)
            self.regentEntry.focus()
            self.regentEntry.delete('0', END)
            self.regent.set("")
        elif (self.var7.get() == 0):
            self.regentEntry.config(state=DISABLED)
            self.regent.set("0")

    def chkopal(self):
        if (self.var8.get() == 1):
            self.opalEntry.config(state=NORMAL)
            self.opalEntry.focus()
            self.opalEntry.delete('0', END)
            self.opal.set("")
        elif (self.var8.get() == 0):
            self.opalEntry.config(state=DISABLED)
            self.opal.set("0")

    def chknpk(self):
        if (self.var9.get() == 1):
            self.NPKEntry.config(state=NORMAL)
            self.NPKEntry.focus()
            self.NPKEntry.delete('0', END)
            self.npk.set("")
        elif (self.var9.get() == 0):
            self.NPKEntry.config(state=DISABLED)
            self.npk.set("0")

    def chkzs(self):
        if (self.var10.get() == 1):
            self.ZSEntry.config(state=NORMAL)
            self.ZSEntry.focus()
            self.ZSEntry.delete('0', END)
            self.zs.set("")
        elif (self.var10.get() == 0):
            self.ZSEntry.config(state=DISABLED)
            self.zs.set("0")

    def chkcan(self):
        if (self.var11.get() == 1):
            self.CANEntry.config(state=NORMAL)
            self.CANEntry.focus()
            self.CANEntry.delete('0', END)
            self.can.set("")
        elif (self.var11.get() == 0):
            self.CANEntry.config(state=DISABLED)
            self.can.set("0")

    def chktsp(self):
        if (self.var12.get() == 1):
            self.TSPEntry.config(state=NORMAL)
            self.TSPEntry.focus()
            self.TSPEntry.delete('0', END)
            self.tsp.set("")
        elif (self.var12.get() == 0):
            self.TSPEntry.config(state=DISABLED)
            self.tsp.set("0")

    def chkssp(self):
        if (self.var13.get() == 1):
            self.SSPEntry.config(state=NORMAL)
            self.SSPEntry.focus()
            self.SSPEntry.delete('0', END)
            self.ssp.set("")
        elif (self.var13.get() == 0):
            self.SSPEntry.config(state=DISABLED)
            self.ssp.set("0")

    def chksa(self):
        if (self.var14.get() == 1):
            self.SAEntry.config(state=NORMAL)
            self.SAEntry.focus()
            self.SAEntry.delete('0', END)
            self.sa.set("")
        elif (self.var14.get() == 0):
            self.SAEntry.config(state=DISABLED)
            self.sa.set("0")

    def chkprov_date(self):
        if (self.var17.get() == 1):
            self.provEntry.config(state=NORMAL)
            self.provEntry.focus()
            self.provEntry.delete('0', END)
            self.provision_date.set("")
        elif (self.var17.get() == 0):
            self.provEntry.config(state=DISABLED)
            self.provision_date.set("")

    def chkfuid(self):
        if (self.var18.get() == 1):
            self.fuidEntry.config(state=NORMAL)
            self.fuidEntry.focus()
            self.fuidEntry.delete('0', END)
            self.repfuid.set("")
        elif (self.var18.get() == 0):
            self.fuidEntry.config(state=DISABLED)
            self.repfuid.set("")

    def chkrefno(self):
        if (self.var19.get() == 1):
            self.refnoEntry.config(state=NORMAL)
            self.refnoEntry.focus()
            self.refnoEntry.delete('0', END)
            self.repref.set("")
        elif (self.var19.get() == 0):
            self.refnoEntry.config(state=DISABLED)
            self.repref.set("")

    def getReceipt(self):
        self.txtReceipt.delete("1.0", END)
        self.provision_date = time.strftime("%d/%m/%Y")
        self.txtReceipt.insert(END, "\tRice Farmer Association Official Receipt" + "\n")
        self.txtReceipt.insert(END,
                               "Receipt Ref:\t\t" + self.Reference.get() + "\t\tDate:\t" + self.provision_date + "\n")
        self.txtReceipt.insert(END, "Item:\t\t\t" + "Quantity\t\t" + "Cost" + "\n")
        self.txtReceipt.insert(END, "_____\t\t\t" + "_________\t\t" + "______" + "\n")
        if self.var1.get() == 1:
            self.txtReceipt.insert(END, "Harvesting\t\t\t" + self.harvest.get() + " acres" + "\t\t" + str(
                (float(self.harvest.get()) * 4500)) + "\n")
        if self.var2.get() == 1:
            self.txtReceipt.insert(END, "Rotavation\t\t\t" + self.rotav.get() + " acres" + "\t\t" + str(
                (float(self.rotav.get()) * 3500)) + "\n")
        if self.var3.get() == 1:
            self.txtReceipt.insert(END, "Transport\t\t\t" + self.transport.get() + " bags" + "\t\t" + str(
                (float(self.transport.get()) * 50)) + "\n")
        if self.var4.get() == 1:
            self.txtReceipt.insert(END, "Seed\t\t\t" + self.seed.get() + " bags" + "\t\t" + str(
                (float(self.seed.get()) * 5000)) + "\n")
        if self.var5.get() == 1:
            self.txtReceipt.insert(END, "Escort\t\t\t" + self.escort.get() + " 500ml" + "\t\t" + str(
                (float(self.escort.get()) * 500)) + "\n")
        if self.var6.get() == 1:
            self.txtReceipt.insert(END, "Dicoper\t\t\t" + self.dicoper.get() + " 100ml" + "\t\t" + str(
                (float(self.dicoper.get()) * 350)) + "\n")
        if self.var7.get() == 1:
            self.txtReceipt.insert(END, "Regent\t\t\t" + self.regent.get() + " 500ml" + "\t\t" + str(
                (float(self.regent.get()) * 500)) + "\n")
        if self.var8.get() == 1:
            self.txtReceipt.insert(END, "Opal\t\t\t" + self.opal.get() + " 250ml" + "\t\t" + str(
                (float(self.opal.get()) * 400)) + "\n")
        if self.var9.get() == 1:
            self.txtReceipt.insert(END, "N.P.K\t\t\t" + self.npk.get() + " 50Kg bags" + "\t\t" + str(
                (float(self.npk.get()) * 1500)) + "\n")
        if self.var10.get() == 1:
            self.txtReceipt.insert(END, "Z.S\t\t\t" + self.zs.get() + " 50Kg bags" + "\t\t" + str(
                (float(self.zs.get()) * 1700)) + "\n")
        if self.var11.get() == 1:
            self.txtReceipt.insert(END, "C.A.N\t\t\t" + self.can.get() + " 50Kg bags" + "\t\t" + str(
                (float(self.can.get()) * 1500)) + "\n")
        if self.var12.get() == 1:
            self.txtReceipt.insert(END, "T.S.P\t\t\t" + self.tsp.get() + " 50Kg bags" + "\t\t" + str(
                (float(self.tsp.get()) * 2000)) + "\n")
        if self.var13.get() == 1:
            self.txtReceipt.insert(END, "S.S.P\t\t\t" + self.ssp.get() + " 50Kg bags" + "\t\t" + str(
                (float(self.ssp.get()) * 1600)) + "\n")
        if self.var14.get() == 1:
            self.txtReceipt.insert(END, "S.A\t\t\t" + self.sa.get() + " 50Kg bags" + "\t\t" + str(
                (float(self.sa.get()) * 1800)) + "\n")
        self.txtReceipt.insert(END, "\t\t\t" + "\t\t" + "__________" + "\n")
        self.txtReceipt.insert(END, "SubTotal:\t\t" + "\t\t" + self.SubTotal.get() + "\n")
        self.txtReceipt.insert(END, "Tax:\t\t" + "\t\t" + self.Tax.get() + "\n")
        self.txtReceipt.insert(END, "\t\t\t" + "\t\t" + "__________" + "\n")
        self.txtReceipt.insert(END, "Total Cost:\t\t" + "\t\t" + self.Total.get() + "\n")
        if self.var16.get() == 1:
            self.txtReceipt.insert(END, "Payment Mode:\t\t" + "\t" + "Deduct on Produce Delivery" + "\n")
        if self.var15.get() == 1:
            self.txtReceipt.insert(END, "Payment Mode:\t\t" + "\t\t" + "Cash" + "\n")

    def iApprove(self):  # Should Add Records to the database and also print contents of the receipt
        self.provision_date = time.strftime("%d/%m/%Y")
        Sqlite3_Backend.serviceTable()
        Sqlite3_Backend.cashServiceTable()
        if self.Total.get() == "":
            tkinter.messagebox.showinfo("Null Record", "No Service Selected")
        else:
            if self.var16.get() == 1:  # For RFA Members
                data = Sqlite3_Backend.getsurid(self.fuid.get())
                # First confirm if the customer is a member of RFA
                if data == []:  # Not a Member
                    tkinter.messagebox.showinfo("Not a Member", "The Customer can get the services on cash basis")
                else:  # A member, Add record to the database
                    self.surname.set(data[0][0])
                    self.iDNo.set(data[0][1])
                    confirm = tkinter.messagebox.askyesno("Approve",
                                                          "Confirm\nTo Approve Service Provision on DoD basis")
                    if confirm > 0:
                        Sqlite3_Backend.addService(self.Reference.get(), self.fuid.get(), self.surname.get(),
                                                   self.provision_date, self.priceofServices, \
                                                   self.priceofFert, self.priceofFarmIn, self.tax, self.ttl)
                        tkinter.messagebox.showinfo("Successful", "Service Approved Successfully")
                        return
                    else:
                        return
            elif self.var15.get() == 1:  # For cash customers/ walk in customers
                # Add record to the tables that stores services for walk in customers
                confirm = tkinter.messagebox.askyesno("Approve", "Confirm\nTo Approve Service Provision on Cash basis")
                if confirm > 0:
                    Sqlite3_Backend.addCashService(self.Reference.get(), self.provision_date,
                                                   self.Cost_of_Services.get(), self.Cost_of_Fertilizer.get(), \
                                                   self.Cost_of_FarmIn.get(), self.Tax.get(), self.Total.get())
                    tkinter.messagebox.showinfo("Successful", "Service Approved Successfully")
                    return
                else:
                    return

    def iEnquire(self):
        if self.var16.get() == 1:
            data = Sqlite3_Backend.listServiceData()
            if data == []:
                tkinter.messagebox.showinfo("Reports", "Report Enquired Not Found")
                return
            else:
                tt = time.strftime("%d%m%Y")
                root6 = Tk()
                root6.title("Reports")
                menubar = Menu(root6)
                filemenu = Menu(menubar, tearoff=0)
                filemenu.add_command(label="Print")
                filemenu.add_command(label="Save As", command=lambda: canvas.save(tt.txt))
                filemenu.add_command(label="Close")
                filemenu.add_separator()
                filemenu.add_command(label="Exit", command=lambda: root6.destroy())

                menubar.add_cascade(label="File", menu=filemenu)
                frame = Frame(root6)
                canvas = Canvas(frame, height=350, width=1000)
                scrollbar = Scrollbar(frame, orient=VERTICAL, command=canvas.yview)
                scrollbarx = Scrollbar(frame, orient=HORIZONTAL, command=canvas.xview)
                scrollable_frame = Frame(canvas)

                scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

                canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
                canvas.configure(yscrollcommand=scrollbar.set)
                canvas.configure(xscrollcommand=scrollbarx.set)

                headers = ['', 'Ref', 'FUID', 'Surname', 'Date', 'Services', 'Fertilizer', 'Other Inputs', 'Tax',
                           'Total']
                colh = len(headers)
                for h1 in range(colh):
                    label = Label(scrollable_frame, width=10, font=('ALGERIAN', 12, 'bold'), text=headers[h1])
                    label.grid(row=0, column=h1)
                total_rows = len(data)
                total_columns = len(data[0])
                for i in range(total_rows):
                    for j in range(total_columns):
                        e = Entry(scrollable_frame, width=10, fg='blue', font=('Arial', 14))
                        e.grid(row=i + 1, column=j)
                        e.insert(END, data[i][j])
                frame.pack()
                canvas.grid(row=0, column=0)
                scrollbar.grid(row=0, column=1, sticky=NS)
                scrollbarx.grid(row=1, column=0, sticky=EW)

                root6.config(menu=menubar)

        elif self.var15.get() == 1:
            data = Sqlite3_Backend.listCashData()
            if data == []:
                tkinter.messagebox.showinfo("Reports", "Report Enquired not Found")
                return
            else:
                root11 = Tk()
                root11.title("Reports")
                menubar = Menu(root11)
                filemenu = Menu(menubar, tearoff=0)
                filemenu.add_command(label="Print")
                filemenu.add_command(label="Save")
                filemenu.add_command(label="Save As")
                filemenu.add_command(label="Close")
                filemenu.add_separator()
                filemenu.add_command(label="Exit")

                menubar.add_cascade(label="File", menu=filemenu)
                frame = Frame(root11)
                canvas = Canvas(frame, height=350, width=1000)
                scrollbar = Scrollbar(frame, orient=VERTICAL, command=canvas.yview)
                scrollbarx = Scrollbar(frame, orient=HORIZONTAL, command=canvas.xview)
                scrollable_frame = Frame(canvas)

                scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

                canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
                canvas.configure(yscrollcommand=scrollbar.set)
                canvas.configure(xscrollcommand=scrollbarx.set)

                headers = ['', 'Ref', 'Date', 'Services', 'Fertilizer', 'Other Inputs', 'Tax', 'Total']
                colh = len(headers)
                for h1 in range(colh):
                    label = Label(scrollable_frame, width=10, font=('ALGERIAN', 12, 'bold'), text=headers[h1])
                    label.grid(row=0, column=h1)
                total_rows = len(data)
                total_columns = len(data[0])
                for i in range(total_rows):
                    for j in range(total_columns):
                        e = Entry(scrollable_frame, width=15, fg='blue', font=('Arial', 14))
                        e.grid(row=i + 1, column=j)
                        e.insert(END, data[i][j])
                frame.pack()
                canvas.grid(row=0, column=0)
                scrollbar.grid(row=0, column=1, sticky=NS)
                scrollbarx.grid(row=1, column=0, sticky=EW)

                root11.config(menu=menubar)

    def iSearch(self):
        if self.var17.get() == 1 and self.var15.get() == 0 and self.var16.get() == 1:
            data = Sqlite3_Backend.dateSearchService(self.provision_date.get())
            if data == []:
                tkinter.messagebox.showinfo("Reports", "Report Enquired not Found")
                return
            else:
                root7 = Tk()
                root7.title("Reports")
                menubar = Menu(root7)
                filemenu = Menu(menubar, tearoff=0)
                filemenu.add_command(label="Print")
                filemenu.add_command(label="Save")
                filemenu.add_command(label="Save As")
                filemenu.add_command(label="Close")
                filemenu.add_separator()
                filemenu.add_command(label="Exit")

                menubar.add_cascade(label="File", menu=filemenu)
                repText = Text(root7, font=('arial', 12, 'bold'), width=120)
                repText.pack()
                for datum in data:
                    repText.insert(END, datum)
                    repText.insert(END, "\n")

                root7.config(menu=menubar)
        elif self.var18.get() == 1:
            data = Sqlite3_Backend.fuidSearchService(self.repfuid.get())
            if data == []:
                tkinter.messagebox.showinfo("Reports", "Report Enquired not Found")
                return
            else:
                root8 = Tk()
                root8.title("Reports")
                menubar = Menu(root8)
                filemenu = Menu(menubar, tearoff=0)
                filemenu.add_command(label="Print")
                filemenu.add_command(label="Save")
                filemenu.add_command(label="Save As")
                filemenu.add_command(label="Close")
                filemenu.add_separator()
                filemenu.add_command(label="Exit")

                menubar.add_cascade(label="File", menu=filemenu)
                repText = Text(root8, font=('arial', 12, 'bold'), width=120)
                repText.pack()
                for datum in data:
                    repText.insert(END, datum)
                    repText.insert(END, "\n")

                root8.config(menu=menubar)

        elif self.var19.get() == 1 and self.var15.get() == 0 and self.var16.get() == 1:
            data = Sqlite3_Backend.refSearchService(self.repref.get())
            if data == []:
                tkinter.messagebox.showinfo("Reports", "Report Enquired Not Found")
                return
            else:
                root9 = Tk()
                root9.title("Reports")
                menubar = Menu(root9)
                filemenu = Menu(menubar, tearoff=0)
                filemenu.add_command(label="Print")
                filemenu.add_command(label="Save")
                filemenu.add_command(label="Save As")
                filemenu.add_command(label="Close")
                filemenu.add_separator()
                filemenu.add_command(label="Exit")

                menubar.add_cascade(label="File", menu=filemenu)
                repText = Text(root9, font=('arial', 12, 'bold'), width=120)
                repText.pack()
                for datum in data:
                    repText.insert(END, datum)
                    repText.insert(END, "\n")

                root9.config(menu=menubar)
        elif self.var15.get() == 1 and self.var19.get() == 1 and self.var16.get() == 0:
            data = Sqlite3_Backend.searchCashService(self.repref.get())
            if data == []:
                tkinter.messagebox.showinfo("Reports", "Report Enquired Not Found")
            else:
                root10 = Tk()
                root10.title("Reports")
                menubar = Menu(root10)
                filemenu = Menu(menubar, tearoff=0)
                filemenu.add_command(label="Print")
                filemenu.add_command(label="Save")
                filemenu.add_command(label="Save As")
                filemenu.add_command(label="Close")
                filemenu.add_separator()
                filemenu.add_command(label="Exit")

                menubar.add_cascade(label="File", menu=filemenu)
                repText = Text(root10, font=('arial', 12, 'bold'), width=120)
                repText.pack()
                for datum in data:
                    repText.insert(END, datum)
                    repText.insert(END, "\n")

                root10.config(menu=menubar)
        if self.var17.get() == 1 and self.var15.get() == 1 and self.var16.get() == 0:
            data = Sqlite3_Backend.dateCashService(self.provision_date.get())
            if data == []:
                tkinter.messagebox.showinfo("Reports", "Report Enquired not Found")
                return
            else:
                root12 = Tk()
                root12.title("Reports")
                menubar = Menu(root12)
                filemenu = Menu(menubar, tearoff=0)
                filemenu.add_command(label="Print")
                filemenu.add_command(label="Save")
                filemenu.add_command(label="Save As")
                filemenu.add_command(label="Close")
                filemenu.add_separator()
                filemenu.add_command(label="Exit")

                menubar.add_cascade(label="File", menu=filemenu)
                repText = Text(root12, font=('arial', 12, 'bold'), width=120)
                repText.pack()
                for datum in data:
                    repText.insert(END, datum)
                    repText.insert(END, "\n")

                root12.config(menu=menubar)

    def iExit(self):
        confirm = tkinter.messagebox.askyesno("Service Provision", "Confirm to Exit Window")
        if confirm > 0:
            self.root5.destroy()
            return

    def sel(self):
        if self.var15.get() == 1:
            self.var16.set(0)

    def sel1(self):
        if self.var16.get() == 1:
            self.var15.set(0)

    def widgets(self, root5):
        self.root5 = root5
        self.root5.geometry("1350x750+0+0")
        self.root5.config(bg='light green')
        self.root5.title("Service Provision and Reports")

        # ______________________ Frames ___________________________
        self.titleFrame = Frame(root5, bg='powder blue', relief=RIDGE)
        self.titleFrame.pack(side=TOP)

        self.mainFrame = Frame(root5, bg='Ghost White', bd=15, relief=RIDGE)
        self.mainFrame.pack(side=TOP)

        self.farmDet = Frame(self.mainFrame, bg="Ghost White", bd=0, relief=RIDGE, pady=10)
        self.farmDet.pack(side=TOP)

        self.frameLeft = Frame(self.mainFrame, bd=0, relief=RIDGE, pady=10)
        self.frameLeft.pack(side=LEFT)
        self.frameSvcs = Frame(self.frameLeft, bg="powder blue", bd=10, relief=RIDGE, pady=10)
        self.frameSvcs.grid(row=0, column=0, sticky=W)
        self.frameInputs = Frame(self.frameLeft, bg="powder blue", bd=10, relief=RIDGE, pady=10)
        self.frameInputs.grid(row=0, column=1, sticky=W)
        self.frameCost = Frame(self.frameLeft, bg="powder blue", bd=10, relief=RIDGE, pady=10)
        self.frameCost.grid(row=1, column=0, columnspan=2)

        self.frameRight = Frame(self.mainFrame, bg="Ghost White", bd=0, relief=RIDGE)
        self.frameRight.pack(side=RIGHT)
        self.repFrame = Frame(self.frameRight, bg="powder blue", bd=10, relief=RIDGE)
        self.repFrame.grid(row=0)
        self.btn2Frame = Frame(self.frameRight, bg="powder blue", bd=5, relief=RIDGE)
        self.btn2Frame.grid(row=2)
        self.receiptFrame = Frame(self.frameRight, bg="powder blue", bd=10, relief=RIDGE)
        self.receiptFrame.grid(row=1)
        self.btnFrame = Frame(self.frameRight, bg="powder blue", bd=10, relief=RIDGE)
        self.btnFrame.grid(row=3)

        # _________________ Title Label _____________________
        self.lblTitle = Label(self.titleFrame, font=('arial', 30, 'bold'), text="RFA Service Provision and Reports",
                              bd=10, bg='light green', justify=CENTER)
        self.lblTitle.grid(row=0, column=0)

        self.fuidlbl = Label(self.farmDet, text="Farmer UID", font=("arial", 20, "bold"), padx=10, pady=4,
                             bg="Ghost White")
        self.fuidlbl.grid(row=0, column=0)
        self.fuidEntry = Entry(self.farmDet, font=("arial", 18, "bold"), textvariable=self.fuid, width=15, bd=2)
        self.fuidEntry.grid(row=0, column=1)

        self.surlbl = Label(self.farmDet, text="Surname", font=("arial", 20, "bold"), padx=10, pady=4, bg="Ghost White")
        self.surlbl.grid(row=0, column=2)
        self.surEntry = Entry(self.farmDet, font=("arial", 18, "bold"), textvariable=self.surname, width=15, bd=2,
                              state=DISABLED)
        self.surEntry.grid(row=0, column=3)

        self.idlbl = Label(self.farmDet, text="ID Number", font=("arial", 20, "bold"), padx=10, pady=4,
                           bg="Ghost White")
        self.idlbl.grid(row=0, column=4)
        self.idEntry = Entry(self.farmDet, font=("arial", 18, "bold"), textvariable=self.iDNo, width=15, bd=2,
                             state=DISABLED)
        self.idEntry.grid(row=0, column=5, padx=10)

        self.reflbl = Label(self.frameSvcs, text="Reference Number", font=("arial", 19, "bold"), bg='powder blue')
        self.reflbl.grid(row=0, column=0)
        self.refEntry = Entry(self.frameSvcs, font=("arial", 18, "bold"), textvariable=self.Reference, width=10, bd=5,
                              state=DISABLED)
        self.refEntry.grid(row=0, column=1, padx=5)

        # ________________________ Services Checkbuttons ____________________________________________________________________
        self.harvestlbl = Checkbutton(self.frameSvcs, text="Harvesting", variable=self.var1, onvalue=1, offvalue=0,
                                      font=('arial', 16, 'bold'), \
                                      bg='powder blue', command=self.chkharvest).grid(row=1, padx=20, sticky=W)
        self.rotavlbl = Checkbutton(self.frameSvcs, text="Rotavation", variable=self.var2, onvalue=1, offvalue=0,
                                    font=('arial', 16, 'bold'), \
                                    bg='powder blue', command=self.chkrotav).grid(row=2, padx=20, sticky=W)
        self.translbl = Checkbutton(self.frameSvcs, text="Transport", variable=self.var3, onvalue=1, offvalue=0,
                                    font=('arial', 16, 'bold'), \
                                    bg='powder blue', command=self.chktrans).grid(row=3, padx=20, sticky=W)
        self.seedlbl = Checkbutton(self.frameSvcs, text="Seed Provision", variable=self.var4, onvalue=1, offvalue=0,
                                   font=('arial', 16, 'bold'), \
                                   bg='powder blue', command=self.chkseed).grid(row=4, padx=20, sticky=W)

        # ________________________ Services Entries ____________________________________________________________________
        self.harvesEntry = Entry(self.frameSvcs, font=('arial', 16, 'bold'), textvariable=self.harvest, bd=5, width=6,
                                 justify=LEFT, state=DISABLED)
        self.harvesEntry.grid(row=1, column=1)
        self.rotavEntry = Entry(self.frameSvcs, font=('arial', 16, 'bold'), bd=5, textvariable=self.rotav, width=6,
                                justify=LEFT, state=DISABLED)
        self.rotavEntry.grid(row=2, column=1)
        self.transEntry = Entry(self.frameSvcs, font=('arial', 16, 'bold'), bd=5, width=6, textvariable=self.transport,
                                justify=LEFT, state=DISABLED)
        self.transEntry.grid(row=3, column=1)
        self.seedEntry = Entry(self.frameSvcs, font=('arial', 16, 'bold'), bd=5, width=6, textvariable=self.seed,
                               justify=LEFT, state=DISABLED)
        self.seedEntry.grid(row=4, column=1)
        # _______________________________ Other Inputs _________________________________________________________
        self.inputlbl = Label(self.frameSvcs, text="Other Farm Inputs", font=("arial", 19, "bold"), bg='powder blue')
        self.inputlbl.grid(row=5, column=0, sticky=W)

        self.escortlbl = Checkbutton(self.frameSvcs, text="Escort 500ml", variable=self.var5, onvalue=1, offvalue=0,
                                     font=('arial', 16, 'bold'), \
                                     bg='powder blue', command=self.chkescort).grid(row=6, padx=20, sticky=W)
        self.dicoperlbl = Checkbutton(self.frameSvcs, text="Dicoper 100ml", variable=self.var6, onvalue=1, offvalue=0,
                                      font=('arial', 16, 'bold'), \
                                      bg='powder blue', command=self.chkdicoper).grid(row=7, padx=20, sticky=W)
        self.Regentlbl = Checkbutton(self.frameSvcs, text="Regent 250ml", variable=self.var7, onvalue=1, offvalue=0,
                                     font=('arial', 16, 'bold'), \
                                     bg='powder blue', command=self.chkregent).grid(row=8, padx=20, sticky=W)
        self.opallbl = Checkbutton(self.frameSvcs, text="Opal 500ml", variable=self.var8, onvalue=1, offvalue=0,
                                   font=('arial', 16, 'bold'), \
                                   bg='powder blue', command=self.chkopal).grid(row=9, padx=20, sticky=W)
        # _______________________________ Other Inputs Entries_________________________________________________________
        self.escortEntry = Entry(self.frameSvcs, font=('arial', 16, 'bold'), bd=5, textvariable=self.escort, width=6,
                                 justify=LEFT, state=DISABLED)
        self.escortEntry.grid(row=6, column=1)
        self.dicoperEntry = Entry(self.frameSvcs, font=('arial', 16, 'bold'), bd=5, width=6, textvariable=self.dicoper,
                                  justify=LEFT, state=DISABLED)
        self.dicoperEntry.grid(row=7, column=1)
        self.regentEntry = Entry(self.frameSvcs, font=('arial', 16, 'bold'), bd=5, width=6, textvariable=self.regent,
                                 justify=LEFT, state=DISABLED)
        self.regentEntry.grid(row=8, column=1)
        self.opalEntry = Entry(self.frameSvcs, font=('arial', 16, 'bold'), bd=5, width=6, textvariable=self.opal,
                               justify=LEFT, state=DISABLED)
        self.opalEntry.grid(row=9, column=1)

        # _______________________________ Fertilizers Checkbuttons_________________________________________________________
        self.fertlbl = Label(self.frameInputs, text="Fertilizers", font=("arial", 19, "bold"), bg='powder blue')
        self.fertlbl.grid(row=0, column=0, sticky=W)

        self.NPKlbl = Checkbutton(self.frameInputs, text="N.P.K 50Kgs", variable=self.var9, onvalue=1, offvalue=0,
                                  font=('arial', 16, 'bold'), \
                                  bg='powder blue', command=self.chknpk).grid(row=1, padx=20, sticky=W)
        self.ZSlbl = Checkbutton(self.frameInputs, text="Zinc Sulphate 50Kgs", variable=self.var10, onvalue=1,
                                 offvalue=0, font=('arial', 16, 'bold'), \
                                 bg='powder blue', command=self.chkzs).grid(row=2, padx=20, sticky=W)
        self.CANlbl = Checkbutton(self.frameInputs, text="C.A.N 50Kgs", variable=self.var11, onvalue=1, offvalue=0,
                                  font=('arial', 16, 'bold'), \
                                  bg='powder blue', command=self.chkcan).grid(row=3, padx=20, sticky=W)
        self.TSPlbl = Checkbutton(self.frameInputs, text="T.S.P 50Kgs", variable=self.var12, onvalue=1, offvalue=0,
                                  font=('arial', 16, 'bold'), \
                                  bg='powder blue', command=self.chktsp).grid(row=4, padx=20, sticky=W)
        self.SSPlbl = Checkbutton(self.frameInputs, text="S.S.P 50Kgs", variable=self.var13, onvalue=1, offvalue=0,
                                  font=('arial', 16, 'bold'), \
                                  bg='powder blue', command=self.chkssp).grid(row=5, padx=20, sticky=W)
        self.SAlbl = Checkbutton(self.frameInputs, text="S.A 50Kgs", variable=self.var14, onvalue=1, offvalue=0,
                                 font=('arial', 16, 'bold'), \
                                 bg='powder blue', command=self.chksa).grid(row=6, padx=20, sticky=W)

        # _______________________________ Fertilizers Entries________________________________________________________
        self.NPKEntry = Entry(self.frameInputs, font=('arial', 16, 'bold'), bd=5, textvariable=self.npk, width=6,
                              justify=LEFT, state=DISABLED)
        self.NPKEntry.grid(row=1, column=1, padx=10)
        self.ZSEntry = Entry(self.frameInputs, font=('arial', 16, 'bold'), bd=5, textvariable=self.zs, width=6,
                             justify=LEFT, state=DISABLED)
        self.ZSEntry.grid(row=2, column=1, padx=10)
        self.CANEntry = Entry(self.frameInputs, font=('arial', 16, 'bold'), bd=5, textvariable=self.can, width=6,
                              justify=LEFT, state=DISABLED)
        self.CANEntry.grid(row=3, column=1, padx=10)
        self.TSPEntry = Entry(self.frameInputs, font=('arial', 16, 'bold'), bd=5, textvariable=self.tsp, width=6,
                              justify=LEFT, state=DISABLED)
        self.TSPEntry.grid(row=4, column=1, padx=10)
        self.SSPEntry = Entry(self.frameInputs, font=('arial', 16, 'bold'), bd=5, textvariable=self.ssp, width=6,
                              justify=LEFT, state=DISABLED)
        self.SSPEntry.grid(row=5, column=1, padx=10)
        self.SAEntry = Entry(self.frameInputs, font=('arial', 16, 'bold'), bd=5, textvariable=self.sa, width=6,
                             justify=LEFT, state=DISABLED)
        self.SAEntry.grid(row=6, column=1, padx=10)
        # _______________________________ Mode of Payment ________________________________________________________
        self.paymentlbl = Label(self.frameInputs, text="Mode of Payment", font=("arial", 19, "bold"), bg='powder blue')
        self.paymentlbl.grid(row=7, column=0, sticky=W)

        self.cashlbl = Checkbutton(self.frameInputs, text="Cash Payment", variable=self.var15, onvalue=1, offvalue=0,
                                   font=('arial', 16, 'bold'), \
                                   bg='powder blue', command=self.sel).grid(row=8, padx=20, sticky=W)
        self.nocashlbl = Checkbutton(self.frameInputs, text="Deduct on Delivery", variable=self.var16, onvalue=1,
                                     offvalue=0, font=('arial', 16, 'bold'), bg='powder blue', command=self.sel1) \
            .grid(row=9, padx=20, sticky=W)
        # _______________________________ Costs ________________________________________________________
        self.svcsCostlbl = Label(self.frameCost, font=('arial', 14, 'bold'), text="  Cost of Services\t",
                                 bg='powder blue', fg='black')
        self.svcsCostlbl.grid(row=0, column=0, sticky=W)
        self.svcsCosttxt = Entry(self.frameCost, insertwidth=2, textvariable=self.Cost_of_Services, bg='white',
                                 font=('arial', 12, 'bold'), justify=RIGHT, bd=7)
        self.svcsCosttxt.grid(row=0, column=1, padx=12)

        self.fertCostlbl = Label(self.frameCost, font=('arial', 14, 'bold'), text="  Cost of Fertilizers\t",
                                 bg='powder blue', fg='black')
        self.fertCostlbl.grid(row=1, column=0, sticky=W)
        self.fertCosttxt = Entry(self.frameCost, insertwidth=2, textvariable=self.Cost_of_Fertilizer, bg='white',
                                 font=('arial', 12, 'bold'), justify=RIGHT, bd=7)
        self.fertCosttxt.grid(row=1, column=1, padx=12)

        self.farmInlbl = Label(self.frameCost, font=('arial', 14, 'bold'), text="  Farm Inputs Cost\t",
                               bg='powder blue', fg='black')
        self.farmInlbl.grid(row=2, column=0, sticky=W)
        self.farmIntxt = Entry(self.frameCost, insertwidth=2, bg='white', textvariable=self.Cost_of_FarmIn,
                               font=('arial', 12, 'bold'), justify=RIGHT, bd=7)
        self.farmIntxt.grid(row=2, column=1, padx=12)

        self.subTotallbl = Label(self.frameCost, font=('arial', 14, 'bold'), text="  Sub Total\t", bg='powder blue',
                                 fg='black')
        self.subTotallbl.grid(row=0, column=2, sticky=W)
        self.subTotaltxt = Entry(self.frameCost, insertwidth=2, textvariable=self.SubTotal, bg='white',
                                 font=('arial', 12, 'bold'), justify=RIGHT, bd=7)
        self.subTotaltxt.grid(row=0, column=3)

        self.taxlbl = Label(self.frameCost, font=('arial', 14, 'bold'), text="  Tax\t", bg='powder blue', fg='black')
        self.taxlbl.grid(row=1, column=2, sticky=W)
        self.taxtxt = Entry(self.frameCost, insertwidth=2, textvariable=self.Tax, bg='white',
                            font=('arial', 12, 'bold'), justify=RIGHT, bd=7)
        self.taxtxt.grid(row=1, column=3)

        self.totallbl = Label(self.frameCost, font=('arial', 14, 'bold'), text="  Total\t", bg='powder blue',
                              fg='black')
        self.totallbl.grid(row=2, column=2, sticky=W)
        self.totaltxt = Entry(self.frameCost, insertwidth=2, textvariable=self.Total, bg='white',
                              font=('arial', 12, 'bold'), justify=RIGHT, bd=7)
        self.totaltxt.grid(row=2, column=3)

        # _______________________________ Reports ________________________________________________________
        self.reportlbl = Label(self.repFrame, text="Reports, Search by:", font=("arial", 19, "bold"), bg='powder blue')
        self.reportlbl.grid(row=0, column=0, sticky=W)

        self.prov_datelbl = Checkbutton(self.repFrame, text="Provision Date\t", variable=self.var17, onvalue=1,
                                        offvalue=0, font=('arial', 16, 'bold'), \
                                        bg='powder blue', command=self.chkprov_date).grid(row=1, padx=20, sticky=W)
        self.fuidlbl = Checkbutton(self.repFrame, text="Famer UID\t", variable=self.var18, onvalue=1, offvalue=0,
                                   font=('arial', 16, 'bold'), \
                                   bg='powder blue', command=self.chkfuid).grid(row=2, padx=20, sticky=W)
        self.refnolbl = Checkbutton(self.repFrame, text="Reference Number\t", variable=self.var19, onvalue=1,
                                    offvalue=0, font=('arial', 16, 'bold'), \
                                    bg='powder blue', command=self.chkrefno).grid(row=3, padx=20, sticky=W)

        self.provEntry = Entry(self.repFrame, font=('arial', 16, 'bold'), bd=5, width=16,
                               textvariable=self.provision_date, justify=LEFT, state=DISABLED)
        self.provEntry.grid(row=1, column=1, padx=10)
        self.fuidEntry = Entry(self.repFrame, font=('arial', 16, 'bold'), bd=5, textvariable=self.repfuid, width=16,
                               justify=LEFT, state=DISABLED)
        self.fuidEntry.grid(row=2, column=1, padx=10)
        self.refnoEntry = Entry(self.repFrame, font=('arial', 16, 'bold'), bd=5, textvariable=self.repref, width=16,
                                justify=LEFT, state=DISABLED)
        self.refnoEntry.grid(row=3, column=1, padx=10)

        # ______________________________________ Report Buttons__________________________________________________

        self.btnSearch = Button(self.btn2Frame, font=('arial', 16, 'bold'), bd=5, text="Search", width=8,
                                command=self.iSearch)
        self.btnSearch.grid(row=4, column=0, padx=8)
        self.btnReset = Button(self.btn2Frame, font=('arial', 16, 'bold'), bd=5, text="Reset", width=8,
                               command=self.iReset)
        self.btnReset.grid(row=4, column=1, padx=3)
        self.btnDisplay = Button(self.btn2Frame, font=('arial', 16, 'bold'), bd=5, text="View All Services", width=16,
                                 command=self.iEnquire)
        self.btnDisplay.grid(row=4, column=2, padx=8)

        # ______________________________________ Service Buttons__________________________________________________

        self.txtReceipt = Text(self.receiptFrame, width=54, height=12, bg='white', bd=4, font=('arial', 12, 'bold'))
        self.txtReceipt.grid(row=0, column=0)

        self.btnTotal = Button(self.btnFrame, font=('arial', 16, 'bold'), bd=5, text="Total", width=8,
                               command=self.Cost_of_Items)
        self.btnTotal.grid(row=0, column=0, padx=2)
        self.btnApprove = Button(self.btnFrame, font=('arial', 16, 'bold'), bd=5, text="Approve", width=8,
                                 command=self.iApprove)
        self.btnApprove.grid(row=0, column=1, padx=2)
        self.btnReceipt = Button(self.btnFrame, font=('arial', 16, 'bold'), bd=5, text="Receipt", width=8,
                                 command=self.getReceipt)
        self.btnReceipt.grid(row=0, column=2, padx=2)
        self.btnExit = Button(self.btnFrame, font=('arial', 16, 'bold'), bd=5, text="Exit", width=8, command=self.iExit)
        self.btnExit.grid(row=0, column=3, padx=2)


def main():
    root = Tk()
    runx = Service_Provision()
    runx.widgets(root)
    root.mainloop()


main()
