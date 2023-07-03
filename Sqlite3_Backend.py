import sqlite3


def farmerTable():
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS FarmerInfo(
                Surname TEXT,
                Firstname TEXT,
                Lastname TEXT,
                IDNo TEXT,
                Gender TEXT,
                Tel TEXT,
                Address TEXT,
                Location TEXT,
                Acres TEXT
            )""")
    conn.commit()
    conn.close()


def addRecord(surname, f_name, l_name, id_num, gender, tel, address, location, no_of_acres):
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("INSERT INTO FarmerInfo VALUES (?,?,?,?,?,?,?,?,?)",
              (surname, f_name, l_name, id_num, gender, tel, address, location, no_of_acres))
    conn.commit()
    conn.close()


def updateDB(surname='', f_name='', l_name='', id_num='', gender='', tel='', address='', location='', no_of_acres='',
             rowid=''):
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute(
        "UPDATE FarmerInfo SET Surname=?,Firstname=?, Lastname=?, IDNo=?, Gender=?, Tel=?, Address=?, Location=?, Acres=? WHERE rowid=?",
        (surname, f_name, l_name, id_num, gender, tel, address, location, no_of_acres, rowid))
    conn.commit()
    conn.close()


def deleteRow(id):
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("DELETE FROM FarmerInfo WHERE rowid = ?", (id,))
    conn.commit()
    conn.close()


def searchRec(surname='', f_name='', l_name='', id_num='', gender='', tel='', address='', location='', no_of_acres=''):
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("SELECT rowid,* FROM FarmerInfo WHERE Surname=? OR Firstname=? OR Lastname=? OR IDNo=? OR Gender=? OR Tel=? OR \
     Address=? OR Location=? OR Acres=?",
              (surname, f_name, l_name, id_num, gender, tel, address, location, no_of_acres))
    data = c.fetchall()
    conn.close()
    return data


def listData():
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("SELECT rowid,* FROM FarmerInfo")
    data = c.fetchall()
    conn.close()
    return data


def insertid(id_num):
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("SELECT rowid FROM FarmerInfo WHERE IDNo = ?", (id_num,))
    data = c.fetchall()
    conn.close()
    return data


def getsurid(id):
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("SELECT Surname, IDNo FROM FarmerInfo WHERE rowid = ?", (id,))
    data = c.fetchall()
    conn.close()
    return data


def serviceTable():
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS Services(
                Reference TEXT,
                FUID TEXT,
                Surname TEXT,
                Date TEXT,
                ServiceCost TEXT,
                FerCost TEXT,
                FarmInCost TEXT,
                Tax TEXT,
                Total TEXT
            )""")
    conn.commit()
    conn.close()


def viewServiceRefStatus(fuid):  # ____Used in Farmer Status Module____
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("SELECT Reference FROM Services WHERE FUID = ?", (fuid,))
    data = c.fetchall()
    conn.close()
    return data


def viewServiceStatus(fuid):  # ____Used in Farmer Status Module____
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("SELECT SUM(ServiceCost) FROM Services WHERE FUID = ?", (fuid,))
    data = c.fetchall()
    conn.close()
    return data


def viewFertilizerStatus(fuid):  # ____Used in Farmer Status Module____
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("SELECT SUM(FerCost) FROM Services WHERE FUID = ?", (fuid,))
    data = c.fetchall()
    conn.close()
    return data


def viewFarmInStatus(fuid):  # ____Used in Farmer Status Module____
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("SELECT SUM(FarmInCost) FROM Services WHERE FUID = ?", (fuid,))
    data = c.fetchall()
    conn.close()
    return data


def viewTaxStatus(fuid):  # ____Used in Farmer Status Module____
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("SELECT SUM(Tax) FROM Services WHERE FUID = ?", (fuid,))
    data = c.fetchall()
    conn.close()
    return data


def viewTotalStatus(fuid):  # ____Used in Farmer Status Module____
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("SELECT SUM(Total) FROM Services WHERE FUID = ?", (fuid,))
    data = c.fetchall()
    conn.close()
    return data


def addService(reference, fuid, surname, date, serviceCost, ferCost, farmInCost, tax, total):
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("INSERT INTO Services VALUES (?,?,?,?,?,?,?,?,?)",
              (reference, fuid, surname, date, serviceCost, ferCost, farmInCost, tax, total))
    conn.commit()
    conn.close()


def getRef():
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("SELECT Reference FROM Services")
    data = c.fetchall
    conn.close()
    return data


def cashServiceTable():
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS CashServices(
                Reference TEXT,
                Date TEXT,
                ServiceCost TEXT,
                FerCost TEXT,
                FarmInCost TEXT,
                Tax TEXT,
                Total TEXT
            )""")
    conn.commit()
    conn.close()


def addCashService(reference, date, serviceCost, ferCost, farmInCost, tax, total):
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("INSERT INTO CashServices VALUES (?,?,?,?,?,?,?)",
              (reference, date, serviceCost, ferCost, farmInCost, tax, total))
    conn.commit()
    conn.close()


def getCashRef():
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("SELECT Reference FROM CashServices")
    data = c.fetchall
    conn.close()
    return data


def listServiceData():
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM Services")
    data = c.fetchall()
    conn.close()
    return data


def listCashData():
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("SELECT rowid,* FROM CashServices")
    data = c.fetchall()
    conn.close()
    return data


def dateSearchService(date):
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("SELECT * FROM Services WHERE Date = ?", (date,))
    data = c.fetchall()
    conn.close()
    return data


def fuidSearchService(fuid):
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("SELECT * FROM Services WHERE FUID = ?", (fuid,))
    data = c.fetchall()
    conn.close()
    return data


def refSearchService(ref):
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("SELECT * FROM Services WHERE Reference = ?", (ref,))
    data = c.fetchall()
    conn.close()
    return data


def searchCashService(ref):
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("SELECT * FROM CashServices WHERE Reference = ?", (ref,))
    data = c.fetchall()
    conn.close()
    return data


def dateCashService(date):
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("SELECT * FROM CashServices WHERE Date = ?", (date,))
    data = c.fetchall()
    conn.close()
    return data


def ServicePricesTable():
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS ServicePrices(
                Harvest TEXT,
                Rotav TEXT,
                Transport TEXT,
                Seed TEXT
            )""")
    conn.commit()
    conn.close()


def selectHarvest():
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("SELECT Harvest FROM ServicePrices")
    data = c.fetchall()
    conn.close()
    return data


def selectRotav():
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("SELECT Rotav FROM ServicePrices")
    data = c.fetchall()
    conn.close()
    return data


def selectTransport():
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("SELECT Transport FROM ServicePrices")
    data = c.fetchall()
    conn.close()
    return data


def selectSeed():
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("SELECT Seed FROM ServicePrices")
    data = c.fetchall()
    conn.close()
    return data


def FarmInPricesTable():
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS FarmInPrices(
                Escort TEXT,
                Dicoper TEXT,
                Regent TEXT,
                Opal TEXT
            )""")
    conn.commit()
    conn.close()


def selectEscort():
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("SELECT Escort FROM FarmInPrices")
    data = c.fetchall()
    conn.close()
    return data


def selectDicoper():
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("SELECT Dicoper FROM FarmInPrices")
    data = c.fetchall()
    conn.close()
    return data


def selectRegent():
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("SELECT Regent FROM FarmInPrices")
    data = c.fetchall()
    conn.close()
    return data


def selectOpal():
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("SELECT Opal FROM FarmInPrices")
    data = c.fetchall()
    conn.close()
    return data


def FertPricesTable():
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS FertPrices(
                NPK TEXT,
                ZS TEXT,
                CAN TEXT,
                TSP TEXT,
                SSP TEXT,
                SA TEXT
            )""")
    conn.commit()
    conn.close()


def selectNPK():
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("SELECT NPK FROM FertPrices")
    data = c.fetchall()
    conn.close()
    return data


def selectZS():
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("SELECT ZS FROM FertPrices")
    data = c.fetchall()
    conn.close()
    return data


def selectCAN():
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("SELECT CAN FROM FertPrices")
    data = c.fetchall()
    conn.close()
    return data


def selectTSP():
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("SELECT TSP FROM FertPrices")
    data = c.fetchall()
    conn.close()
    return data


def selectSSP():
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("SELECT SSP FROM FertPrices")
    data = c.fetchall()
    conn.close()
    return data


def selectSA():
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("SELECT SA FROM FertPrices")
    data = c.fetchall()
    conn.close()
    return data


def OtherPricesTable():
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS OtherPrices(
                Tax TEXT,
                DeliveryPrice TEXT
            )""")
    conn.commit()
    conn.close()


def selectTax():
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("SELECT Tax FROM OtherPrices")
    data = c.fetchall()
    conn.close()
    return data


def selectPrice():
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("SELECT DeliveryPrice FROM OtherPrices")
    data = c.fetchall()
    conn.close()
    return data


def FertPricesTable():
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS FertPrices(
                NPK TEXT,
                ZS TEXT,
                CAN TEXT,
                TSP TEXT,
                SSP TEXT,
                SA TEXT
            )""")
    conn.commit()
    conn.close()


def selectSurname(fuid):
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("SELECT Surname FROM FarmerInfo WHERE rowid = ?", (fuid,))
    data = c.fetchall()
    conn.close()
    return data


def DeliveryTable():
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS Delivery(
                DeliveryRef TEXT,
                DeliveryDate TEXT,
                FUID TEXT,
                Surname TEXT,
                Weight TEXT,
                Total TEXT
            )""")
    conn.commit()
    conn.close()


def viewDeliveryRefStatus(fuid):  # ____Used in Farmer Status Module____
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("SELECT DeliveryRef FROM Delivery WHERE FUID = ?", (fuid,))
    data = c.fetchall()
    conn.close()
    return data


def viewWeightStatus(fuid):  # ____Used in Farmer Status Module____
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("SELECT SUM(Weight) FROM Delivery WHERE FUID = ?", (fuid,))
    data = c.fetchall()
    conn.close()
    return data


def viewTotalCashStatus(fuid):  # ____Used in Farmer Status Module____
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("SELECT SUM(Total) FROM Delivery WHERE FUID = ?", (fuid,))
    data = c.fetchall()
    conn.close()
    return data


def addDelivery(ref, date, fuid, surname, weight, cash):
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("INSERT INTO DELIVERY VALUES(?,?,?,?,?,?)", (ref, date, fuid, surname, weight, cash))
    conn.commit()
    conn.close()


def refSearchDelivery(ref):
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("SELECT * FROM Delivery WHERE DeliveryRef = ?", (ref,))
    data = c.fetchall()
    conn.close()
    return data


def dateSearchDelivery(date):
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("SELECT * FROM Delivery WHERE DeliveryDate = ?", (date,))
    data = c.fetchall()
    conn.close()
    return data


def fuidSearchDelivery(fuid):
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("SELECT * FROM Delivery WHERE FUID = ?", (fuid,))
    data = c.fetchall()
    conn.close()
    return data


def rdfSearchDelivery(ref, date, fuid):
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("SELECT * FROM Delivery WHERE DeliveryRef = ? AND DeliveryDate = ? AND FUID = ?", (ref, date, fuid))
    data = c.fetchall()
    conn.close()
    return data


def displayDeliveryData():
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM Delivery")
    data = c.fetchall()
    conn.close()
    return data


def paymentTable():
    conn = sqlite3.connect('Farmer.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS PayFarmer(
        PaymentRef TEXT,
        PaymentDate TEXT,
        FUID TEXT,
        Surname TEXT,
        Amount TEXT
    )""")


def addPaymentRec(ref, date, fuid, surname, amount):
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("INSERT  INTO PayFarmer VALUES(?,?,?,?,?)", (ref, date, fuid, surname, amount))
    conn.commit()
    conn.close()


# ______ Move The Service Record To Archives _______
def serviceArchiveTable():
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS ServicesArchives(
                Reference TEXT,
                FUID TEXT,
                Surname TEXT,
                Date TEXT,
                ServiceCost TEXT,
                FerCost TEXT,
                FarmInCost TEXT,
                Tax TEXT,
                Total TEXT
            )""")
    conn.commit()
    conn.close()


def DeliveryArchiveTable():
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS DeliveryArchives(
                DeliveryRef TEXT,
                DeliveryDate TEXT,
                FUID TEXT,
                Surname TEXT,
                Weight TEXT,
                Total TEXT
            )""")
    conn.commit()
    conn.close()


def copyService(fuid):
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("""INSERT INTO ServicesArchives
        SELECT * FROM Services WHERE FUID = ?
        """, (fuid,))


def copyDelivery(fuid):
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("""INSERT INTO DeliveryArchives
        SELECT * FROM Delivery WHERE FUID = ?
        """, (fuid,))


# _____ Delete Copied Data From Active Tables ______
def deleteServiceCopy(fuid):
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("DELETE FROM Services WHERE FUID = ?", (fuid,))
    conn.commit()
    conn.close()


def deleteDeliveryCopy(fuid):
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("DELETE FROM Delivery WHERE FUID = ?", (fuid,))
    conn.commit()
    conn.close()


def displayPayment():
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("SELECT * FROM PayFarmer")
    data = c.fetchall()
    conn.close()
    return data


def searchPayment(fuid, ref, date):
    conn = sqlite3.connect("Farmer.db")
    c = conn.cursor()
    c.execute("SELECT * FROM PayFarmer WHERE FUID=? OR PaymentRef=? OR PaymentDate=?", (fuid, ref, date))
    data = c.fetchall()
    conn.close()
    return data