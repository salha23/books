from main import *
from tabulate import tabulate
from prettytable import PrettyTable




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
        else:
            print('Wrong Information Please Try Again!')



def deleteBook():
    book_id_delet = input("Enter Book id to delete: ")
    delet = "DELETE FROM book WHERE book_id = %s"
    delete_val = (book_id_delet,)
    cursor.execute(delet, delete_val)
    connection.commit()
    print("------------------Book removed successfully------------------")



def addBook():
    name = input("please enter the name of book:")
    price = input("please enter the price book:")
    quantity = input("please enter the number of books:")
    status = input("please enter the status of book:")
    insert = "INSERT INTO book(title,price,quantity,status) VALUES (%s,%s,%s,%s)"
    valuse = (name, price, quantity, status)
    cursor.execute(insert, valuse)
    connection.commit()
    print("------------------Book Details added successfully--------------------")



def updateBook():
    update = int(input("Enter Book id to update:"))
    choice = int(input(
        "what information of book you want to update? \n press:\n 1 to change book id \n 2 to change book name \n 3 to change book price \n 4 to change quantity of book \n"))
    if (choice == 1):
        new_id = int(input("Enter new book id:"))
        update_id = "UPDATE book SET book_id =%s WHERE book_id =%s"
        val_id = (new_id, update)
        cursor.execute(update_id, val_id)
        connection.commit()
        print("------------------book updated successfully------------------")

    if (choice == 2):
        new_name = int(input("Enter new book name:"))
        update_name = "UPDATE book SET book_title=%s WHERE book_id =%s"
        val_name = (new_name, update)
        cursor.execute(update_name, val_name)
        connection.commit()
        print("------------------book updated successfully------------------")

    if (choice == 3):
        new_price = int(input("Enter new book price:"))
        update_price = "UPDATE book SET price =%s WHERE book_id =%s"
        val_price = (new_price, update)
        cursor.execute(update_price, val_price)
        connection.commit()
        print("------------------book updated successfully------------------")

    if (choice == 4):
        new_quantity = int(input("Enter new book quantity:"))
        update_quantity = "UPDATE book SET quantity=%s WHERE book_id =%s"
        val_quantity = (new_quantity, update)
        cursor.execute(update_quantity, val_quantity)
        connection.commit()
        print("------------------book updated successfully------------------")

    elif (choice == 5):
        new_status = int(input("Enter new book status:"))
        update_status = "UPDATE book SET status=%s WHERE book_id =%s"
        val_status = (new_status, update)
        cursor.execute(update_status, val_status)
        connection.commit()
        print("------------------book updated successfully------------------")




def viewBookStatus():
    book_id = int(input("Enter the book ID that you want to see the status:"))
    sql = "select status from book where book_id=%s"
    val = (book_id,)
    cursor.execute(sql, val)
    print("----------", cursor.fetchall())


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

        #table.add_row(['TOTAL', total])
        print(table)
        print('\nThanks for shopping with us :)')
        print('Your total bill amount is ', total, '/-')




def printBrrow(list = None):

    if list is not None:
        table = PrettyTable(['Book title', 'Quantity'])
        total = 0
        print(list)

        for record in list:
            table.add_row([record[0] , record[1]])


        table.add_row(['TOTAL', total])
        print(table)
        print('\nThanks for shopping with us :)')
        print('Your total bill amount is ', total, '/-')





def print_books():
    cursor.execute("SELECT book_id, title, price, quantity, status FROM book")
    myresult = cursor.fetchall()
    print(tabulate(myresult, headers=['book id','title', 'price', 'quantity', 'status'], tablefmt='fancy_grid'))



def buy_book():
    shoppingCart = []
    list = []
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
                    print(
                        "--------------------- You Can Visit in the nearest branch us to pick up the Book --------------------")
                    flag = True
                elif conti == None or conti == '':
                    print("Please Enter an option")
                else:
                    print("unkown Option")



def borrow_book():
    shoppingCart = []
    list = []
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

