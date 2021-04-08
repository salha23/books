import mysql.connector as mysql
from tabulate import tabulate
from prettytable import PrettyTable
from termcolor import colored


connection=mysql.connect(
 host="localhost",
 user="root",
 password="",
 database="BKUni",
 auth_plugin='mysql_native_password'
)

#class BKUni:
cursor =connection.cursor()


#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------- COMMON FUNCTIONS ----------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#



class commonFunc:

    def print_books(self):
        print("--------------------- Available Books in BKUni ---------------------")
        cursor.execute("SELECT book_id, title, price, quantity, status FROM book")
        myresult = cursor.fetchall()
        print(tabulate(myresult, headers=['book id', 'title', 'price', 'quantity', 'status'], tablefmt='fancy_grid'))

    def welcome(self):
        print()
        print("------------------------------------------------------------------")
        print("--------------------- Welcome to BKUni store ---------------------")
        print("------------------------------------------------------------------")
        print()




#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------- ADMIN FUNCTIONS ----------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#





class Admin:



    def Loggedin(self):
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
                        print(colored('Logged in Successfully','green'))
                        break
                    else:
                        print(colored('Wrong Information Please Try Again!','red'))
                        print()
                else:
                    print(colored('Wrong Information Please Try Again!','red'))
                    print()
            else:
                print(colored('Wrong Information Please Try Again!','red'))
                print()



    def deleteBook(self):
        c = commonFunc()
        c.print_books()
        while True:
            print()
            book_id_delet = input("Enter Book id to delete:   ")
            cursor.execute("SELECT title, price , quantity FROM book WHERE book_id = %s", (book_id_delet,))
            data = cursor.fetchone()
            if data is None:
                print()
                print(colored("Wrong ID Try again","red"))
            else:
                delet = "DELETE FROM book WHERE book_id = %s"
                delete_val = (book_id_delet,)
                cursor.execute(delet, delete_val)
                connection.commit()
                print(colored("------------------Book Removed Successfully------------------","green"))
                break


    def read_price(self):
        flag = False
        while not flag:
            price = input("please enter the price book:   ")
            try:
                price = int(price)
                if price <= 0:
                    print(colored("!!!!!","red"))
                    print(colored("Price cannot be negative or 0","red"))
                    print(colored("!!!!!","red"))
                else:
                    return price
                    flag = True
            except:
                print(colored("Price can be numbers ONLY","red"))




    def readQuant(self):
        flag = False
        while not flag:
            quantity = input("please enter the number of books:   ")
            try:
                quantity = int(quantity)
                if quantity <= 0:
                    print(colored("!!!!!", "red"))
                    print(colored("Quantity cannot be negative or 0","red"))
                    print(colored("!!!!!","red"))
                else:
                    return quantity
                    flag = True
            except ValueError:
                print(colored("Quantity is numbers ONLY","red"))




    def addBook(self):
        print("--------------------- Add New Book Information ---------------------")
        name = input("please enter the name of book:   ")
        price = self.read_price()
        quantity = self.readQuant()
        status = input("please enter the status of book:   ")
        insert = "INSERT INTO book(title,price,quantity,status) VALUES (%s,%s,%s,%s)"
        valuse = (name, price, quantity, status)
        cursor.execute(insert, valuse)
        connection.commit()
        print()
        print(colored("------------------Book Details added successfully--------------------","green"))


    def checkID(self):
        flag = False
        while not flag:
            update = input("Enter Book id:   ")
            try:
                update = int(update)
                if update <= 0:
                    print(colored("!!!!!", "red"))
                    print(colored("ID cannot be negative or 0","red"))
                    print(colored("!!!!!","red"))
                else:
                    return update
                    flag = True
            except ValueError:
                print(colored("ID is numbers ONLY","red"))


    def checkExistID(self,update):

        flag = False
        while not flag:
            cursor.execute("SELECT * FROM book WHERE book_id = %s", (update,))
            data = cursor.fetchall()
            if data is not None:
                return update
                flag = True
            else:
                print(colored("!!!!!", "red"))
                print(colored("This ID is not Exist ,", "red"))
                print(colored("!!!!!", "red"))
                self.checkID()





    def updateBook(self):
        c = commonFunc()
        c.print_books()
        print()
        while True:
            update = self.checkID()
            self.checkExistID(update)
            print()
            choice = input("what information of book you want to update? \npress:\n 1. to change book id \n"
                           " 2. to change book name \n 3. to change book price \n 4. to change quantity of book "
                           "\n 5. to change status of book \nEnter Your Choice:   ")
            if (choice == '1'):
                while True:
                    flag = False
                    while not flag:
                        new_id = input("Enter new book id:")
                        try:
                            new_id = int(new_id)
                            if new_id <= 0:
                                print(colored("!!!!!", "red"))
                                print(colored("ID cannot be negative or 0", "red"))
                                print(colored("!!!!!", "red"))
                            else:
                                flag = True
                        except ValueError:
                            print(colored("ID is numbers ONLY", "red"))
                    cursor.execute("SELECT * FROM book WHERE book_id = %s", (new_id,))
                    data = cursor.fetchone()
                    if data is not None:
                        print()
                        print(colored("WRONG: This ID is Already exists!!","red"))
                    else:
                        update_id = "UPDATE book SET book_id =%s WHERE book_id =%s"
                        val_id = (new_id, update)
                        cursor.execute(update_id, val_id)
                        connection.commit()
                        print()
                        print(colored("------------------Book Details Updated Successfully------------------","green"))
                        break
                break
            elif (choice == '2'):
                print()
                new_name = input("Enter new book name:   ")
                update_name = "UPDATE book SET title=%s WHERE book_id =%s"
                val_name = (new_name, update)
                cursor.execute(update_name, val_name)
                connection.commit()
                print()
                print(colored("------------------Book Details Updated Successfully------------------","green"))
                break

            elif (choice == '3'):
                print()
                new_price = self.read_price()
                update_price = "UPDATE book SET price =%s WHERE book_id =%s"
                val_price = (new_price, update)
                cursor.execute(update_price, val_price)
                connection.commit()
                print()
                print(colored("------------------Book Details Updated Successfully------------------","green"))
                break

            elif (choice == '4'):
                print()
                new_quantity = self.readQuant()
                update_quantity = "UPDATE book SET quantity=%s WHERE book_id =%s"
                val_quantity = (new_quantity, update)
                cursor.execute(update_quantity, val_quantity)
                connection.commit()
                print()
                print(colored("------------------Book Details Updated Successfully------------------","green"))
                break

            elif (choice == '5'):
                print()
                new_status = input("Enter new book status:   ")
                update_status = "UPDATE book SET status=%s WHERE book_id =%s"
                val_status = (new_status, update)
                cursor.execute(update_status, val_status)
                connection.commit()
                print()
                print(colored("------------------Book Details Updated Successfully------------------","green"))
                break

            else:
                print()
                print(colored("Please Choose only from the above menu !!","red"))




    def comments(self):
        print()
        cursor.execute("SELECT user_name, cooment FROM comment")
        myresult = cursor.fetchall()
        print(tabulate(myresult, headers=['user name', 'comment'], tablefmt='fancy_grid'))
        print()


#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------- STUDENT FUNCTIONS ----------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#

class buyer:





    def printBill(self,list):
        if list is not None:
            table = PrettyTable(['Book title', 'Quantity', 'Price'])
            total = 0

            for record in list:
                table.add_row([record[0], record[1], record[2]])
                total += record[2]

            table.add_row(['TOTAL', '', total])
            print(table)
            print('\nThanks for Choosing BkUni :)')
            print('Your total bill amount is ', total, '/-')
            print()



    def printBrrow(self,list):

        if list is not None:
            table = PrettyTable(['Book title', 'Quantity'])
            total = 0

            for record in list:
                table.add_row([record[0], record[1]])

            print(table)
            print('\nThanks for Choosing BkUni :)')
            print('Your total bill amount is ', total, '/-')
            print()



    def buy_book(self):
        shoppingCart = []
        flag = False
        while not flag:
            c = commonFunc()
            c.print_books()
            while True:
                try:
                    book_ID = int(input("Enter Book ID you want to buy:   "))
                    numOfbooks = int(input("How many copy you want?   "))
                    if numOfbooks <= 0:
                        print(colored("!!!!!!!","red"))
                        print(colored("Quantity Can not be negative or 0","red"))
                        print(colored("!!!!!!!","red"))
                    else:
                        break
                except ValueError:
                    print(colored("ID And Quantity can only be a numbers!","red"))

            cursor.execute("SELECT title, price , quantity FROM book WHERE book_id = %s", (book_ID,))
            data = cursor.fetchone()
            if data is None:
                print(colored("Wrong ID please try again","red"))
            else:
                cursor.execute("SELECT quantity FROM book WHERE book_id = %s", (book_ID,))
                row = cursor.fetchone()
                quantity = row[0]
                if quantity <= 0:
                    print(colored("Sorry the book out of stock..","red"))
                else:
                    list = []
                    cursor.execute("SELECT title, price FROM book WHERE book_id = %s", (book_ID,))
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
                    self.printBill(shoppingCart)
                    print()
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
                        print(colored("Please Enter an option","red"))
                    else:
                        print(colored("unknown Option","red"))




    def borrow_book(self):
        shoppingCart = []
        flag = False
        while not flag:
            c = commonFunc()
            c.print_books()
            while True:
                try:
                    book_ID = int(input("Enter Book ID you want to borrow:   "))
                    numOfbooks = int(input("How many copy you want?   "))
                    if numOfbooks <= 0:
                        print(colored("!!!!!!!","red"))
                        print(colored("Quantity Can not be negative or 0","red"))
                        print(colored("!!!!!!!","red"))
                    else:
                        break
                except ValueError:
                    print(colored("ID And Quaninty can only be a numbers!","red"))

            cursor.execute("SELECT * FROM book WHERE book_id = %s", (book_ID,))
            data = cursor.fetchone()
            if data is None:
                print(colored("Wrong ID please try again","red"))
            else:
                cursor.execute("SELECT quantity FROM book WHERE book_id = %s", (book_ID,))
                row = cursor.fetchone()
                quantity = row[0]
                if quantity <= 0:
                    print(colored("Sorry the book out of stock..","red"))
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
                    self.printBrrow(shoppingCart)
                conti = '0'
                while conti != '2':
                    conti = input("Contuneiu? \n 1. yes \n 2.no \n")
                    if conti == '1':
                        break
                    elif conti == '2':
                        print("--------------------- You Can Visit in the nearest branch us to pick up the Book --------------------")
                        flag = True
                    elif conti == None or conti == '':
                        print(colored("Please Enter an option","red"))
                    else:
                        print(colored("unkown Option","red"))





    def user_comment(self):
        print()
        print("*************************************************************")
        print("Cause here in BkUni we care about our customer, We design this option \nto help you share your opinion and thoughts")
        print("*************************************************************")
        print()
        name = input("Please Provide You Name:   ")
        comment = input("Enter your comment:   ")
        insert = "INSERT INTO comment(user_name,cooment) VALUES (%s,%s)"
        valuse = (name, comment)
        cursor.execute(insert, valuse)
        connection.commit()
        print("------------------ Your comment is well received, Thank You --------------------")



    def searchBook(self):
        while True:
            user_input = input("Enter a search key word:   ")
            cursor.execute("SELECT title,quantity,price,status FROM book WHERE title LIKE %s",("%" + user_input + "%",))
            result = cursor.fetchall()
            if len(result) > 0:
                print("Results Found: ", len(result))
                print(tabulate(result, headers=['title', 'quantity','price','status'], tablefmt='pretty'))
                break
            else:
                print(colored("No Result Found","red"))

