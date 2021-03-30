import sys

import MySQLdb as mysql
import MySQLdb.cursors as c

def startCon(self):
    con = mysql.connect(
        host="localhost",
        port="3306",
        user="root",
        password="1234",
        database="BKUni"
    )
    return con





print("Welcome to Books store")
SE = int(input(" 1)Admin \n 2)Student \n enter your select :"))

while True:
    if SE == 1:
        admin = 0
        while admin != 5:
         print("1.Add new Book")
         print("2.Delete book")
         print("3.Modify books ")
         print("4.View the borrowing status ")
         print("5.Exit")
         admin = int(input("enter choice : "))
         if admin == 1:
             print("here you can added")

         elif admin == 2:
             print("hi")

         elif admin == 4:
             print("hi")

         elif admin == 5:
             break
        SE = int(input(" 1)Admin \n 2)Student \n enter your select :"))


    elif SE == 2:
        print("Welcome student ")
        st = 0
        while st != 5:
            print("1.View the available books in BKUni")
            print("2.Buy a books ")
            print("3.Borrow a books ")
            print("4.Search for a specific books")
            print("5.Exit")
            st = int(input("enter choice : "))
            if st == 1:
                print("")
        break
    else:
        print("Unknown Option Selected! pleas try again ")
        SE = int(input(" 1)Admin \n 2)Student \n enter your select :"))

sys.exit()

