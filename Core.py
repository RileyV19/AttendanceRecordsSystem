#Imports
import sqlite3

DatabaseConnection = sqlite3.connect("C:\sqlite\Database.db")
cursor = DatabaseConnection.cursor()



cursor.execute('''CREATE TABLE stocks
               (date text, trans text, symbol text, qty real, price real)''')



DatabaseConnection.commit()
DatabaseConnection.close()

print("done")
