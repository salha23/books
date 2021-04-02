import sys
import mysql.connector as mysql
connection=mysql.connect(
 host="localhost",
 user="root",
 password="safa1234",
 database="BKUni",
 auth_plugin='mysql_native_password'
)

#class BKUni:
cursor =connection.cursor()
cursor.execute("SHOW DATABASES")

for x in cursor:
     print(x)

print("---------------------Welcome to Books store--------------------")
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

               id = input("please enter the id book :")
               name = input("please enter the name of book:")
               price = input("please enter the price book:")
               quantity = input("please enter the number of books:")
               status=input("please enter the status of book:")

               insert="INSERT INTO book(book_id,title,price,quantity,status) VALUES (%s,%s,%s,%s,%s)"
               valuse=(id,name, price,quantity,status)
               cursor.execute(insert,valuse)
               connection.commit()
               print("------------------Book Details added successfully--------------------")

           elif admin == 2:
               book_id_delet = input("Enter Book id to delete: ")
               delet="DELETE FROM book WHERE book_id = %s"
               delete_val=(book_id_delet, )
               cursor.execute(delet,delete_val)
               connection.commit()
               print("------------------book removed successfully------------------")


           elif admin == 3:
               update=int(input("Enter Book id to update:"))
               choice=int(input("what information of book you want to update? \n press:\n 1 to change book id \n 2 to change book name \n 3 to change book price \n 4 to change quantity of book \n"))
               if(choice==1):
                  new_id=int(input("Enter new book id:"))
                  update_id="UPDATE book SET book_id =%s WHERE book_id =%s"
                  val_id=(new_id,update)
                  cursor.execute(update_id,val_id)
                  connection.commit()
                  print("------------------book updated successfully------------------")

               if(choice==2):
                  new_name=int(input("Enter new book name:"))
                  update_name="UPDATE book SET book_title=%s WHERE book_id =%s"
                  val_name=(new_name,update)
                  cursor.execute(update_name,val_name)
                  connection.commit()
                  print("------------------book updated successfully------------------")

               if(choice==3):
                  new_price=int(input("Enter new book price:"))
                  update_price="UPDATE book SET price =%s WHERE book_id =%s"
                  val_price=(new_price,update)
                  cursor.execute(update_price,val_price)
                  connection.commit()
                  print("------------------book updated successfully------------------")

               if(choice==4):
                 new_quantity=int(input("Enter new book quantity:"))
                 update_quantity="UPDATE book SET quantity=%s WHERE book_id =%s"
                 val_quantity=(new_quantity,update)
                 cursor.execute(update_quantity,val_quantity)
                 connection.commit()
                 print("------------------book updated successfully------------------")

               elif(choice==5):
                   new_status=int(input("Enter new book status:"))
                   update_status="UPDATE book SET status=%s WHERE book_id =%s"
                   val_status=(new_status,update)
                   cursor.execute(update_status,val_status)
                   connection.commit()
                   print("------------------book updated successfully------------------")



           elif admin == 4:
               book_id=int(input("Enter the book ID that you want to see the status:"))
               sql="select status from book where book_id=%s"
               val=(book_id,)
               cursor.execute(sql,val)
               print("----------",cursor.fetchone())

           elif admin == 5:
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

