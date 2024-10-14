from PyQt5.QtWidgets import QWidget 

from components import Label , Input  , Input_Text , Button

class Add_New_Dish_Window(QWidget):
     def __init__(self):
          super().__init__()

          self.setWindowTitle("New Dish")
          self.resize(480 , 640)
          self.new_dish_label=Label(self , "New Dish" , 70)
          self.name_dish_input=Input(self , "Dish Name" , 150)
          self.ingredient_input=Input_Text(self , "Ingredients" , 230)
          self.instuction_input=Input_Text(self , "Instructions" , 370)
          self.save_new_dish_btn=Button(self , "Save" , 500)
          self.back_first_page_btn=Button(self , "Back" , 560)
