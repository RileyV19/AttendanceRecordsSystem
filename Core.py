#Imports
import sqlite3

#+------------------------------------------------
#|  Main App class
#|    - All methods that require a connection to 
#|      the sqlite3 database are contained here
#+------------------------------------------------
class App(object):
    #--- Define and initialise variables ---
    def __init__(self):
        #Variables
        self.DatabaseConnection = None
        self.cursor = None
        self.Options = "CreateTable(1), DeleteTable(2), ShowTables(3), ShowTableContents(4), InsertIntoTable(5), Commit(6), Close(7)"
        self.newline_indent = '\n   '
    
    #+---------------------------------------
    #|  SQL functions - Create, delete, modify, show tables and entries
    #+---------------------------------------
    
    #Create a new table - 
    def CreateTable(self, Name: str, Contents: str):
        self.cursor.execute('''CREATE TABLE {} ({});'''.format(Name, Contents))


    def DeleteTable(self, Name: str):
        self.cursor.execute('''DROP TABLE {};'''.format(Name))


    def ShowTables(self):
        newline_indent = '\n   '
        result = self.cursor.execute('''SELECT name FROM sqlite_master WHERE type='table';''').fetchall()
        table_names = sorted(list(zip(*result))[0])
        print ("\ntables with columns:" + newline_indent)
        for table_name in table_names:
            result = self.cursor.execute("PRAGMA table_info('%s')" % table_name).fetchall()
            column_names = list(zip(*result))[1]
            print("\t" + (table_name) + "\t" + str(column_names))


    def ShowTableContents(self, Name: str):
        newline_indent = '\n   '
        result = self.cursor.execute('''SELECT * FROM {};'''.format(Name)).fetchall()
        print(result)


    def InsertIntoTable(self, Name: str, Contents: str):
        self.cursor.execute('''INSERT INTO {} VALUES ({});'''.format(Name, Contents))


    def Commit(self):
        self.DatabaseConnection.commit()

    #+---------------------------------------
    #|  SQL connection functions - Establish and close the connection, prepare the cursor
    #+---------------------------------------
    def Connect(self):
        self.DatabaseConnection = sqlite3.connect("C:\sqlite\Database\Database.db")
        print("Successfully connected to database")
        
    def Close(self):
        self.DatabaseConnection.close()

    def Cursor(self):
        self.cursor = self.DatabaseConnection.cursor()

    
    #+---------------------------------------
    #|  Command-line User Interface - create and manipulate data as user
    #+---------------------------------------
    def Selections(self):
        print("\nPlease select one of the following options: {}".format(self.Options))
        Selection = str(input("Enter option 1-7: "))
        if Selection == "1":
                print("you chose 1")
                Name = input("Enter new table Name: ")
                Contents = input("Enter new table contents: ")                   
                self.CreateTable(Name, Contents)
                                       
        elif Selection == "2":
                print("you chose 2")
                Name = input("Enter table name to delete: ")                   
                self.DeleteTable(Name)
                
        elif Selection == "3":
                print("you chose 3")
                self.ShowTables()

        elif Selection == "4":
                print("you chose 4")
                Name = input("Enter table name to display its contents: ")  
                self.ShowTableContents(Name)

        elif Selection == "5":
                print("you chose 5")
                Name = input("Enter table name to insert data into: ")
                Contents = input("Enter new table entries: ") 
                self.InsertIntoTable(Name, Contents)
                
        elif Selection == "6":
                print("you chose 6")
                self.Commit()
                print("Commit success")
                
        elif Selection == "7":
                print("you chose 7")
                self.Close()
                print("Connection closed")
                
        else:
            print("invalid selection")
        
        self.Selections()

    def CommandInterface(self):
        self.Commit()
        self.Selections()
        
####################################################################################################
def main():
    AppInstance = App()
    AppInstance.Connect()
    AppInstance.Cursor()
    AppInstance.CommandInterface()

if __name__ == "__main__":
    main()
