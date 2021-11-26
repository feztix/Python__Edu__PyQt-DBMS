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
from PyQt5 import QtWidgets, QtGui, QtCore
from BinaryTreeWindow import Ui_MainWindow, myWindow
import random
import copy
import numpy
import collections
import json

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.root = 1

    # def preOrder(root):
    #     if root:
    #         size = 50
    #         if root == 1:
    #             x = 1 * 0.8 * pow(2, 1) * size
    #             y = 0
    #         scene.addEllipse(x, y, size, size)
    #         text = scene.addText(str(node.key))
    #         text.setPos(x + (10 * scale), y + (10 * scale))
    #         print(root.val)
    #         if root.left:
    #             print("Draw Left Here")
    #             TreeNode.preOrder(root.left)
    #         if root.right:
    #             print("Draw Right Here")
    #             TreeNode.preOrder(root.right)


class Codec:

    def serialize(self, root):
        if not root:
            return 'null'
        nodes = collections.deque([root])
        maps = collections.deque([{'v': root.val}])
        tree = maps[0]
        while nodes:
            frontNode = nodes.popleft()
            frontMap = maps.popleft()
            if frontNode.left:
                frontMap['l'] = {'v': frontNode.left.val}
                nodes.append(frontNode.left)
                maps.append(frontMap['l'])
            if frontNode.right:
                frontMap['r'] = {'v': frontNode.right.val}
                nodes.append(frontNode.right)
                maps.append(frontMap['r'])
        return json.dumps(tree)

    def deserialize(self, data):
        tree = json.loads(data)
        if not tree:
            return None
        root = TreeNode(tree['v'])
        maps = collections.deque([tree])
        nodes = collections.deque([root])
        while nodes:
            frontNode = nodes.popleft()
            frontMap = maps.popleft()
            left, right = frontMap.get('l'), frontMap.get('r')
            if left:
                frontNode.left = TreeNode(left['v'])
                maps.append(left)
                nodes.append(frontNode.left)
            if right:
                frontNode.right = TreeNode(right['v'])
                maps.append(right)
                nodes.append(frontNode.right)
        return root


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

    def import_to_db(self, filename):
        # Диалог выходит за область видимости
        # TODO: возвращать ссылку на диалог
        # ----------------------------------
        global dialog1

        dialog1 = myWindow()
        dialog1.show()


class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.root = 1

class BinaryTree1:

    def __init__(self, root=None):
        if root is None:
            self.root = None
            self.count = 0
            self.lvlCount = 0
            self.maxLCount = 0
        else:
            self.root = root
            self.count = 1
            self.lvlCount = 0
            self.maxLCount = 0

    # def AddNode(self, keyP: int, nodeP=None, currLvl=0):
    #     if nodeP is None:
    #         nodeP = self.root
    #     if self.count == 0:
    #         self.root = Node(keyP)
    #     elif keyP < nodeP.key:
    #         currLvl += 1
    #         if currLvl > self.lvlCount:
    #             self.lvlCount = currLvl
    #         if nodeP.leftCh is None:
    #             nodeP.leftCh = Node(keyP, nodeP)
    #         else:
    #             self.count -= 1
    #             self.AddNode(keyP, nodeP.leftCh, currLvl)
    #     else:
    #         currLvl += 1
    #         if currLvl > self.lvlCount:
    #             self.lvlCount = currLvl
    #         if nodeP.rightCh is None:
    #             nodeP.rightCh = Node(keyP, nodeP)
    #         else:
    #             self.count -= 1
    #             self.AddNode(keyP, nodeP.rightCh, currLvl)
    #     self.count += 1

    def GenerateTree(self):
        # for i in range(10):
        #     self.AddNode(random.randint(0, 1245))

        codec = Codec()

        data = '{"v": 1, "r": {"v": 2, "l": {"v": 3}}, "l": {"v":5}}'
        des = codec.deserialize(data)
        # здесь я получаю дерево
        print(des.right.left.val)

        ser = codec.serialize(des)
        print(ser)
        return des

    # def SearchNode(self, keyP: int, nodeP):
    #     if nodeP is None:
    #         return None
    #     if nodeP.key == keyP:
    #         return nodeP
    #     elif keyP < nodeP.key:
    #         if nodeP.leftCh is None:
    #             return None
    #         else:
    #             return self.SearchNode(keyP, nodeP.leftCh)
    #     else:
    #         if nodeP.rightCh is None:
    #             return None
    #         else:
    #             return self.SearchNode(keyP, nodeP.rightCh)

    # def DeleteNode(self, keyP):
    #     self.count-=1
    #     searchedElem = self.SearchNode(keyP, self.root)
    #     if searchedElem is None:
    #         return
    #     else:
    #         if searchedElem.leftCh is None and searchedElem.rightCh is None:
    #             if searchedElem == self.root:
    #                 self.root = None
    #             else:
    #                 if searchedElem.parent.leftCh == searchedElem:
    #                     searchedElem.parent.leftCh = None
    #                 else:
    #                     searchedElem.parent.rightCh = None
    #         else:
    #             if searchedElem.leftCh is None:
    #                 searchedElem.rightCh.parent = searchedElem.parent
    #                 if searchedElem == self.root:
    #                     self.root = searchedElem.rightCh
    #                 else:
    #                     if searchedElem.parent.leftCh == searchedElem:
    #                         searchedElem.parent.leftCh = searchedElem.rightCh
    #                     else:
    #                         searchedElem.parent.rightCh = searchedElem.rightCh
    #             else:
    #                 if searchedElem.rightCh is None:
    #                     searchedElem.leftCh.parent = searchedElem.parent
    #                     if searchedElem == self.root:
    #                         self.root = searchedElem.leftCh
    #                     else:
    #                         if searchedElem.parent.leftCh == searchedElem:
    #                             searchedElem.parent.leftCh = searchedElem.leftCh
    #                         else:
    #                             searchedElem.parent.rightCh = searchedElem.leftCh
    #                 else:
    #                     self.count+=1
    #                     nodeT = searchedElem.rightCh
    #                     while nodeT.leftCh is not None:
    #                         nodeT = nodeT.leftCh
    #                     keyT = nodeT.key
    #                     self.DeleteNode(nodeT.key)
    #                     searchedElem.key = keyT
    #     self.CountLvl()

    # def CountLvl(self, nodeP=None, lCount=0):
    #     if nodeP is None:
    #         if self.root is None:
    #             return
    #         else:
    #             self.maxLCount = 0
    #             nodeP = self.root
    #     if nodeP.leftCh is not None:
    #         lCount +=1
    #         if lCount>self.maxLCount:
    #             self.maxLCount = lCount
    #         self.CountLvl(nodeP.leftCh, lCount)
    #         lCount -= 1
    #     if nodeP.rightCh is not None:
    #         lCount += 1
    #         if lCount>self.maxLCount:
    #             self.maxLCount = lCount
    #         self.CountLvl(nodeP.rightCh, lCount)
    #         lCount -= 1
    #     self.lvlCount = self.maxLCount
    #
    # def Clear(self):
    #     if self.root is not None:
    #         self.DeleteNode(self.root.key)
    #         self.Clear()


    def paint(self, scene, scale, des , x=0, y=0, currLvl=0, currNum=1):
        ###########################################3

        if des is None:
            return
        size = 50
        if des.val == des.root:
            x = currNum*scale*pow(2, self.lvlCount) * size
            y = 0
        scene.addEllipse(x, y, size, size)
        text = scene.addText(str(des.val))
        text.setPos(x+(10*scale), y+(10*scale))
        nextNumL = currNum * 2 - 1
        nextNumR = currNum * 2
        nextXL = x-pow(2, self.lvlCount-currLvl)*size*0.50
        nextXR = x+pow(2, self.lvlCount-currLvl)*size*0.50
        nextY = y + 150
        if des.left is not None:
            scene.addLine(x + size*0.5, y + size, nextXL + size*0.5, nextY)
            self.paint(scene, scale, des.left, nextXL, nextY, currLvl + 1, currNum * 2 - 1)
        if des.right is not None:
            scene.addLine(x + size*0.5, y + size, nextXR + size*0.5, nextY)
            self.paint(scene, scale, des.right, nextXR, nextY, currLvl + 1, currNum * 2)

    def print(self, lvl, node=None,  currLvl=0):
        if node is None:
            node = self.root
        if currLvl == lvl:
            print(node.key, end=" ")
        else:
            if node.leftCh is not None:
                self.print(lvl, node.leftCh, currLvl+1)
            if node.rightCh is not None:
                self.print(lvl, node.rightCh, currLvl+1)