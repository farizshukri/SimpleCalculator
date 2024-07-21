# Simple Calculator using PyQt GUI
# Fariz Shukri
# 07/2024

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Simple Calculator')
        self.setGeometry(200, 200, 300, 400)

        self.init_ui()

    def init_ui(self):
        # Create a vertical layout
        vbox = QVBoxLayout()
        self.setLayout(vbox)

        # Create a line edit widget to display input/output
        self.line_edit = QLineEdit()
        vbox.addWidget(self.line_edit)

        # Create buttons for digits and operations
        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', '=', '+')
        ]

        for row in buttons:
            hbox = QHBoxLayout()
            for label in row:
                button = QPushButton(label)
                button.clicked.connect(self.on_button_click)
                hbox.addWidget(button)
            vbox.addLayout(hbox)

    def on_button_click(self):
        button = self.sender()
        label = button.text()

        if label == '=':
            try:
                result = str(eval(self.line_edit.text()))
                self.line_edit.setText(result)
            except Exception as e:
                self.line_edit.setText("Error")
        else:
            current_text = self.line_edit.text()
            new_text = current_text + label
            self.line_edit.setText(new_text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
