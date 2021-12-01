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
            self.export_from_json(fileName)

    def export_from_json(self, filename):
        global dialog1

        file = open(filename, 'r')
        unhandled_data_from_json = file.read()

        dialog1 = myWindow(unhandled_data_from_json)
        dialog1.show()


class BinaryTree:

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

    def GenerateTree(self):
        codec = Codec()

        # data = '{"r": {"l": {"l": {"v": 9}, "v": 2}, "v": 7}, "l": {"l": {"l": {"v": -1}, "v": 3}, "v": 4}, "v": 5}'
        data = '{"v": 1, "r": {"v": 2, "l": {"v": 3}}, "l": {"v":5}}'
        des = codec.deserialize(data)

        # #### serialize for debug
        # ser = codec.serialize(des)
        # print(ser)
        # ####

        return des

    def paint(self, scene, scale, des, x=0, y=0, currLvl=0, currNum=1):
        if des is None:
            return
        size = 50
        if des.val == des.root:
            x = currNum * scale * pow(2, self.lvlCount) * size
            y = 0
        scene.addEllipse(x, y, size, size)
        text = scene.addText(str(des.val))
        text.setPos(x + (10 * scale), y + (10 * scale))
        nextNumL = currNum * 2 - 1
        nextNumR = currNum * 2
        nextXL = x - pow(2, self.lvlCount - currLvl) * size * 3
        nextXR = x + pow(2, self.lvlCount - currLvl) * size * 3
        nextY = y + 150
        if des.left is not None:
            scene.addLine(x + size * 0.5, y + size, nextXL + size * 0.5, nextY)
            self.paint(scene, scale, des.left, nextXL, nextY, currLvl + 1, currNum * 2 - 1)
        if des.right is not None:
            scene.addLine(x + size * 0.5, y + size, nextXR + size * 0.5, nextY)
            self.paint(scene, scale, des.right, nextXR, nextY, currLvl + 1, currNum * 2)
