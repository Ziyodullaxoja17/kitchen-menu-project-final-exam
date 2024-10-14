from PyQt5.QtWidgets import QApplication , QWidget  , QListWidget  , QPushButton
from components import Label  


class Main_Window(QWidget):
     def __init__(self):
          super().__init__()
          self.setWindowTitle("Main Window")
          self.resize(600 , 800 )
          self.welcome_label=Label(self , "Dishes" , 30)
          self.list_dishes=QListWidget(self)
          self.list_dishes.resize(500 , 600)
          self.list_dishes.move(50 , 100)
          self.edit_dish_btn=QPushButton(self)
          self.edit_dish_btn.setText("EDIT")
          self.edit_dish_btn.setStyleSheet("""font-size : 22px""")
          self.edit_dish_btn.resize(100 , 60)
          self.edit_dish_btn.move(300 , 720)
          self.back_first_btn=QPushButton(self)
          self.back_first_btn.setText("BACK")
          self.back_first_btn.resize(100 , 60)
          self.back_first_btn.move(140 , 720)
          self.back_first_btn.setStyleSheet("""font-size : 22px""")

          self.list_dishes.setStyleSheet("""font-size : 22px""")





