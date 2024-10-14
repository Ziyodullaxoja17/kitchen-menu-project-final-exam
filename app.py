from os import system
from PyQt5.QtWidgets import QApplication ,QMessageBox  , QListWidgetItem
from database import Database
from first_window import First_Window 
from add_dish_window import Add_New_Dish_Window 
from show_dishes_window import Main_Window
from edit_dish_window import Edit_Window 


class App:

     def __init__(self) -> None:

          self.first_page=First_Window()
          self.add_dish_page=Add_New_Dish_Window()
          self.dishes_page=Main_Window()
          self.edit_page=Edit_Window()
          

          self.databs=Database()


          self.first_page.show()

          self.first_page.add_dish_btn.clicked.connect(self.show_add_page)
          self.first_page.find_dishes_btn.clicked.connect(self.show_dishes_page_func)

     def show_add_page(self):
          self.add_dish_page.show()
          self.first_page.close()

          self.add_dish_page.save_new_dish_btn.clicked.connect(self.save_new_dish_func)
          self.add_dish_page.back_first_page_btn.clicked.connect(self.back_to_first_page_from_add)
     

     def save_new_dish_func(self):
          name=self.add_dish_page.name_dish_input.text()
          ingred=self.add_dish_page.ingredient_input.toPlainText()
          inctruct=self.add_dish_page.ingredient_input.toPlainText()
          try :
               self.databs.Insert(name , ingred , inctruct)
               self.msgbox=QMessageBox(self.add_dish_page)
               self.msgbox.setText("Ma'lumot saqlandi ")
               self.msgbox.exec()
               self.add_dish_page.name_dish_input.clear()
               self.add_dish_page.ingredient_input.clear()
               self.add_dish_page.instuction_input.clear()
               
          except :
               print("Error")
          
     
     def back_to_first_page_from_add(self):
          self.first_page.show()
          self.add_dish_page.close()

          

     def show_dishes_page_func(self):
          self.dishes_page.show()
          self.first_page.close()

          

          data=self.databs.Get_All_Dishes()
          print(data)


          for i in data:
               text=f' {i[0]}   name : {i[1]}  \n ingredient : {i[2]} \ninctruntions : {i[3]}\n'
               item=QListWidgetItem()
               item.setText(text)
               
               self.dishes_page.list_dishes.addItem(item)

          
          self.dishes_page.back_first_btn.clicked.connect(self.back_to_first_page_from_main)
          self.dishes_page.edit_dish_btn.clicked.connect(self.edit_page_show_func)
     


     def edit_page_show_func(self):

          self.edit_page.show()
          self.dishes_page.close()

          self.edit_page.edit_btn.clicked.connect(self.edit_func)
          self.edit_page.delete_btn.clicked.connect(self.delete_func)

     
     def delete_func(self):
          name=self.edit_page.last_name_input.text()
          self.databs.Delete(name)
     
     def edit_func(self):
          pass
     
     

     def back_to_first_page_from_main(self):
          self.first_page.show()
          self.dishes_page.close()






     



app=QApplication([])
main=App()

app.exec()