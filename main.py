import sys
import sqlite3
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class CoffeeApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.pushButton.clicked.connect(self.load_data)
        self.load_data()

    def load_data(self):
        con = sqlite3.connect("coffee.sqlite")
        cursor = con.cursor()
        query = "SELECT id, name, degree_of_roasting, ground_or_grains, description, price, volume FROM coffee"
        cursor.execute(query)
        rows = cursor.fetchall()

        self.tableWidget.setRowCount(len(rows))
        self.tableWidget.setColumnCount(len(rows[0]))
        self.tableWidget.setHorizontalHeaderLabels([
            "ID", "Название сорта", "Степень обжарки", "Молотый/в зёрнах",
            "Описание вкуса", "Цена(₽)", "Объём упаковки"
        ])

        for row_number, row_items in enumerate(rows):
            for column_number, value in enumerate(row_items):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(value)))
        con.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    coffee = CoffeeApp()
    coffee.show()
    sys.exit(app.exec())