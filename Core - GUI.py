#Imports
import sqlite3
#GUI Imports
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class App(tkinter.Frame):
    def __init__(self, master=None):
        #Variables
        self.DatabaseConnection = None
        self.cursor = None
        self.Options = "CreateTable(1), DeleteTable(2), ShowTables(3), ShowTableContents(4), InsertIntoTable(5), Commit(6), Close(7)"
        self.newline_indent = '\n   '

        #GUI variables
        self.GUIRoot = Tk()
        #super().__init__(self.GUIRoot)
        #self.frame = ttk.Frame(self.GUIRoot)
        self.GUIRoot.title("Attendence Record System Executable")
        self.GUIRoot.geometry("800x400")

        self.rows = 0
        while self.rows < 50:
            self.GUIRoot.rowconfigure(self.rows, weight=1)
            self.GUIRoot.columnconfigure(self.rows,weight=1)
            self.rows += 1

        #self.frame.grid()
            
        #self.GUIRoot.columnconfigure((0), weight=1)
        #self.GUIRoot.rowconfigure((0,1,2,3,4,5,6,7,8,9), weight=1)
        
        #self.frame.grid_propagate(0) #stops auto window resize
        self.GUIRoot.resizable(0, 0)
        self.SignInPage()



######################################################################
        ###GUI OPERATIONS


    def clear_frame(self):
        for widgets in self.GUIRoot.winfo_children():
            widgets.destroy()


    def SignInPage(self):
        
        ttk.Label(self.GUIRoot, text="Welcome, please login").grid(column=25, row=3)
        
        #self.text = StringVar()
        #ttk.Entry(textvar=self.text).grid(column=1, row=2)
        
        ttk.Button(self.GUIRoot, text="Sign In", command=lambda:[self.clear_frame(),self.MainMenu()]).grid(column=25, row=5)


    def MainMenu(self):
        ttk.Label(self.GUIRoot, text="Welcome, please choose an option: ").grid(column=2, row=0, columnspan=1, padx=10, pady=10)
        ttk.Button(self.GUIRoot, text="Add Student", command=lambda:[self.clear_frame(),self.Add_Student_Menu()]).grid(column=0, row=2, padx=10, pady=10)
        ttk.Button(self.GUIRoot, text="Record Attendence", command=lambda:[self.clear_frame(),self.Record_Attendence_Menu()]).grid(column=1, row=2, padx=10, pady=10)
        ttk.Button(self.GUIRoot, text="Record Parts, Topics or Tests", command=lambda:[self.clear_frame(),self.RecordPartsTopicsTestsMenu()]).grid(column=2, row=2, padx=10, pady=10)
        ttk.Button(self.GUIRoot, text="Search Student Details and Achievements", command=lambda:[self.clear_frame(),self.SearchStudentDetailsAndAchievementsMenu()]).grid(column=3, row=2, padx=10, pady=10)


    def Add_Student_Menu(self):
        ttk.Label(self.GUIRoot, text="Please enter new Students Details: ").grid(column=1, row=0, padx=5, pady=5)
        
        ttk.Label(self.GUIRoot, text="First Name: ").grid(column=0, row=2, padx=5, pady=5)
        self.text1 = StringVar()
        ttk.Entry(self.GUIRoot, textvar=self.text1).grid(column=1, row=2, padx=5, pady=5)

        ttk.Label(self.GUIRoot, text="Last Name: ").grid(column=0, row=4, padx=5, pady=5)
        self.text2 = StringVar()
        ttk.Entry(self.GUIRoot, textvar=self.text2).grid(column=1, row=4, padx=5, pady=5)

        ttk.Label(self.GUIRoot, text="DOB (YYYY-MM-DD): ").grid(column=0, row=6, padx=5, pady=5)
        self.text3 = StringVar()
        ttk.Entry(self.GUIRoot, textvar=self.text3).grid(column=1, row=6, padx=5, pady=5)
        
        ttk.Button(self.GUIRoot, text="Submit", command=lambda:[self.SubmitStudent(self.text1.get(), self.text2.get(), self.text3.get())]).grid(column=1, row=7, padx=5, pady=5)

        ttk.Button(self.GUIRoot, text="Main Menu", command=lambda:[self.clear_frame(),self.MainMenu()]).grid(column=0, row=45, padx=5, pady=5)


    def SubmitStudent(self, a: str, b: str, c: str):
        self.cursor.execute("INSERT INTO Student VALUES (?,?,?,?);", (None, a, b, c))
        self.Commit()



    def Record_Attendence_Menu(self):
        ttk.Label(self.GUIRoot, text="Please enter new attendence record: ").grid(column=2, row=0, padx=5, pady=5)
        
        ttk.Label(self.GUIRoot, text="weekNumber").grid(column=1, row=2, padx=5, pady=5)
        self.text1 = StringVar()
        ttk.Entry(self.GUIRoot, textvar=self.text1).grid(column=2, row=2, padx=5, pady=5)

        ttk.Label(self.GUIRoot, text="Student ID: ").grid(column=1, row=4, padx=5, pady=5)
        self.text2 = StringVar()
        ttk.Entry(self.GUIRoot, textvar=self.text2).grid(column=2, row=4, padx=5, pady=5)
        
        ttk.Button(self.GUIRoot, text="Submit", command=lambda:[self.SubmitAttendence(self.text1.get(), self.text2.get())]).grid(column=2, row=5, padx=5, pady=5)

        ttk.Button(self.GUIRoot, text="Main Menu", command=lambda:[self.clear_frame(),self.MainMenu()]).grid(column=1, row=45, padx=5, pady=5)


    def SubmitAttendence(self, a: str, b: str):
        self.cursor.execute("INSERT INTO ATTENDENCE VALUES (?,?);", (a, b))
        self.Commit()



    def RecordPartsTopicsTestsMenu(self):
        ttk.Label(self.GUIRoot, text="Please enter new attendence record: ").grid(column=1, row=0, columnspan=1, padx=5, pady=5)
        
        ttk.Label(self.GUIRoot, text="weekNumber").grid(column=1, row=1, padx=15, pady=5)
        self.text1 = StringVar()
        ttk.Entry(self.GUIRoot, textvar=self.text1).grid(column=2, row=1, padx=15, pady=5)

        ttk.Label(self.GUIRoot, text="Student ID: ").grid(column=1, row=2, padx=5, pady=5)
        self.text2 = StringVar()
        ttk.Entry(self.GUIRoot, textvar=self.text2).grid(column=2, row=2, padx=5, pady=5)
        
        ttk.Button(self.GUIRoot, text="Submit", command=lambda:[self.SubmitPartsTopicsTests(self.text1.get(), self.text2.get())]).grid(column=2, row=4, padx=10, pady=10)

        ttk.Button(self.GUIRoot, text="Main Menu", command=lambda:[self.clear_frame(),self.MainMenu()]).grid(column=10, row=10, padx=10, pady=10, sticky='SE')


    def SubmitPartsTopicsTests(self, a: str, b: str):
        self.cursor.execute("INSERT INTO Student VALUES (?,?);", (a, b))
        self.Commit()

    
    def SearchStudentDetailsAndAchievementsMenu(self):
        ttk.Label(self.GUIRoot, text="Please enter Student Name to search: ").grid(column=2, row=0, padx=5, pady=5)
        
        ttk.Label(self.GUIRoot, text="Student First Name: ").grid(column=1, row=2, padx=5, pady=5)
        self.text1 = StringVar()
        ttk.Entry(self.GUIRoot, textvar=self.text1).grid(column=2, row=2, padx=2, pady=5)

        ttk.Label(self.GUIRoot, text="Student Last Name:  ").grid(column=1, row=4, padx=5, pady=5)
        self.text2 = StringVar()
        ttk.Entry(self.GUIRoot, textvar=self.text2).grid(column=2, row=4, padx=5, pady=5)
        
        ttk.Button(self.GUIRoot, text="Submit", command=lambda:[self.GetSearchResult(self.text1.get(),self.text2.get()), self.DisplaySearchResult()]).grid(column=2, row=5, padx=10, pady=10)

        ttk.Button(self.GUIRoot, text="Main Menu", command=lambda:[self.clear_frame(),self.MainMenu()]).grid(column=1, row=45, padx=10, pady=10, sticky="W")


    def GetSearchResult(self, a: str, b: str):
        #self.StudentSearchResult = self.cursor.execute("SELECT studentID, DOB FROM Student WHERE firstName = '{}' AND lastName = '{}';".format(str(a), str(b))).fetchall()
        self.StudentSearchResult = self.cursor.execute("SELECT studentID, DOB, name, tier, type FROM Student, Badge WHERE Badge.badgeID = StudentBadge.badgeID AND Student.studentID = StudentBadge.studentID AND firstName = '{}' AND lastName = '{}';".format(str(a), str(b)))
        print(self.StudentSearchResult)


    def DisplaySearchResult(self):
        print(self.StudentSearchResult)
        #tkinter.messagebox.showinfo(self.StudentSearchResult)
        ttk.Label(self.GUIRoot, text=self.StudentSearchResult).grid(column=1, row=5, columnspan=1, padx=5, pady=5)

        
######################################################################
        ###SQL OPERATIONS METHODS

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


    def InsertIntoTable(self, Name: str, Columns: str, Contents: str):
        self.cursor.execute('''INSERT INTO {}({}) VALUES ({});'''.format(Name, Columns, Contents))


    def Commit(self):
        self.DatabaseConnection.commit()


    def Close(self):
        self.DatabaseConnection.close()


    def Connect(self):
        self.DatabaseConnection = sqlite3.connect("C:\sqlite\Database\Database.db")
        print("Successfully connected to database")


    def Cursor(self):
        self.cursor = self.DatabaseConnection.cursor()


########################################################################
        ###Selection Methods

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
                Columns = input("Enter column names to insert data into: ")
                Contents = input("Enter new table entries: ") 
                self.InsertIntoTable(Name, Columns, Contents)
                
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
        #self.Selections()
        
#########################################
        ###MAIN METHODS


def main():
    AppInstance = App()
    AppInstance.Connect()
    AppInstance.Cursor()
    AppInstance.CommandInterface()
    
    AppInstance.GUIRoot.mainloop()
    

if __name__ == "__main__":
    main()
