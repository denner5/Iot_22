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
    try:                                                    
        db = sqlite3.connect('Data_1.db')     
        cursor = db.cursor()                  

        sql_select_query = """select * from butik_lager where Stregkode = ?""" 
        cursor.execute(sql_select_query, (dbdata.Stregkode,))  
        records = cursor.fetchall()                        
        print("Printing ID ", dbdata.Stregkode)
        print(records)
        for row in records:                                       
            if(dbdata.Stregkode == row[0]):                  
                print("Vi har produktet")
                dbdata.Navn = row[1]                 
                dbdata.Pris = row[2]                    
                dbdata.Stockoption = True
            else:   
                print("Vi har ikke produktet")
                db_data.Stockoption = False
        cursor.close()                                      
    except sqlite3.Error as error:                          
        print("Failed to read data from sqlite table", error)

    finally:                                                
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
                            (?,?,?)"""                                                                                                                         
        data = (str(dbdata.Stregkode), dbdata.Navn, dbdata.Pris/dbdata.nedsættelsesværdi) 
        print("row værdi: ", data)
        cursor.execute(sqlite_insert_query, data)                                                                                                                     
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
