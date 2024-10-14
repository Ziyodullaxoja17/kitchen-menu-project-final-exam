from PyQt5.QtWidgets import QLabel , QLineEdit , QTextEdit , QPushButton , QWidget 




class Label(QLabel):
     def __init__(self , oyna : QWidget , text , y):
          super().__init__(oyna)

          self.setText(text)
          self.move((oyna.width()-self.width())//2-30 , y)
          self.setStyleSheet("""font-size : 40px;""")



class Button(QPushButton):
     def __init__(self , oyna : QWidget, text , y ):
          super().__init__(oyna)
          self.setText(text)
          self.resize(100 , 50)
          self.move(190 , y)
          self.setStyleSheet("""
          font-size : 30px
""")

class Input(QLineEdit):
     def __init__(self , oyna , text , y ):
          super().__init__(oyna)
          self.move(65 , y)
          self.resize(350 , 60)
          self.setPlaceholderText(text)
          self.setStyleSheet("""
          font-size : 22px;
""")


class Input_Text(QTextEdit):
     def __init__(self , oyna , text , y ):
          super().__init__(oyna)
          self.setPlaceholderText(text)
          self.move(65 , y)
          self.resize(350 , 120)
          self.setStyleSheet("""
          font-size : 22px;
""")
