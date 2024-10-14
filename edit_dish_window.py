from PyQt5.QtWidgets import QApplication , QWidget
from components import Input , Label , Input_Text , Button


class Edit_Window(QWidget):
     def __init__(self):
          super().__init__()
          self.resize(480  , 640)


          self.edit_label=Label(self, "   Edit" , 50)

          self.last_name_input=Input(self, "Last Name" , 110)
          self.new_name_input=Input(self , "New Name" ,180 )
          self.new_indgre_input=Input_Text(self , "New Ingredient" , 250)
          self.new_instruc_input=Input_Text(self , "New Instruction" , 400)
          self.delete_btn=Button(self , "DELETE" , 590)
          self.edit_btn=Button(self , "EDIT" , 530)

