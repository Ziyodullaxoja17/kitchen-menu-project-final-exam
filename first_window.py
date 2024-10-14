from PyQt5.QtWidgets import QApplication , QWidget 
from components import Label , Button
from os import system
system("cls")



class First_Window(QWidget):
     def __init__(self):
          super().__init__()

          self.setWindowTitle("Kitchen")
          self.resize(480 , 640)
          self.welcome_label=Label(self , "Welcome !" , 100)


          self.find_dishes_btn=Button(self , "FIND" , 380)
          self.add_dish_btn=Button(self , "ADD" , 300)


     