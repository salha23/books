from functions_file import *
import sys
import mysql.connector as mysql



connection=mysql.connect(
 host="localhost",
 user="root",
 password="",
 database="BKUni",
 auth_plugin='mysql_native_password'
)

#class BKUni:
cursor =connection.cursor()


#cursor.execute("SHOW DATABASES")
#for x in cursor:
#     print(x)



a = Admin()
s = buyer()
c = commonFunc()



c.welcome()

while True:

    SE = input(" Plase Choose From The below: \n 1)Admin \n 2)Buyer \n 3) Exit \n enter your select :   ")

    # Admin Part:
    if SE == '1':
        print()
        admin = '0'
        #Login for admin:
        a.Loggedin()
        while admin != '6':
            print()
            print("--------------------- Welcome to BKUni Admin System --------------------")
            print("1.Add new Book")
            print("2.Delete book")
            print("3.Modify books ")
            print("4.View the borrowing status ")
            print("5.View Students comments")
            print("6.Log out")
            admin = input("enter choice :   ")
            print()

            if admin == '1':
                print()
                a.addBook()
                print()


            elif admin == '2':
                print()
                a.deleteBook()
                print()



            elif admin == '3':
                print()
                a.updateBook()
                print()

            elif admin == '4':
                print()
                c.print_books()
                print()

            elif admin == '5':
                print()
                a.comments()
                print()


            elif admin == '6':
                print("Logged out Successfully")
                break

            elif admin == None or admin == '':
                print(colored("Please Enter a choice","red"))

            else:
                print(colored("Unknown Option ... Please Try Again","red"))







    # student Part
    elif SE == '2':
        print("--------------------- Welcome to BKUni --------------------")
        print()
        st = '0'
        while st != '6':
            print()
            print()
            print("--------------------- Menu --------------------")
            print("1.View the available books in BKUni")
            print("2.Buy a books ")
            print("3.Borrow a books ")
            print("4.Search for a specific books")
            print("5.Rating a bought or borrowed books")
            print("6.Exit")
            st = input("enter choice :   ")


            if st == '1':

                print()
                c.print_books()
                print()


            elif st == '2':
                print()
                s.buy_book()
                print()

            elif st == '3':
                print()
                s.borrow_book()
                print()

            elif st == '4':
                print()
                s.searchBook()
                print()

            elif st == '5':
                print()
                s.user_comment()
                print()

            elif st == '6':
                print()
                print("Thank You For using BkUni ... See You Soon ... Bye Bye")
                print()
                break

            elif st == "" or st == None:
                print()
                print(colored("Please Enter a choice","red"))
                print()

            else:
                print()
                print(colored("Unknown Option ... Please Try Again","red"))
                print()


    elif SE == '3':
        print()
        print("Thank You For using BkUni ... See You Soon ... Bye Bye")
        print()
        break

    else:
        print()
        print(colored("Unknown option ... please try again","red"))
        print()


sys.exit()



