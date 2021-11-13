# TODO перебрать список зависимостей
import csv
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import *
import sys, sqlite3, time
from MainWindow import *
import os
import pandas

class VisualizeBinTreeFromJson(QDialog):
    def __init__(self, *args, **kwargs):
        super(VisualizeBinTreeFromJson, self).__init__(*args, **kwargs)

        self.setWindowTitle("Visualize Binary Tree From Json File")
        self.setFixedWidth(300)
        self.setFixedHeight(100)

        self.open()

    def open(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, 'Open a file', '',
                                           'Text Files (*.json)', options=options)
        if fileName:
            self.import_to_db(fileName)

    # def import_to_db(self, filename):
    #     self.conn = sqlite3.connect("database.db")
    #     self.c = self.conn.cursor()
    #     self.c.execute("DROP TABLE IF EXISTS employee")
    #     self.c.execute("""
    #                 CREATE TABLE IF NOT EXISTS employee(roll INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT,branch TEXT,
    #                 sem TEXT,mobile INTEGER,address TEXT)""")

        # table_name = "employee"
        # orders = pandas.read_csv(filename)  # load to DataFrame
        # orders.to_sql(table_name, self.conn, if_exists='append', index=False)