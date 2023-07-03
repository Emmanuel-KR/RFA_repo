from tkinter import *
import tkinter.messagebox
import Sqlite3_Backend


class Register_Update:
    global uid
    global surname
    global f_name
    global l_name
    global id_number
    global gender
    global tel
    global address
    global location
    global no_of_acres

    # ========================================== Functions =====================================================================================
    def addData(self):
        Sqlite3_Backend.farmerTable()
        if (len(self.surEnt.get()) != 0 and len(self.fnameEnt.get()) != 0 and len(self.lnameEnt.get()) != 0 and len(
                self.idEnt.get()) != 0 and len(self.genEnt.get()) != 0 \
                and len(self.telEnt.get()) != 0 and len(self.addrEnt.get()) != 0 and len(
                    self.locEnt.get()) != 0 and len(self.acreEnt.get()) != 0):
            confirm = tkinter.messagebox.askyesno("Add New Record", "Confirm to add a new Record")
            if confirm > 0:
                Sqlite3_Backend.addRecord(self.surEnt.get().capitalize(), self.fnameEnt.get().capitalize(),
                                          self.lnameEnt.get().capitalize(), self.idEnt.get(),
                                          self.genEnt.get().capitalize(), self.telEnt.get(), self.addrEnt.get(),
                                          self.locEnt.get().capitalize(), self.acreEnt.get())
                uid = Sqlite3_Backend.insertid(self.idEnt.get())
                self.farmerlist.delete(0, END)
                self.farmerlist.insert(END, (
                uid, self.surEnt.get(), self.fnameEnt.get(), self.lnameEnt.get(), self.idEnt.get(), self.genEnt.get(),
                self.telEnt.get(), self.addrEnt.get(),
                self.locEnt.get(), self.acreEnt.get()))
                self.clearFields()
                tkinter.messagebox.showinfo("Successful", "Record Added Successfully")
            else:
                return
        elif (len(self.surEnt.get()) == 0 or len(self.fnameEnt.get()) == 0 or len(self.lnameEnt.get()) == 0 or len(
                self.idEnt.get()) == 0 or len(self.genEnt.get()) == 0 \
              or len(self.telEnt.get()) == 0 or len(self.addrEnt.get()) == 0 or len(self.locEnt.get()) == 0 or len(
                    self.acreEnt.get()) == 0):
            tkinter.messagebox.showerror("Error", "All Fields Must be Filled")

    def updateRecord(self):
        if (len(self.surEnt.get()) != 0 and len(self.fnameEnt.get()) != 0 and len(self.lnameEnt.get()) != 0 and len(
                self.idEnt.get()) != 0 and len(self.genEnt.get()) != 0 \
                and len(self.telEnt.get()) != 0 and len(self.addrEnt.get()) != 0 and len(self.locEnt.get()) != 0):
            confirm = tkinter.messagebox.askyesno("Record Update", "Confirm to Update Record")
            if confirm > 0:
                Sqlite3_Backend.updateDB(self.surEnt.get(), self.fnameEnt.get(), self.lnameEnt.get(), self.idEnt.get(),
                                         self.genEnt.get(), self.telEnt.get(), self.addrEnt.get(),
                                         self.locEnt.get(), self.acreEnt.get(), self.fidEnt.get())
                self.farmerlist.delete(0, END)
                uid = Sqlite3_Backend.insertid(self.idEnt.get())
                self.farmerlist.insert(END, (
                uid, self.surEnt.get(), self.fnameEnt.get(), self.lnameEnt.get(), self.idEnt.get(), self.genEnt.get(),
                self.telEnt.get(), self.addrEnt.get(),
                self.locEnt.get(), self.acreEnt.get()))
                self.clearFields()
                tkinter.messagebox.showinfo("Successful", "Record Updated Successfully")
            else:
                return
        elif (len(self.surEnt.get()) == 0 or len(self.fnameEnt.get()) == 0 or len(self.lnameEnt.get()) == 0 or len(
                self.idEnt.get()) == 0 or len(self.genEnt.get()) == 0 \
              or len(self.telEnt.get()) == 0 or len(self.addrEnt.get()) == 0 or len(self.locEnt.get()) == 0 or len(
                    self.acreEnt.get()) == 0):
            tkinter.messagebox.showerror("Error", "All Fields Must be Filled")

    def clearFields(self):
        self.fidEnt.delete(0, END)
        self.surEnt.delete(0, END)
        self.fnameEnt.delete(0, END)
        self.lnameEnt.delete(0, END)
        self.idEnt.delete(0, END)
        self.genEnt.delete(0, END)
        self.telEnt.delete(0, END)
        self.addrEnt.delete(0, END)
        self.locEnt.delete(0, END)
        self.acreEnt.delete(0, END)

    def farmerRec(self, event):  # ____To make listbox functional_____
        global lbselect
        searchfm = self.farmerlist.curselection()[0]
        lbselect = self.farmerlist.get(searchfm)
        self.fidEnt.delete(0, END)
        self.fidEnt.insert(END, lbselect[0])
        self.surEnt.delete(0, END)
        self.surEnt.insert(END, lbselect[1])
        self.fnameEnt.delete(0, END)
        self.fnameEnt.insert(END, lbselect[2])
        self.lnameEnt.delete(0, END)
        self.lnameEnt.insert(END, lbselect[3])
        self.idEnt.delete(0, END)
        self.idEnt.insert(END, lbselect[4])
        self.genEnt.delete(0, END)
        self.genEnt.insert(END, lbselect[5])
        self.telEnt.delete(0, END)
        self.telEnt.insert(END, lbselect[6])
        self.addrEnt.delete(0, END)
        self.addrEnt.insert(END, lbselect[7])
        self.locEnt.delete(0, END)
        self.locEnt.insert(END, lbselect[8])
        self.acreEnt.delete(0, END)
        self.acreEnt.insert(END, lbselect[9])

    def deleteRecord(self):
        if (len(self.surEnt.get()) != 0 and len(self.fnameEnt.get()) != 0 and len(self.lnameEnt.get()) != 0 and len(
                self.idEnt.get()) != 0 and len(self.genEnt.get()) != 0 \
                and len(self.telEnt.get()) != 0 and len(self.addrEnt.get()) != 0 and len(
                    self.locEnt.get()) != 0 and len(self.acreEnt.get()) != 0):
            confirm = tkinter.messagebox.askyesno("Delete Record", "Confirm to Delete Record")
            if confirm > 0:
                Sqlite3_Backend.deleteRow(lbselect[0])
                self.clearFields()
                self.list_all()
                tkinter.messagebox.showinfo("Successful", "Record Deleted Successfully")
            else:
                return

    def searchDatabase(self):
        self.farmerlist.delete(0, END)
        for data in Sqlite3_Backend.searchRec(self.surEnt.get().capitalize(), self.fnameEnt.get().capitalize(),
                                              self.lnameEnt.get().capitalize(), \
                                              self.idEnt.get(), self.genEnt.get().capitalize(), self.telEnt.get(),
                                              self.addrEnt.get(), self.locEnt.get().capitalize(), self.acreEnt.get()):
            self.farmerlist.insert(END, data, str(" "))

    def list_all(self):
        self.farmerlist.delete(0, END)
        for data in Sqlite3_Backend.listData():
            self.farmerlist.insert(END, data, str(""))

    def exitWindow(self):
        iExit = tkinter.messagebox.askyesno("RFA Register/Update", "Confirm to exit")
        if iExit > 0:
            self.root2.destroy()
            return

    def widgets(self, root2):
        # ========================================== Frames ========================================================================================
        self.root2 = root2
        self.root2.geometry("1350x750+0+0")
        self.root2.title("Student Management System")
        self.root2.config(bg="light green")
        # _______ Main Frame ______
        self.MainFrame = Frame(self.root2, bg="light green")
        self.MainFrame.grid()

        # _______ Title Frame _______
        self.titleFrame = Frame(self.MainFrame, bd=2, padx=54, pady=8, bg="Ghost White", relief=RIDGE)
        self.titleFrame.pack(side=TOP)

        # _______ Button Frame _______
        self.buttonFrame = Frame(self.MainFrame, bd=1, width=1350, height=70, padx=18, pady=10, relief=RIDGE,
                                 bg="Ghost White")
        self.buttonFrame.pack(side=BOTTOM)

        # _______ Data Frame _________
        self.dataFrame = Frame(self.MainFrame, bd=0, width=1300, height=400, padx=87, pady=20, relief=RIDGE,
                               bg="light green")
        self.dataFrame.pack(side=BOTTOM)
        self.dataFrameLeft = LabelFrame(self.dataFrame, bd=1, width=1000, height=1000, padx=20, relief=RIDGE,
                                        bg="Ghost White",
                                        font=("arial", 20, 'bold'), text="Rice Farmers Association\nFarmer Details\n")
        self.dataFrameLeft.pack(side=LEFT)

        self.dataFrameRight = LabelFrame(self.dataFrame, bd=1, width=450, height=466, padx=31, pady=3, relief=RIDGE,
                                         bg="Ghost White", font=("arial", 20, "bold"), text="List View\n")
        self.dataFrameRight.pack(side=RIGHT)

        # ========================================== Labels and Entries================================================================================
        self.lblTitle = Label(self.titleFrame, font=("arial", 47, 'bold'), text="Register/Update Farmer Details",
                              bg="Ghost White")
        self.lblTitle.grid()

        self.fidlbl = Label(self.dataFrameLeft, font=("arial", 20, "bold"), text="Farmer's UID:", bg="Ghost White",
                            padx=2, pady=2)
        self.fidlbl.grid(row=0, column=0, sticky=W)
        uid = StringVar()
        self.fidEnt = Entry(self.dataFrameLeft, font=("arial", 18), textvariable=uid, width=39, bg='light grey')
        self.fidEnt.grid(row=0, column=1)

        self.surlbl = Label(self.dataFrameLeft, font=("arial", 20, "bold"), text="Surname:", bg="Ghost White", padx=2,
                            pady=2)
        self.surlbl.grid(row=1, column=0, sticky=W)
        surname = StringVar()
        self.surEnt = Entry(self.dataFrameLeft, font=("arial", 18), textvariable=surname, width=39)
        self.surEnt.grid(row=1, column=1)

        self.fnamelbl = Label(self.dataFrameLeft, font=("arial", 20, "bold"), text="First Name:", bg="Ghost White",
                              padx=2, pady=2)
        self.fnamelbl.grid(row=2, column=0, sticky=W)
        f_name = StringVar()
        self.fnameEnt = Entry(self.dataFrameLeft, font=("arial", 18), textvariable=f_name, width=39)
        self.fnameEnt.grid(row=2, column=1)

        self.lnamelbl = Label(self.dataFrameLeft, font=("arial", 20, "bold"), text="Last Name:", bg="Ghost White",
                              padx=2, pady=2)
        self.lnamelbl.grid(row=3, column=0, sticky=W)
        l_name = StringVar()
        self.lnameEnt = Entry(self.dataFrameLeft, font=("arial", 18), textvariable=l_name, width=39)
        self.lnameEnt.grid(row=3, column=1)

        self.idlbl = Label(self.dataFrameLeft, font=("arial", 20, "bold"), text="ID Number:", bg="Ghost White", padx=2,
                           pady=2)
        self.idlbl.grid(row=4, column=0, sticky=W)
        id_number = StringVar()
        self.idEnt = Entry(self.dataFrameLeft, font=("arial", 18), textvariable=id_number, width=39)
        self.idEnt.grid(row=4, column=1)

        self.genlbl = Label(self.dataFrameLeft, font=("arial", 20, "bold"), text="Gender:", bg="Ghost White", padx=2,
                            pady=2)
        self.genlbl.grid(row=5, column=0, sticky=W)
        gender = StringVar()
        self.genEnt = Entry(self.dataFrameLeft, font=("arial", 18), textvariable=gender, width=39)
        self.genEnt.grid(row=5, column=1)

        self.tellbl = Label(self.dataFrameLeft, font=("arial", 20, "bold"), text="Tel:", bg="Ghost White", padx=2,
                            pady=2)
        self.tellbl.grid(row=6, column=0, sticky=W)
        tel = StringVar()
        self.telEnt = Entry(self.dataFrameLeft, font=("arial", 18), textvariable=tel, width=39)
        self.telEnt.grid(row=6, column=1)

        self.addrlbl = Label(self.dataFrameLeft, font=("arial", 20, "bold"), text="Address:", bg="Ghost White", padx=2,
                             pady=2)
        self.addrlbl.grid(row=7, column=0, sticky=W)
        address = StringVar()
        self.addrEnt = Entry(self.dataFrameLeft, font=("arial", 18), textvariable=address, width=39)
        self.addrEnt.grid(row=7, column=1)

        self.loclbl = Label(self.dataFrameLeft, font=("arial", 20, "bold"), text="Location:", bg="Ghost White", padx=2,
                            pady=2)
        self.loclbl.grid(row=8, column=0, sticky=W)
        location = StringVar()
        self.locEnt = Entry(self.dataFrameLeft, font=("arial", 18), textvariable=location, width=39)
        self.locEnt.grid(row=8, column=1)

        self.acrelbl = Label(self.dataFrameLeft, font=("arial", 20, "bold"), text="No of Acres:", bg="Ghost White",
                             padx=2, pady=2)
        self.acrelbl.grid(row=9, column=0, sticky=W)
        no_of_acres = StringVar()
        self.acreEnt = Entry(self.dataFrameLeft, font=("arial", 18), textvariable=no_of_acres, width=39)
        self.acreEnt.grid(row=9, column=1)

        # ========================================== ListBox and Scrollbar ======================================================================
        self.scrollbar = Scrollbar(self.dataFrameRight, orient=VERTICAL)
        self.scrollbar.grid(row=0, column=1, sticky=NS)

        self.scrollbarx = Scrollbar(self.dataFrameRight, orient=HORIZONTAL)
        self.scrollbarx.grid(row=1, column=0, sticky=EW)

        self.farmerlist = Listbox(self.dataFrameRight, width=41, height=20, font=('arial', 12, 'bold'),
                                  yscrollcommand=self.scrollbar.set,
                                  xscrollcommand=self.scrollbarx.set)
        self.farmerlist.bind('<<ListboxSelect>>', self.farmerRec)
        self.farmerlist.grid(row=0, column=0, padx=8, pady=3)
        self.scrollbar.config(command=self.farmerlist.yview)
        self.scrollbarx.config(command=self.farmerlist.xview)

        # ========================================== Buttons ===================================================================================
        self.btnAddNew = Button(self.buttonFrame, text="Add New", font=('arial', 20, 'bold'), height=1, width=10, bd=4,
                                command=self.addData)
        self.btnAddNew.grid(row=0, column=0)
        self.btnUpdate = Button(self.buttonFrame, text="Update", font=('arial', 20, 'bold'), height=1, width=10, bd=4,
                                command=self.updateRecord)
        self.btnUpdate.grid(row=0, column=1)
        self.btnClear = Button(self.buttonFrame, text="Clear", font=('arial', 20, 'bold'), height=1, width=10, bd=4,
                               command=self.clearFields)
        self.btnClear.grid(row=0, column=2)
        self.btnDelete = Button(self.buttonFrame, text="Delete", font=('arial', 20, 'bold'), height=1, width=10, bd=4,
                                command=self.deleteRecord)
        self.btnDelete.grid(row=0, column=3)
        self.btnSearch = Button(self.buttonFrame, text="Search", font=('arial', 20, 'bold'), height=1, width=10, bd=4,
                                command=self.searchDatabase)
        self.btnSearch.grid(row=0, column=4)
        self.btnListall = Button(self.buttonFrame, text="List All", font=('arial', 20, 'bold'), height=1, width=10,
                                 bd=4, command=self.list_all)
        self.btnListall.grid(row=0, column=5)
        self.btnExit = Button(self.buttonFrame, text="Exit", font=('arial', 20, 'bold'), height=1, width=10, bd=4,
                              command=self.exitWindow)
        self.btnExit.grid(row=0, column=6)


root = Tk()
runx = Register_Update()
runx.widgets(root)
root.mainloop()