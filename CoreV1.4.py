#Imports
import sqlite3


################################################################


class App(object):
    def __init__(self):
        #Variables
        self.DatabaseConnection = None
        self.cursor = None
        self.Options = "Add Student (1), Record Attendance (2), Record Parts, Topics or Tests completed (3), Search Student (4), Advanced Options (5)"
        self.ExtraOptions = "CreateTable(1), DeleteTable(2), ShowTables(3), ShowTableContents(4), InsertIntoTable(5), DeleteAllEntiresInTable(6), Commit(7), Close(8), Basic Options (9)"
        self.newline_indent = '\n   '


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
        print()
        for Entry in result:
            print("\t" + str(Entry))


    def InsertIntoTable(self, Name: str, Columns: str, Contents: str):
        self.cursor.execute('''INSERT INTO {}({}) VALUES ({});'''.format(Name, Columns, Contents))


    def DeleteAllEntiresInTable(self, Name: str):
        self.cursor.execute('''DELETE FROM {};'''.format(Name))


    def Commit(self):
        self.DatabaseConnection.commit()


    def Close(self):
        self.DatabaseConnection.close()


    def Connect(self):
        self.DatabaseConnection = sqlite3.connect("C:\sqlite\Database\Database.db")
        print("Welcome to the Attendece Record System Executable app!")


    def Cursor(self):
        self.cursor = self.DatabaseConnection.cursor()



#######################################################################


    def BasicOptions(self):
        print("\nPlease select one of the following basic options: {}".format(self.Options))
        Selection = str(input("Enter option 1-5: "))
        if Selection == "1":
                print("you chose 1")
                FirstName = input("Enter new Students first name: ")
                LastName = input("Enter new Students last name: ")
                DOB = input("Enter new Students Date-of-Birth (in YYYY-MM-DD format): ")
                self.cursor.execute("INSERT INTO STUDENT VALUES ('"'{}'"','"'{}'"','"'{}'"');".format(FirstName, LastName, DOB))
                                       
        elif Selection == "2":
                print("you chose 2")
                StudentID = input("Enter Students ID to record attendence for: ")
                ClassType = input("Enter class type attended ")
                AttendenceDate = input("Enter date of attendence(in YYYY-MM-DD format): ")
                AttendenceTime = input("Enter date of attendence(in YYYY-MM-DD format): ")
                self.cursor.execute("INSERT INTO ATTENDENCE VALUES ('"'{}'"','"'{}'"','"'{}'"');".format(StudentID, ClassType, AttendenceDate))
                
        elif Selection == "3":
                print("you chose 3")
                StudentID = input("Enter Students ID to record achievement for: ")
                AchievementType = input("Enter achievement type (part, topic, test: ")
                AchievementName = input("Enter achievement name: ")
                AchievementDate = input("Enter date of achievement(in YYYY-MM-DD format): ")
                AchievemntStatus = input("Achievement passed? (TRUE/FALSE): ")
                self.cursor.execute("INSERT INTO Achievement VALUES ('"'{}'"','"'{}'"','"'{}'"','"'{}'"','"'{}'"');".format(StudentID, AchievementType, AchievementName, AchievementDate, AchievemntStatus))

        elif Selection == "4":
                print("you chose 4")
                Name = input("Enter students name to retrieve personal details and achievements: ")  
                self.cursor.execute("INSERT A SEARCH QUERY HERE")

        elif Selection == "5":
                print("you chose 5")
                self.AdvancedOptions()

        else:
            print("Invalid selection!")

        self.Commit()
        self.BasicOptions()


    def AdvancedOptions(self):
        print("\nPlease select one of the following advanced options: {}".format(self.ExtraOptions))
        Selection = str(input("Enter option 1-8: "))
        if Selection == "1":
                print("you chose 1")
                Name = input("Enter new table Name: ")
                Contents = input("Enter new table columns: ")                   
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
                Columns = input("Enter column names to insert data into: ")
                Contents = input("Enter new table entries: ") 
                self.InsertIntoTable(Name, Columns, Contents)

        elif Selection == "6":
                print("you chose 6")
                Name = input("Enter table name to delete all entries from: ")
                self.DeleteAllEntiresInTable(Name)
           
        elif Selection == "7":
                print("you chose 7")
                self.Commit()
                print("Commit success")
                
        elif Selection == "8":
                print("you chose 8")
                self.Close()
                print("Connection closed")

        elif Selection == "9":
                print("you chose 9")
                self.BasicOptions()
                
        else:
            print("Invalid selection!")

        self.Commit()
        self.AdvancedOptions()


    def CommandInterface(self):
        self.Commit()
        self.BasicOptions()

#########################################################
########### Main Method

def main():
    AppInstance = App()
    AppInstance.Connect()
    AppInstance.Cursor()
    AppInstance.CommandInterface()


if __name__ == "__main__":
    main()
