import time
import sqlite3

db=sqlite3.connect("/home/pi/Desktop/iot2/Data_1.db")
cursor = db.cursor()

class dbdata:
    Stregkode = ""
    Navn =""
    Pris = 0
    Stockoption = False
    nedsættelsesværdi = 2
    
def control():
    data_check_product()
    if dbdata.Stockoption == True:
        inserintoDB()
    nulstil_variabler()
    


def data_check_product():
    try:                                                    #Vi har nedenstående inde i en try så programmer ikke lukker hvis der sker en fejl
        db = sqlite3.connect('Data_1.db')     #Opretter forbindelse til batch.db
        cursor = db.cursor()                  #cursor er en instance hvor man kan tilsutte sqlite metoder og køre dem

        sql_select_query = """select * from butik_lager where Stregkode = ?""" #Den tager alt fra product table som matcher variablen med EAN13 kolonnen
        cursor.execute(sql_select_query, (dbdata.Stregkode,)) #Spørgsmålstegnene ovenover betyder at vi har variabler. Her laver vi en tuple med de variabler vi gerne vil bruge
        records = cursor.fetchall()                         #Her hiver den så alt ud af databasen og sætter records variablen lig med det
        print("Printing ID ", dbdata.Stregkode)
        print(records)
        for row in records:                                 #For loopet her køre lige så mange gange den har fået rækker ud af tabellen       
            if(dbdata.Stregkode == row[0]):                  #Kigger på om der er nogle rækker med deres kolonne 1 matcher EAN13 i batchdata
                print("Vi har produktet")
                dbdata.Navn = row[1]                 #Her sætter den Category variablen til kolonne 3 som er kategorien varen tilhøre
                dbdata.Pris = row[2]                    #Her sætter den price variablen til kolonne 4 som er prisen på varen
                dbdata.Stockoption = True
            else:   
                print("Vi har ikke produktet")
                db_data.Stockoption = False
        cursor.close()                                      #Derefter lukker vi cursor metoden. Hvilket for os er forbindelsen til databasen
    except sqlite3.Error as error:                          #Hvis der sker en fejl udprinter vi fejlbeskeden
        print("Failed to read data from sqlite table", error)

    finally:                                                #Til sidst kigger den på om den har en forbindelse til en database. Hvis den har det lukker den forbindelsen
        if db:
            db.commit()
            db.close()


def inserintoDB():
    try:
        sqliteConnection = sqlite3.connect('Data_1.db')
        cursor = sqliteConnection.cursor()
        sqlite_insert_query = """INSERT INTO tilbud
                            (Stregkode, Navn, Pris) 
                            VALUES 
                            (?,?,?)"""                                                                                                                        #Her 
        data = (str(dbdata.Stregkode), dbdata.Navn, dbdata.Pris/dbdata.nedsættelsesværdi) 
        print("row værdi: ", data)
        cursor.execute(sqlite_insert_query, data)                                                                                                                     #Nu køre vi querien med vores tuple variabler
        sqliteConnection.commit()
        print("Record inserted successfully into tilbud table", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into tilbuds table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
def nulstil_variabler():
    dbdata.Stregkode = ""
    dbdata.Navn = ""
    dbdata.Pris = 0
    dbdata.Stockoption = False
    
def delete():
    print("kør delete")
    try:
        sqliteConnection = sqlite3.connect('Data_1.db')
        cursor = sqliteConnection.cursor()

        sql_update_query = """DELETE FROM tilbud WHERE Stregkode = ? LIMIT 1"""
        data = (str(dbdata.Stregkode)) 
        cursor.execute(sql_update_query, (data,))
        sqliteConnection.commit()
        print("Record deleted successfully")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to delete reocord from a sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")
#delete()
            
# def inserintoDaB():
#     try:
#         sqliteConnection = sqlite3.connect('Data_1.db')
#         cursor = sqliteConnection.cursor()
#         sqlite_insert_query = """INSERT INTO butik_lager
#                             (Stregkode, Navn, Pris) 
#                             VALUES 
#                             (?,?,?)"""                                                                                                                        #Her 
#         data = ("0799439041905", "kage", 50) 
#         print("row værdi: ", data)
#         cursor.execute(sqlite_insert_query, data)                                                                                                                     #Nu køre vi querien med vores tuple variabler
#         sqliteConnection.commit()
#         print("Record inserted successfully into tilbud table", cursor.rowcount)
#         cursor.close()
# 
#     except sqlite3.Error as error:
#         print("Failed to insert data into tilbuds table", error)
#     finally:
#         if sqliteConnection:
#             sqliteConnection.close()
# inserintoDaB()
