from PyQt5.QtPrintSupport import *
import sys, sqlite3, time

from PyQt5.QtWidgets import QMainWindow
import BinaryTree
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import pandas


class myWindow(QMainWindow):

    def __init__(self, unhandled_data_from_json):

        super(myWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # генерация дерева
        self.tree = BinaryTree.BinaryTree()
        # присваивание необработанных данных из json дереву
        self.unhandled_data_from_json = unhandled_data_from_json

        self.scene = QtWidgets.QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)
        self.scale = 0.8
        self.ui.graphicsView.scale(self.scale, self.scale)
        self.ui.pushButton_5.clicked.connect(self.Generate)

    def Generate(self):
        self.scene.clear()
        self.tree.GenerateTree()
        self.PaintT()

    def PaintT(self):
        codec = BinaryTree.Codec()

        data = self.unhandled_data_from_json
        des = codec.deserialize(data)
        self.tree.paint(self.scene, self.scale, des)


# UI дизайн
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 10, 600, 661))
        self.graphicsView.setObjectName("graphicsView")

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(615, 20, 325, 130))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 5, 325, 130))
        self.label.setObjectName("label")

        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(615, 160, 325, 110))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 325, 110))
        self.label_2.setObjectName("label_2")

        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(615, 280, 325, 40))
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_3 = QtWidgets.QLabel(self.groupBox_5)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 325, 40))
        self.label_3.setObjectName("label_3")

        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setGeometry(QtCore.QRect(615, 340, 325, 65))
        self.groupBox_6.setObjectName("groupBox_6")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_5.setGeometry(QtCore.QRect(120, 30, 121, 23))
        self.pushButton_5.setObjectName("pushButton_5")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1080, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.groupBox.setTitle(_translate("MainWindow", "Описание визуализации"))
        self.label.setText(_translate("MainWindow", """Отображение на графике структуры
данных в виде бинарного дерева и связи между
этими данными. Данные о структуре данных
хранятся в формате json, которые подаются
на вход"""))

        self.groupBox_2.setTitle(_translate("MainWindow", "Описание входных данных"))
        self.label_2.setText(_translate("MainWindow", """Входные данные представляют
собой одностроковый json файл бинарного
дерева, где
-- v - корневой элемент
-- r - правый элемент корня
-- l - левый элемент корня"""))

        self.groupBox_5.setTitle(_translate("MainWindow", "Пример входных данных"))
        self.label_3.setText(_translate("MainWindow", '{"v": 1, "r": {"v": 2, "l": {"v": 3}}, "l": {"v":5}}'))

        self.groupBox_6.setTitle(_translate("MainWindow", "Сгенерировать дерево"))
        self.pushButton_5.setText(_translate("MainWindow", "Начать"))
