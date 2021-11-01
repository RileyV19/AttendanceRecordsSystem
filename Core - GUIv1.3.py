# SQL Imports
import sqlite3

# GUI Imports
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#+------------------------------------------------
#|  Main App class
#|    - All methods that require a connection to 
#|      the sqlite3 database are contained here
#|    - Graphic User Interface (GUI) methods are
#|      contained here also
#+------------------------------------------------
class App(tkinter.Frame):
    def __init__(self, master=None):
        # Variables
        self.DatabaseConnection = None
        self.cursor = None
        self.Options = "CreateTable(1), DeleteTable(2), ShowTables(3), ShowTableContents(4), InsertIntoTable(5), Commit(6), Close(7)" 
        self.newline_indent = '\n   '

        # GUI variables
        self.GUIRoot = Tk()
        self.GUIRoot.title("Attendence Record System Executable")
        self.GUIRoot.geometry("900x400")

        self.rows = 0
        while self.rows < 50:
            self.GUIRoot.rowconfigure(self.rows, weight=1)
            self.GUIRoot.columnconfigure(self.rows,weight=1)
            self.rows += 1
        self.GUIRoot.resizable(0, 0)
        self.SignInPage()



    #+---------------------------------------
    #|  GUI functions - GUI methods for buttons, entry boxes and data viewing
    #+---------------------------------------

    # Reset GUI (clear)
    def clear_frame(self):
        for widgets in self.GUIRoot.winfo_children():
            widgets.destroy()

    # Sign in page
    def SignInPage(self):
        ttk.Label(self.GUIRoot, text="Welcome, please login").grid(column=25, row=3)
        ttk.Button(self.GUIRoot, text="Sign In", command=lambda:[self.clear_frame(),self.MainMenu()]).grid(column=25, row=5)

    # main Menu
    def MainMenu(self):
        ttk.Label(self.GUIRoot, text="Welcome, please choose an option: ").grid(column=2, row=0, columnspan=1, padx=10, pady=10)
        ttk.Button(self.GUIRoot, text="Add Student", command=lambda:[self.clear_frame(),self.Add_Student_Menu()]).grid(column=0, row=2, padx=10, pady=10)
        ttk.Button(self.GUIRoot, text="Record Attendence", command=lambda:[self.clear_frame(),self.Record_Attendence_Menu()]).grid(column=1, row=2, padx=10, pady=10)
        ttk.Button(self.GUIRoot, text="Record Parts, Topics or Tests", command=lambda:[self.clear_frame(),self.RecordStudentPartsTopicsTestsMenu()]).grid(column=2, row=2, padx=10, pady=10)
        ttk.Button(self.GUIRoot, text="Search Student Details and Achievements", command=lambda:[self.clear_frame(),self.SearchStudentDetailsAndAchievementsMenu()]).grid(column=3, row=2, padx=10, pady=10)
        ttk.Button(self.GUIRoot, text="Leaderboard", command=lambda:[self.clear_frame(),self.StudentLeaderboard()]).grid(column=2, row=4, padx=10, pady=10)

    # Add student menu
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

    # Commit add student
    def SubmitStudent(self, a: str, b: str, c: str):
        self.cursor.execute("INSERT INTO Student VALUES (?,?,?,?);", (None, a, b, c))
        self.Commit()

    # Record Attendance
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

    # Commit record attendance
    def SubmitAttendence(self, a: str, b: str):
        self.cursor.execute("INSERT INTO STUDENTATTENDENCE VALUES (?,?,?);", (None,a, b))
        self.Commit()


    # Record parts, tests and topics completed by a student
    def RecordStudentPartsTopicsTestsMenu(self):
        ttk.Label(self.GUIRoot, text="Record Student Completion of Part, Topic or Test:").grid(column=1, row=0, padx=5, pady=5)
        
        ttk.Label(self.GUIRoot, text="Part, Topic or Test?").grid(column=0, row=2, padx=5, pady=5)
        self.text1 = StringVar()
        ttk.Entry(self.GUIRoot, textvar=self.text1).grid(column=1, row=2, padx=5, pady=5)

        ttk.Label(self.GUIRoot, text="Student ID:").grid(column=0, row=4, padx=5, pady=5)
        self.text2 = StringVar()
        ttk.Entry(self.GUIRoot, textvar=self.text2).grid(column=1, row=4, padx=5, pady=5)

        ttk.Label(self.GUIRoot, text="part,topic,test ID:").grid(column=0, row=6, padx=5, pady=5)
        self.text3 = StringVar()
        ttk.Entry(self.GUIRoot, textvar=self.text3).grid(column=1, row=6, padx=5, pady=5)
        
        
        ttk.Button(self.GUIRoot, text="Submit", command=lambda:[self.SubmitStudentPartsTopicsTests(self.text1.get(), self.text2.get(), self.text2.get())]).grid(column=1, row=7, padx=10, pady=10)

        ttk.Button(self.GUIRoot, text="Main Menu", command=lambda:[self.clear_frame(),self.MainMenu()]).grid(column=0, row=45, padx=10, pady=10, sticky='SE')

    # Commit record sections
    def SubmitStudentPartsTopicsTests(self, a: str, b: str, c: str):
        self.cursor.execute("INSERT INTO STUDENT{} VALUES (?,?,?);".format(a),(None, b, c))
        self.Commit()

    # Search for a student and see their details
    def SearchStudentDetailsAndAchievementsMenu(self):
        ttk.Label(self.GUIRoot, text="Please enter Student Name to search: ").grid(column=1, row=0, padx=5, pady=5)
        
        ttk.Label(self.GUIRoot, text="Student First Name: ").grid(column=0, row=2, padx=5, pady=5)
        self.text1 = StringVar()
        ttk.Entry(self.GUIRoot, textvar=self.text1).grid(column=1, row=2, padx=2, pady=5)

        ttk.Label(self.GUIRoot, text="Student Last Name:  ").grid(column=0, row=4, padx=5, pady=5)
        self.text2 = StringVar()
        ttk.Entry(self.GUIRoot, textvar=self.text2).grid(column=1, row=4, padx=5, pady=5)
        
        ttk.Button(self.GUIRoot, text="Submit", command=lambda:[self.GetSearchResult(self.text1.get(),self.text2.get())]).grid(column=1, row=5, padx=10, pady=10)

        ttk.Button(self.GUIRoot, text="Main Menu", command=lambda:[self.clear_frame(),self.MainMenu()]).grid(column=0, row=45, padx=10, pady=10, sticky='SE')

    # Print search result to GUI
    def GetSearchResult(self, a: str, b: str):
        self.StudentSearchResult = self.cursor.execute("SELECT studentID, DOB FROM Student WHERE firstName = '{}' AND lastName = '{}';".format(str(a), str(b))).fetchall()
        self.StudentSearchResult2 = self.cursor.execute("SELECT name, tier, type FROM Badge, Student, StudentBadge WHERE Badge.badgeID = StudentBadge.badge AND Student.studentID = StudentBadge.student AND firstName = '{}' AND lastName = '{}';".format(str(a), str(b))).fetchall()
        self.CombinedResults = str(self.StudentSearchResult + self.StudentSearchResult2)
        self.var = ttk.Label(self.GUIRoot, text=self.CombinedResults).grid(column=35, row=2, columnspan=1, padx=5, pady=5)

    # Show badge leaderboard
    def StudentLeaderboard(self):
        ttk.Label(self.GUIRoot, text="Student Leaderboard: ").grid(column=2, row=0, padx=5, pady=5)

        self.GetStudentLeaderboardResults()

        ttk.Button(self.GUIRoot, text="Main Menu", command=lambda:[self.clear_frame(),self.MainMenu()]).grid(column=0, row=45, padx=10, pady=10, sticky='SE')

    # Calculate leaderboard standings
    def GetStudentLeaderboardResults(self):
        self.StudentSearchResult = self.cursor.execute("SELECT student, tier FROM StudentBadge JOIN Badge ON StudentBadge.badge = Badge.badgeID;").fetchall()

        All_StudentBadges_Dictionary = {}

        Lithium = 0
        Platinum = 0
        Diamond = 0
        
        for result in self.StudentSearchResult:
                if result[0] not in All_StudentBadges_Dictionary.keys():
                    All_StudentBadges_Dictionary[result[0]] = (0,0,0)
                    
                CurrentData = list(All_StudentBadges_Dictionary[result[0]])
                
                if result[1] == 'Lithium':
                    CurentData[2] = CurentData[2] + 1
                    
                elif result[1] == 'Platinum':
                    CurrentData[1] = CurrentData[1] + 1

                elif result[1] == 'Diamond':
                    CurrentData[0] = CurrentData[0] + 1

                All_StudentBadges_Dictionary[result[0]] = CurrentData

        self.FormattedResult = dict(sorted(All_StudentBadges_Dictionary.items(), key=lambda item: item[1], reverse=True))
        self.lol = "Student ID\tDiam\tPlat\tLith\n"
        for key, value in self.FormattedResult.items():
            self.lol = self.lol + "\t" + str(key) + "\t" + str(value[0]) + "\t" + str(value[1]) + "\t" + str(value[2]) + "\n"

        self.var = ttk.Label(self.GUIRoot, text=self.lol).grid(column=2, row=2, columnspan=1, rowspan=10, padx=5, pady=5)
  
#############################################################################
    #+---------------------------------------
    #|  SQL functions - Create, delete, modify, show tables and entries
    #+---------------------------------------

    # Create table
    def CreateTable(self, Name: str, Contents: str):
        self.cursor.execute('''CREATE TABLE {} ({});'''.format(Name, Contents))

    # Delete Table
    def DeleteTable(self, Name: str):
        self.cursor.execute('''DROP TABLE {};'''.format(Name))

    # Show tables in Database
    def ShowTables(self):
        newline_indent = '\n   '
        result = self.cursor.execute('''SELECT name FROM sqlite_master WHERE type='table';''').fetchall()
        table_names = sorted(list(zip(*result))[0])
        print ("\ntables with columns:" + newline_indent)
        for table_name in table_names:
            result = self.cursor.execute("PRAGMA table_info('%s')" % table_name).fetchall()
            column_names = list(zip(*result))[1]
            print("\t" + (table_name) + "\t" + str(column_names))

    # Show table contents
    def ShowTableContents(self, Name: str):
        newline_indent = '\n   '
        result = self.cursor.execute('''SELECT * FROM {};'''.format(Name)).fetchall()
        print(result)

    # Add data to table
    def InsertIntoTable(self, Name: str, Columns: str, Contents: str):
        self.cursor.execute('''INSERT INTO {}({}) VALUES ({});'''.format(Name, Columns, Contents))

    #+---------------------------------------
    #|  SQL connection functions - Establish and close the connection, prepare the cursor
    #+---------------------------------------

    # Start a connection
    def Connect(self):
        self.DatabaseConnection = sqlite3.connect("C:\sqlite\Database\Database.db")
        print("Welcome to the Attendance Record System Executable!")# Welcome message

    # Execute SQL Query
    def Commit(self):
        self.DatabaseConnection.commit()

    # Close connection
    def Close(self):
        self.DatabaseConnection.close()

    # Initialise SQL cursor
    def Cursor(self):
        self.cursor = self.DatabaseConnection.cursor()


    #+---------------------------------------
    #|  Advanced User Interface (command line) - create and manipulate data as administrator
    #+---------------------------------------

    
    def Selections(self):
        print("\nPlease select one of the following options: {}".format(self.Options))
        Selection = str(input("Enter option 1-7: "))

        # Create new table
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

        # Show Tables
        elif Selection == "3":
                print("you chose 3")
                self.ShowTables()

        # Show Table Contents
        elif Selection == "4":
                print("you chose 4")
                Name = input("Enter table name to display its contents: ")  
                self.ShowTableContents(Name)

        # Add data to table
        elif Selection == "5":
                print("you chose 5")
                Name = input("Enter table name to insert data into: ")
                Columns = input("Enter column names to insert data into: ")
                Contents = input("Enter new table entries: ") 
                self.InsertIntoTable(Name, Columns, Contents)

        # Commit
        elif Selection == "6":
                print("you chose 6")
                self.Commit()
                print("Commit success")

        # Close Connection
        elif Selection == "7":
                print("you chose 7")
                self.Close()
                print("Connection closed")

        # Error 
        else:
            print("invalid selection")
        
        self.Selections()

    # Start interface
    def CommandInterface(self):
        self.Commit()
        #self.Selections()
        
        
####################################################################################################
######### Main Method

def main():
    AppInstance = App()
    AppInstance.Connect()
    AppInstance.Cursor()
    AppInstance.CommandInterface()
    AppInstance.GUIRoot.mainloop()
    

if __name__ == "__main__":
    main()
