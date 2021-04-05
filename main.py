import sys
import mysql.connector as mysql
from tabulate import tabulate
from prettytable import PrettyTable
import pandas as pd


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

def welcome():
    print()
    print("------------------------------------------------------------------")
    print("--------------------- Welcome to BKUni store ---------------------")
    print("------------------------------------------------------------------")
    print()




#Admin Functions
def Loggedin():
    print("--------------------- Login Information ---------------------")
    while True:
        username = input("Username:   ")
        password = input("Password:   ")
        cursor.execute("SELECT username FROM admin WHERE username = %s", (username,))
        record = cursor.fetchone()
        if record is not None:
            userConfirm = record[0]
            if userConfirm == username:
                cursor.execute("SELECT password FROM admin WHERE username = %s", (username,))
                row = cursor.fetchone()
                passConfirm = row[0]
                if passConfirm == password:
                    print()
                    print('Logged in Successfully')
                    break
                else:
                    print('Wrong Information Please Try Again!')
                    print()
            else:
                print('Wrong Information Please Try Again!')
                print()
        else:
            print('This Admin Does not Exist!!')
            print()




def print_books():
    cursor.execute("SELECT book_id, title, price, quantity, status FROM book")
    myresult = cursor.fetchall()
    print(tabulate(myresult, headers=['book id','title', 'price', 'quantity', 'status'], tablefmt='fancy_grid'))




def deleteBook():
    print_books()
    while True:
        book_id_delet = input("Enter Book id to delete: ")
        cursor.execute("SELECT title, price , quantity FROM book WHERE book_id = %s", (book_id_delet,))
        data = cursor.fetchone()
        if data is None:
            print("Wrong ID Try again")
        else:
            delet = "DELETE FROM book WHERE book_id = %s"
            delete_val = (book_id_delet,)
            cursor.execute(delet, delete_val)
            connection.commit()
            print("------------------Book removed successfully------------------")
            break





def read_price():
    flag = False
    while not flag:
        price = input("please enter the price book:")
        try:
            price = int(price)
            if price <= 0:
                print("!!!!!")
                print("Price cannot be negative or")
            else:
                return price
                flag = True
        except:
            print("Price can be numbers ONLY")



def readQuant():
    flag = False
    while not flag:
        quantity = input("please enter the number of books:")
        try:
            quantity = int(quantity)
            if quantity <= 0:
                print("!!!!!")
                print("Quantity cannot be negative or 0")
            else:
                return quantity
                flag = True
        except TypeError:
            print("Quantity is numbers ONLY")



def addBook():
        name = input("please enter the name of book:")
        price = read_price()
        quantity = readQuant()
        status = input("please enter the status of book:")
        insert = "INSERT INTO book(title,price,quantity,status) VALUES (%s,%s,%s,%s)"
        valuse = (name, price, quantity, status)
        cursor.execute(insert, valuse)
        connection.commit()
        print("------------------Book Details added successfully--------------------")



def updateBook():
    print_books()
    update = int(input("Enter Book id to update:"))
    while True:
        choice = input("what information of book you want to update? \n press:\n 1 to change book id \n 2 to change book name \n 3 to change book price \n 4 to change quantity of book \n")
        if (choice == '1'):
            while True:
                new_id = int(input("Enter new book id:"))
                cursor.execute("SELECT * FROM book WHERE book_id = %s", (new_id,))
                data = cursor.fetchone()
                if data is not None:
                    print("WRONG: This ID is Already exists!!")
                else:
                    update_id = "UPDATE book SET book_id =%s WHERE book_id =%s"
                    val_id = (new_id, update)
                    cursor.execute(update_id, val_id)
                    connection.commit()
                    print("------------------book updated successfully------------------")
                    break
            break

        elif (choice == '2'):
            new_name = int(input("Enter new book name:"))
            update_name = "UPDATE book SET book_title=%s WHERE book_id =%s"
            val_name = (new_name, update)
            cursor.execute(update_name, val_name)
            connection.commit()
            print("------------------book updated successfully------------------")
            break

        elif (choice == '3'):
            new_price = read_price()
            update_price = "UPDATE book SET price =%s WHERE book_id =%s"
            val_price = (new_price, update)
            cursor.execute(update_price, val_price)
            connection.commit()
            print("------------------book updated successfully------------------")
            break

        elif (choice == '4'):
            new_quantity = readQuant()
            update_quantity = "UPDATE book SET quantity=%s WHERE book_id =%s"
            val_quantity = (new_quantity, update)
            cursor.execute(update_quantity, val_quantity)
            connection.commit()
            print("------------------book updated successfully------------------")
            break

        elif (choice == '5'):
            new_status = int(input("Enter new book status:"))
            update_status = "UPDATE book SET status=%s WHERE book_id =%s"
            val_status = (new_status, update)
            cursor.execute(update_status, val_status)
            connection.commit()
            print("------------------book updated successfully------------------")
            break

        else:
            print("Please Choose only from the above menu !!")





def comments():
    cursor.execute("SELECT user_name, cooment FROM comment")
    myresult = cursor.fetchall()
    print(tabulate(myresult, headers=['user name','comment'], tablefmt='fancy_grid'))




#Student functions:

def printBill(list):
    if list is not None:
        table = PrettyTable(['Book title', 'Quantity','Price'])
        total = 0
        print(list)

        for record in list:
            table.add_row([record[0], record[1], record[2]])
            total += record[2]


        table.add_row(['TOTAL','', total])
        print(table)
        print('\nThanks for shopping with us :)')
        print('Your total bill amount is ', total, '/-')
        print()




def printBrrow(list = None):

    if list is not None:
        table = PrettyTable(['Book title', 'Quantity'])
        total = 0

        for record in list:
            table.add_row([record[0] , record[1]])

        print(table)
        print('\nThanks for Choosing BkUni :)')
        print('Your total bill amount is ', total, '/-')




def buy_book():
    shoppingCart = []
    flag = False
    while not flag:
        print_books()
        while True:
            try:
                book_ID = int(input("Enter Book ID you want to buy: "))
                numOfbooks = int(input("How many copy you want? "))
                if numOfbooks <= 0:
                    print("!!!!!!!")
                    print("Quantity Can not be negative or 0")
                else:
                    break
            except ValueError:
                print("ID And Quantity can only be a numbers!")

        cursor.execute("SELECT title, price , quantity FROM book WHERE book_id = %s", (book_ID,))
        data = cursor.fetchone()
        if data is None:
            print("Wrong ID please try again")
        else:
            cursor.execute("SELECT quantity FROM book WHERE book_id = %s", (book_ID,))
            row = cursor.fetchone()
            quantity = row[0]
            if quantity <= 0:
                print("Sorry the book out of stock..")
            else:
                list = []
                cursor.execute("SELECT title, price FROM book WHERE book_id = %s",(book_ID,))
                record = cursor.fetchone()
                title = record[0]
                price = record[1]
                final_price = numOfbooks * price
                list.append(title)
                list.append(numOfbooks)
                list.append(final_price)
                shoppingCart.append(tuple(list))
                quantity = quantity - numOfbooks
                cursor.execute("UPDATE book SET quantity = %s WHERE book_id = %s", (quantity, book_ID))
                connection.commit()
                print()
                print("--- Current Shopping Cart ---")
                printBill(shoppingCart)
            conti = '0'
            while conti != '2':
                conti = input("Contuneiu? \n 1. yes \n 2.no \n")
                if conti == '1':
                    break
                elif conti == '2':
                    # final Bill ....
                    print("--------------------- You Can Visit in the nearest branch us to pick up the Book --------------------")
                    flag = True
                elif conti == None or conti == '':
                    print("Please Enter an option")
                else:
                    print("unknown Option")



def borrow_book():
    shoppingCart = []
    flag = False
    while not flag:
        print_books()
        while True:
            try:
                book_ID = int(input("Enter Book ID you want to borrow: "))
                numOfbooks = int(input("How many copy you want? "))
                break
            except ValueError:
                print("ID And Quaninty can only be a numbers!")

        cursor.execute("SELECT * FROM book WHERE book_id = %s", (book_ID,))
        data = cursor.fetchone()
        if data is None:
            print("Wrong ID please try again")
        else:
            cursor.execute("SELECT quantity FROM book WHERE book_id = %s", (book_ID,))
            row = cursor.fetchone()
            quantity = row[0]
            if quantity <= 0:
                print("Sorry the book out of stock..")
            else:
                list = []
                cursor.execute("SELECT title, price FROM book WHERE book_id = %s", (book_ID,))
                record = cursor.fetchone()
                title = record[0]
                list.append(title)
                list.append(numOfbooks)
                shoppingCart.append(tuple(list))
                cursor.execute("SELECT status FROM book WHERE book_id = %s", (book_ID,))
                row = cursor.fetchone()
                status = row[0]
                status = "Borrowed"
                cursor.execute("UPDATE book SET status = %s WHERE book_id = %s", (status, book_ID))
                connection.commit()
                print()
                print("--- Current Shopping Cart ---")
                printBrrow(shoppingCart)
            conti = '0'
            while conti != '2':
                conti = input("Contuneiu? \n 1. yes \n 2.no \n")
                if conti == '1':
                    break
                elif conti == '2':
                    # final Bill ....
                    print("--------------------- You Can Visit in the nearest branch us to pick up the Book --------------------")
                    flag = True
                elif conti == None or conti == '':
                    print("Please Enter an option")
                else:
                    print("unkown Option")



def user_comment():
    print("Cause here in BkUni we care about our customer, We design this\n to help you share your opinion and thoughts")
    name = input("Please Provide You Name: ")
    comment = input("Enter your comment: ")
    insert = "INSERT INTO comment(user_name,cooment) VALUES (%s,%s)"
    valuse = (name, comment)
    cursor.execute(insert, valuse)
    connection.commit()
    print("------------------ Your comment is well recived, Thank You --------------------")


def searchBook():
    while True:
        user_input = input("book name: ")
        cursor.execute("SELECT title,quantity,price,status FROM book WHERE title LIKE %s", ("%" + user_input + "%",))
        result = cursor.fetchall()
        if len(result) > 0:
            print("Found: ", len(result))
            for row in result:
                print(row)
            break
        else:
            print("No book existing with the entered name !!")



while True:

    welcome()
    SE = input(" Plase Choose From The below: \n 1)Admin \n 2)Student \n 3) Exit \n enter your select :")

    # Admin Part:
    if SE == '1':
        print()
        admin = '0'
        #Login for admin:
        Loggedin()
        while admin != '6':
            print()
            print("--------------------- Welcome to BKUni Admin System --------------------")
            print("1.Add new Book")
            print("2.Delete book")
            print("3.Modify books ")
            print("4.View the borrowing status ")
            print("5.View Students comments")
            print("6.Log out")
            admin = input("enter choice : ")

            if admin == '1':
                print()
                addBook()


            elif admin == '2':
                print()
                deleteBook()



            elif admin == '3':
                print()
                updateBook()

            elif admin == '4':
                print()
                print_books()

            elif admin == '5':
                comments()


            elif admin == '6':
                print("Logged out Successfully")
                break

            elif admin == None or admin == '':
                print("Please Enter a choice")

            else:
                print("Unknown Option ... Please Try Again")







    # student Part
    elif SE == '2':
        print("--------------------- Welcome to BKUni --------------------")
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
            st = input("enter choice : ")


            if st == '1':

                print()
                print("------------------ Available Books in BKUni ------------------")
                print()
                print_books()

            elif st == '2':
                buy_book()

            elif st == '3':
                borrow_book()

            elif st == '4':
                searchBook()

            elif st == '5':
                print()
                user_comment()



            elif st == "" or st == None:
                print("Please Enter a choice")

            else:
                print("Unknown Option please try again!!")

        break

    elif SE == '3':
        print("Thank You For using BkUni ... See You Soon ... Bye Bye")
        print()

    else:
        print("Unknown option ... please try again")


sys.exit()



