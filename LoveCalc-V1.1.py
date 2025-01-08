from PySide6.QtWidgets import (  
    QApplication, QMainWindow, QVBoxLayout, QLineEdit, QPushButton, QWidget, QGridLayout  
)  
from PySide6.QtCore import Qt  


class Calculadora(QMainWindow):  
    def __init__(self):  
        super().__init__()  
        self.setWindowTitle("LOVECALC") 
        self.setGeometry(1600, 100, 230, 290)
        self.setFixedSize(230, 290)
        self.setWindowOpacity(0.99)

        self.layout =  QGridLayout()
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        central_widget.setLayout(self.layout)
  
        self.current = ''  
        self.op = ''  
        self.total = 0  
        self.operation_verification = False  
        
        self.central_widget = QWidget()  
        self.setCentralWidget(self.central_widget)  
        self.layout = QVBoxLayout(self.central_widget)  

        # Input / Display  
        self.display = QLineEdit()  
        self.display.setAlignment(Qt.AlignRight)  
        self.display.setReadOnly(True)  
        self.display.setStyleSheet("font-size: 23px; background-color: #9333FF; color: white;")  
        self.layout.addWidget(self.display)  

        # Configuración de los botones  
        self.grid_layout = QGridLayout()  
        self.layout.addLayout(self.grid_layout)  

        buttons = [  
            "7", "8", "9", "/",  
            "4", "5", "6", "*",  
            "1", "2", "3", "-",  
            "C", "0", ".", "+",  
            "=", "HI"  
        ]  

        row, col = 0, 0  
        for button in buttons:  
            self.add_button(button, row, col)  
            col += 1  
            if col > 3:  
                col = 0  
                row += 1  

    def add_button(self, text, row, col):  
        button = QPushButton(text)  
        button.setStyleSheet("font-size: 18px; padding: 10px;")  
        button.clicked.connect(lambda: self.handle_click(text))  
        self.grid_layout.addWidget(button, row, col)  

    def handle_click(self, key):  
        if key == "C":  
            self.clear_display()  
        elif key == "=":  
            self.calculate()  
        elif key == "HI":  
            self.send_message()  
        else:  
            self.click(key)  

    def click(self, key):  
        if self.operation_verification:  
            self.operation_verification = False  

        if key in '0123456789' or key == '.':  
            self.current += key  
            self.display.setText(self.display.text() + key)  
        else:  
            if self.current:  
                if not self.op:  
                    self.total = float(self.current)  
            self.current = ''  
            self.op = key  
            self.display.setText(self.display.text() + key)  

    def calculate(self):  
        if self.current and self.op:  
            try:  
                if self.op == '/':  
                    self.total /= float(self.current)  
                elif self.op == '*':  
                    self.total *= float(self.current)  
                elif self.op == '+':  
                    self.total += float(self.current)  
                elif self.op == '-':  
                    self.total -= float(self.current)  
            except ZeroDivisionError:  
                self.display.setText("Error")  
                return  

        self.display.setText(str(round(self.total, 3)))  
        self.operation_verification = True  
        self.current = ''  
        self.op = ''  

    def clear_display(self):  
        self.display.clear()  
        self.current = ''  
        self.op = ''  
        self.total = 0  
        self.operation_verification = False  

    def send_message(self):  
        self.display.setText("I LOVE U")  


if __name__ == "__main__":  
    app = QApplication([])  
    window = Calculadora()  
    window.show()  
    app.exec()
