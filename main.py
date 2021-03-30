import sys

import MySQLdb as mysql

def startCon(self):
    con = mysql.connect(
        host="localhost",
        port="3306",
        user="root",
        password="1234",
        database="BKUni"
    )
    return con



Books = []
class BKUni:
 def __init__(self, id, B_name,quantity , B_price, major, level):
    self.id = id
    self.B_name = B_name
    self.B_price = B_price
    self.major = major
    self.level = level
    self.quantity = quantity

 def setLevel(self, level):
     self.level = level

 def getLevel(self):
     return self.level

 def setMajor(self, major):
     self.major = major

 def getMajor(self):
     return self.major

 def setId(self, id):
     self.id = id

 def setBname(self, B_name):
     self.B_name = B_name

 def setBpice(self, B_price):
     self.B_price = B_price

 def getId(self):
     return self.id

 def getBname(self):
     return self.B_name

 def getBprice(self):
     return self.B_price

 def display(self):
     print('Books ID:', self.id, '\t Books name :', self.B_name, '\t Price', self.B_price, '\t major', self.major, '\t Level', self.level)


print("Welcome to Books store")
SE = int(input(" 1)Admin \n 2)Student \n enter your select :"))

while True:
    if SE == 1:
        admin = 0
        while admin != 6:
         print("1.Add new Book")
         print("2.Delete book")
         print("3.Modify books ")
         print("4.View books rating")
         print("5.View the borrowing status ")
         print("6.Exit")
         admin = int(input("enter choice : "))
         if admin == 1:

             id = input("please enter the id book :")
             name = input("please enter the name of book")
             quantity = input("please enter the number of books")
             price = input("please enter the price book")
             major = input("please enter your major ")
             level = input("please enter your level")

             book = BKUni(id, name, quantity, price, major, level)
             Books.append(book)
             print("Book Details added successfully .")

         elif admin == 2:
             for x in range(len(Books)):
                 print(Books[x].display())
             dele = input("Enter Book name to delete: ")
             if (dele not in Books):
                 ans = input("Entered book does not exists,do you want to retry ? (y/n): ")
                 if (ans == "y"):
                     #del1 = input("Enter book name to delete: ")
                     Books.remove(dele)
                     print("book removed successfully.")
                     print(Books)
                 else:
                     print("book deletion aborted.")
             else:
                 Books.remove(dele)
                 print("city removed successfully.")
                 print(Books)

         elif admin == 4:
             for x in range(len(Books)):
                 print(Books[x].getMajor())
                 print(Books[x].display())

         elif admin == 5:
             for x in range(len(Books)):
                 print(Books[x].display())

         elif admin == 6:
             break
        SE = int(input(" 1)Admin \n 2)Student \n enter your select :"))


    elif SE == 2:
        print("Welcome student ")
        st = 0
        while st != 6:
            print("1.View the available books in BKUni")
            print("2.Buy a books ")
            print("3.Borrow a books ")
            print("4.Search for a specific books")
            print("5.Rating a bought or borrowed books")
            print("6.Exit")
            st = int(input("enter choice : "))

        break
    else:
        print("Unknown Option Selected! pleas try again ")
        SE = int(input(" 1)Admin \n 2)Student \n enter your select :"))

sys.exit()

