from PyQt5.QtPrintSupport import *
import sys, sqlite3, time

from PyQt5.QtWidgets import QMainWindow
import BinaryTree
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import pandas


class myWindow(QMainWindow):

    def __init__(self):
        super(myWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.tree = BinaryTree.BinaryTree1()

        self.scene = QtWidgets.QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)
        self.scale = 0.8
        self.ui.graphicsView.scale(self.scale, self.scale)
        self.ui.pushButton.clicked.connect(self.AddEl)
        self.ui.pushButton_2.clicked.connect(self.DelEl)
        self.ui.pushButton_4.clicked.connect(self.Clear)
        self.ui.pushButton_5.clicked.connect(self.Generate)

    def AddEl(self):
        self.tree.AddNode(int(self.ui.spinBox.text()))
        self.scene.clear()
        self.PaintT()

    def DelEl(self):
        self.tree.DeleteNode(int(self.ui.spinBox_2.text()))
        self.scene.clear()
        self.PaintT()

    def Clear(self):
        self.scene.clear()
        self.tree.Clear()
        self.PaintT()

    def Generate(self):
        self.scene.clear()
        self.tree.GenerateTree()
        self.PaintT()

    def PaintT(self):
        self.ui.label_5.setText(str(self.tree.count))
        self.ui.label_7.setText(str(self.tree.lvlCount))
        self.tree.paint(self.scene, self.scale, self.tree.root)


# UI дизайн
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 10, 801, 661))
        self.graphicsView.setObjectName("graphicsView")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(820, 20, 241, 91))
        self.groupBox.setObjectName("groupBox")
        self.spinBox = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox.setGeometry(QtCore.QRect(140, 30, 71, 21))
        self.spinBox.setMinimum(-10000)
        self.spinBox.setMaximum(10000)
        self.spinBox.setProperty("value", 0)
        self.spinBox.setObjectName("spinBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 121, 21))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(60, 60, 121, 23))
        self.pushButton.setObjectName("pushButton")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(820, 120, 241, 91))
        self.groupBox_2.setObjectName("groupBox_2")
        self.spinBox_2 = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_2.setGeometry(QtCore.QRect(140, 30, 71, 21))
        self.spinBox_2.setMinimum(-10000)
        self.spinBox_2.setMaximum(10000)
        self.spinBox_2.setObjectName("spinBox_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 121, 21))
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 60, 121, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(820, 360, 241, 91))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 61, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setGeometry(QtCore.QRect(80, 20, 47, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_4)
        self.label_6.setGeometry(QtCore.QRect(10, 50, 61, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_4)
        self.label_7.setGeometry(QtCore.QRect(80, 50, 47, 16))
        self.label_7.setObjectName("label_7")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(820, 220, 241, 61))
        self.groupBox_5.setObjectName("groupBox_5")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_4.setGeometry(QtCore.QRect(60, 30, 121, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setGeometry(QtCore.QRect(820, 290, 241, 61))
        self.groupBox_6.setObjectName("groupBox_6")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_5.setGeometry(QtCore.QRect(60, 30, 121, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1080, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        # MainWindow.setMainWindowStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Добавить элемент"))
        self.label.setText(_translate("MainWindow", "Введите значение:"))
        self.pushButton.setText(_translate("MainWindow", "Добавить элемент"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Удалить элемент"))
        self.label_2.setText(_translate("MainWindow", "Введите значение:"))
        self.pushButton_2.setText(_translate("MainWindow", "Удалить элемент"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Количество элементов и высота дерева"))
        self.label_4.setText(_translate("MainWindow", "Элементов:"))
        self.label_5.setText(_translate("MainWindow", "0"))
        self.label_6.setText(_translate("MainWindow", "Высота:"))
        self.label_7.setText(_translate("MainWindow", "0"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Очистить дерево"))
        self.pushButton_4.setText(_translate("MainWindow", "Очистить"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Добавить в дерево 10 элементов"))
        self.pushButton_5.setText(_translate("MainWindow", "Добавить"))
