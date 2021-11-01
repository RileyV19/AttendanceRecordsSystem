#Imports
import sqlite3


#+------------------------------------------------
#|  Main App class
#|    - All methods that require a connection to 
#|      the sqlite3 database are contained here
#+------------------------------------------------
class App(object):
    def __init__(self):
        #Variables
        self.DatabaseConnection = None
        self.cursor = None
        self.Options = "[1] Add Student\n[2] Record Attendance\n[3] Record Parts\n[4] Topics or Tests completed\n[4] Search Student\n[5] Advanced Options"
        self.ExtraOptions = "[1] CreateTable\n[2] DeleteTable\n[3] ShowTables\n[4] ShowTableContents\n[5] InsertIntoTable\n[6] DeleteAllEntiresInTable\n[7] Commit\n[8] Close\n[9] Basic Options (9)"
        self.newline_indent = '\n   '

    #+---------------------------------------
    #|  SQL functions - Create, delete, modify, show tables and entries
    #+---------------------------------------
    
    # Create table
    def CreateTable(self, Name: str, Contents: str):
        self.cursor.execute('''CREATE TABLE {} ({});'''.format(Name, Contents))

    # Delete Table
    def DeleteTable(self, Name: str):
        self.cursor.execute('''DROP TABLE {};'''.format(Name))

    # Show tables
    def ShowTables(self):
        newline_indent = '\n   '
        result = self.cursor.execute('''SELECT name FROM sqlite_master WHERE type='table';''').fetchall()
        table_names = sorted(list(zip(*result))[0])
        print ("\ntables with columns:" + newline_indent)
        for table_name in table_names:
            result = self.cursor.execute("PRAGMA table_info('%s')" % table_name).fetchall()
            column_names = list(zip(*result))[1]
            print("\t" + (table_name) + "\t" + str(column_names))

    #Show table contents
    def ShowTableContents(self, Name: str):
        newline_indent = '\n   '
        result = self.cursor.execute('''SELECT * FROM {};'''.format(Name)).fetchall()
        print()
        for Entry in result:
            print("\t" + str(Entry))

    # Add data to table
    def InsertIntoTable(self, Name: str, Contents: str):
        self.cursor.execute('''INSERT INTO {} VALUES({});'''.format(Name, Contents))

    # Clear table
    def DeleteAllEntiresInTable(self, Name: str):
        self.cursor.execute('''DELETE FROM {};'''.format(Name))


        
    #+---------------------------------------
    #|  SQL connection functions - Establish and close the connection, prepare the cursor
    #+---------------------------------------
    def Connect(self):
        self.DatabaseConnection = sqlite3.connect("C:\sqlite\Database\Database.db")
        print("Welcome to the APPNAMEGOESHERE App!")

    def Commit(self):
        self.DatabaseConnection.commit()

    def Close(self):
        self.DatabaseConnection.close()

    def Cursor(self):
        self.cursor = self.DatabaseConnection.cursor()

        
    #+---------------------------------------
    #|  Command-line Basic User Interface - create and manipulate data as user
    #+---------------------------------------
    def BasicOptions(self):
        print("\nPlease select one of the following basic options: {}".format(self.Options))
        Selection = str(input("Enter option 1-5: "))
        
        # Add student
        if Selection == "1":
                print("you chose 1")
                FirstName = input("Enter new Students first name: ")
                LastName = input("Enter new Students last name: ")
                DOB = input("Enter new Students Date-of-Birth (in YYYY-MM-DD format): ")
                self.cursor.execute("INSERT INTO STUDENT VALUES ('"'{}'"','"'{}'"','"'{}'"');".format(FirstName, LastName, DOB))
        
        # Record Attendance
        elif Selection == "2":
                print("you chose 2")
                StudentID = input("Enter Students ID to record attendence for: ")
                ClassType = input("Enter class type attended ")
                AttendenceDate = input("Enter date of attendence(in YYYY-MM-DD format): ")
                self.cursor.execute("INSERT INTO ATTENDENCE VALUES ('"'{}'"','"'{}'"','"'{}'"');".format(StudentID, ClassType, AttendenceDate))
        
        # Record Student Achievement
        elif Selection == "3":
                print("you chose 3")
                StudentID = input("Enter Students ID to record achievement for: ")
                AchievementType = input("Enter achievement type (part, topic, test: ")
                AchievementName = input("Enter achievement name: ")
                AchievementDate = input("Enter date of achievement(in YYYY-MM-DD format): ")
                AchievemntStatus = input("Enter Achievement Status (PASS/FAIL): ")
                self.cursor.execute("INSERT INTO Achievement VALUES ('"'{}'"','"'{}'"','"'{}'"','"'{}'"','"'{}'"');".format(StudentID, AchievementType, AchievementName, AchievementDate, AchievemntStatus))

        # Search Achievements
        elif Selection == "4":
                print("you chose 4")
                Name = input("Enter students name to retrieve personal details and achievements: ")  
                self.cursor.execute("INSERT A SEARCH QUERY HERE")
        
        # Enter Advanced menu - password protected
        elif Selection == "5":
                print("you chose 5")
                self.AdvancedOptions()
        
        # Error - invalid option
        else:
            print("Invalid selection!")

        self.Commit()
        self.BasicOptions()

    #+---------------------------------------
    #|  Command-line Advanced User Interface - Create, delete and modify tables from the back end of the program
    #+---------------------------------------
    def AdvancedOptions(self):
        print("\nPlease select one of the following advanced options: {}".format(self.ExtraOptions))
        Selection = str(input("Enter option 1-8: "))
        
        # Create Table
        if Selection == "1":
                print("you chose 1")
                Name = input("Enter new table Name: ")
                Contents = input("Enter new table contents: ")                   
                self.CreateTable(Name, Contents)
        
        # Delete table
        elif Selection == "2":
                print("you chose 2")
                Name = input("Enter table name to delete: ")                   
                self.DeleteTable(Name)
        
        # Show tables
        elif Selection == "3":
                print("you chose 3")
                self.ShowTables()
        
        # Show table contents
        elif Selection == "4":
                print("you chose 4")
                Name = input("Enter table name to display its contents: ")  
                self.ShowTableContents(Name)
        
        # Add data to table
        elif Selection == "5":
                print("you chose 5")
                Name = input("Enter table name to insert data into: ")
                Contents = input("Enter new table entries: ") 
                self.InsertIntoTable(Name, Contents)

        # Clear table
        elif Selection == "6":
                print("you chose 6")
                Name = input("Enter table name to delete all entries from: ")
                self.DeleteAllEntiresInTable(Name)
        
        # Save changes
        elif Selection == "7":
                print("you chose 7")
                self.Commit()
                print("Commit success")
        
        # Exit program
        elif Selection == "8":
                print("you chose 8")
                self.Close()
                print("Connection closed")
        
        # Return to Basic Options menu
        elif Selection == "9":
                print("you chose 9")
                self.BasicOptions()
        
        # Error - invalid option
        else:
            print("Invalid selection!")

        self.Commit()
        self.AdvancedOptions()


    def CommandInterface(self):
        self.Commit()
        self.BasicOptions()
        
####################################################################################################
def main():
    AppInstance = App()
    AppInstance.Connect()
    AppInstance.Cursor()
    AppInstance.CommandInterface()


if __name__ == "__main__":
    main()
