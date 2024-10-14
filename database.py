import mysql.connector
from colorama import init , Fore
import mysql.connector.cursor
from os import system
system("cls")



class Database:
     def __init__(self) -> None:
          self.dbase=mysql.connector.connect(
               host= "localhost",
               user='root',
               password='111317'
          )


          self.kursor=self.dbase.cursor()

          self.__Set_UP()
          self.__Create_Table()


     

     def __Set_UP(self):
          self.kursor.execute("CREATE DATABASE IF NOT EXISTS KITCHEN;")
          self.kursor.execute("USE KITCHEN;")

          print(Fore.GREEN + "$ DATABSE YARATILINDI ")
     
     def __Create_Table(self):
          self.kursor.execute("""CREATE TABLE IF NOT EXISTS DISHES (
          RECIPE_ID INT AUTO_INCREMENT PRIMARY KEY,
          NAME VARCHAR(32) UNIQUE,
          INGREDIENTS VARCHAR(128) ,
          INSTRUCTIONS VARCHAR(128));""")
          
          print(Fore.GREEN + "$ TABLE YARATILINDI ")
     

     def Insert(self , name , ingredients , instructions):
          
          self.kursor.execute("""
          INSERT INTO DISHES VALUES(
          NULL , %s , %s , %s);
""",(name , ingredients , instructions))
          
          self.dbase.commit()

          print(Fore.GREEN + "$ MA'LUMOT MUOFAQQIYATLI QO'SHILDI ")


     
     def Get_All_Dishes(self):
          self.kursor.execute("SELECT * FROM DISHES;")
          data=self.kursor.fetchall()
          data=list(data)

          return data
     def Delete(self , name):
          self.kursor.execute("DELETE FROM DISHES WHERE NAME = %s;",(name))

          self.dbase.commit()
          print(Fore.RED + "% MA'LUMOT O'CHIRILDI ")
     
     def Edit(self , name , new_name , ing , inc):
          self.kursor.execute("UPDATE DISHES SET NAME = %s , INGREDIENTS = %s , INSTRUCTIONS = %s   WHERE NAME = %s;"(new_name , ing , inc , name))
          self.dbase.commit()
          print(Fore.GREEN + "$ MALUMOT O'ZGARIRILDI ")
          








database=Database()

