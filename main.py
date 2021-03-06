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


class InsertDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(InsertDialog, self).__init__(*args, **kwargs)

        self.QBtn = QPushButton()
        self.QBtn.setText("Register")

        self.setWindowTitle("Add Employee")
        self.setFixedWidth(300)
        self.setFixedHeight(250)

        self.QBtn.clicked.connect(self.addemployee)

        layout = QVBoxLayout()

        self.nameinput = QLineEdit()
        self.nameinput.setPlaceholderText("Name")
        layout.addWidget(self.nameinput)

        self.branchinput = QComboBox()
        self.branchinput.addItem("Manager")
        self.branchinput.addItem("Accountant")
        self.branchinput.addItem("CEO Deputy")
        self.branchinput.addItem("CEO")
        self.branchinput.addItem("System Adm.")
        self.branchinput.addItem("Security Adm.")
        layout.addWidget(self.branchinput)

        self.seminput = QComboBox()
        self.seminput.addItem("Non Confidential")
        self.seminput.addItem("Confidential")
        self.seminput.addItem("Secret")
        self.seminput.addItem("Top Secret")
        layout.addWidget(self.seminput)

        self.mobileinput = QLineEdit()
        self.mobileinput.setPlaceholderText("Mobile")
        self.mobileinput.setInputMask('999 999 99 99')
        layout.addWidget(self.mobileinput)

        self.addressinput = QLineEdit()
        self.addressinput.setPlaceholderText("Department")
        layout.addWidget(self.addressinput)

        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def addemployee(self):

        name = self.nameinput.text()
        branch = self.branchinput.itemText(self.branchinput.currentIndex())
        sem = self.seminput.itemText(self.seminput.currentIndex())
        mobile = self.mobileinput.text()
        address = self.addressinput.text()
        try:
            self.conn = sqlite3.connect("database.db")
            self.c = self.conn.cursor()
            self.c.execute("INSERT INTO employee (name,branch,sem,Mobile,address) VALUES (?,?,?,?,?)",
                           (name, branch, sem, mobile, address))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            QMessageBox.information(QMessageBox(), 'Successful', 'Student is added successfully to the database.')
            self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not add student to the database.')


class UpdateDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(UpdateDialog, self).__init__(*args, **kwargs)

        self.QBtn = QPushButton()
        self.QBtn.setText("Update")

        self.setWindowTitle("Update Employee")
        self.setFixedWidth(300)
        self.setFixedHeight(250)

        self.QBtn.clicked.connect(self.updateEmployee)

        layout = QVBoxLayout()

        self.idinput = QLineEdit()
        self.idinput.setPlaceholderText("ID")
        layout.addWidget(self.idinput)

        self.nameinput = QLineEdit()
        self.nameinput.setPlaceholderText("Name")
        layout.addWidget(self.nameinput)

        self.branchinput = QComboBox()
        self.branchinput.addItem("Manager")
        self.branchinput.addItem("Accountant")
        self.branchinput.addItem("CEO Deputy")
        self.branchinput.addItem("CEO")
        self.branchinput.addItem("System Adm.")
        self.branchinput.addItem("Security Adm.")
        layout.addWidget(self.branchinput)

        self.seminput = QComboBox()
        self.seminput.addItem("Non Confidential")
        self.seminput.addItem("Confidential")
        self.seminput.addItem("Secret")
        self.seminput.addItem("Top Secret")
        layout.addWidget(self.seminput)

        self.mobileinput = QLineEdit()
        self.mobileinput.setPlaceholderText("Mobile")
        self.mobileinput.setInputMask('999 999 99 99')
        layout.addWidget(self.mobileinput)

        self.addressinput = QLineEdit()
        self.addressinput.setPlaceholderText("Department")
        layout.addWidget(self.addressinput)

        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def updateEmployee(self):

        id = self.idinput.text()
        name = self.nameinput.text()
        branch = self.branchinput.itemText(self.branchinput.currentIndex())
        sem = self.seminput.itemText(self.seminput.currentIndex())
        mobile = self.mobileinput.text()
        address = self.addressinput.text()

        try:
            # Check if ID is available
            self.conn = sqlite3.connect("database.db")
            self.c = self.conn.cursor()
            result = self.c.execute("SELECT * from employee WHERE roll=" + str(id))
            row = result.fetchone()
            serachresult = "ID : " + str(row[0]) + '\n' + "Name : " + str(row[1]) + '\n' + "Role : " + str(
                row[2]) + '\n' + "Access Level : " + str(row[3]) + '\n' + "Department : " + str(row[4])
            QMessageBox.information(QMessageBox(), 'Successful', serachresult)
            self.conn.commit()
            self.c.close()
            self.conn.close()

            # Update employee data
            self.conn = sqlite3.connect("database.db")
            self.c = self.conn.cursor()
            # self.c.execute("INSERT INTO employee (name,branch,sem,Mobile,address) VALUES (?,?,?,?,?)",
            #                (name, branch, sem, mobile, address))
            self.c.execute(f"UPDATE employee SET name = '{name}',"
                           f"branch = '{branch}',"
                           f"sem = '{sem}',"
                           f"Mobile = '{mobile}',"
                           f"address = '{address}'"
                           f"WHERE roll = {id};")
            self.conn.commit()
            self.c.close()
            self.conn.close()
            QMessageBox.information(QMessageBox(), 'Successful', 'Employee was updated successfully.')
            self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not update employee data. Check ID')


class SearchDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(SearchDialog, self).__init__(*args, **kwargs)

        self.QBtn = QPushButton()
        self.QBtn.setText("Search")

        self.setWindowTitle("Search user")
        self.setFixedWidth(300)
        self.setFixedHeight(100)
        self.QBtn.clicked.connect(self.searchstudent)
        layout = QVBoxLayout()

        self.searchinput = QLineEdit()
        self.onlyInt = QIntValidator()
        self.searchinput.setValidator(self.onlyInt)
        self.searchinput.setPlaceholderText("Employee ID")
        layout.addWidget(self.searchinput)
        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def searchstudent(self):

        searchrol = self.searchinput.text()
        try:
            self.conn = sqlite3.connect("database.db")
            self.c = self.conn.cursor()
            result = self.c.execute("SELECT * from employee WHERE roll=" + str(searchrol))
            row = result.fetchone()
            serachresult = "ID : " + str(row[0]) + '\n' + "Name : " + str(row[1]) + '\n' + "Role : " + str(
                row[2]) + '\n' + "Access Level : " + str(row[3]) + '\n' + "Department : " + str(row[4])
            QMessageBox.information(QMessageBox(), 'Successful', serachresult)
            self.conn.commit()
            self.c.close()
            self.conn.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not Find employee from the database.')


class DeleteDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(DeleteDialog, self).__init__(*args, **kwargs)

        self.QBtn = QPushButton()
        self.QBtn.setText("Delete")

        self.setWindowTitle("Delete Student")
        self.setFixedWidth(300)
        self.setFixedHeight(100)
        self.QBtn.clicked.connect(self.deletestudent)
        layout = QVBoxLayout()

        self.deleteinput = QLineEdit()
        self.onlyInt = QIntValidator()
        self.deleteinput.setValidator(self.onlyInt)
        self.deleteinput.setPlaceholderText("ID")
        layout.addWidget(self.deleteinput)
        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def deletestudent(self):

        delrol = self.deleteinput.text()
        try:
            self.conn = sqlite3.connect("database.db")
            self.c = self.conn.cursor()
            self.c.execute("DELETE from employee WHERE roll=" + str(delrol))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            QMessageBox.information(QMessageBox(), 'Successful', 'Deleted From Table Successful')
            self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not Delete employee from the database.')


class LoginDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(LoginDialog, self).__init__(*args, **kwargs)

        self.setFixedWidth(300)
        self.setFixedHeight(120)

        layout = QVBoxLayout()

        self.passinput = QLineEdit()
        self.passinput.setEchoMode(QLineEdit.Password)
        self.passinput.setPlaceholderText("Enter Password.")
        self.QBtn = QPushButton()
        self.QBtn.setText("Login")
        self.setWindowTitle('Login')
        self.QBtn.clicked.connect(self.login)

        title = QLabel("Login")
        font = title.font()
        font.setPointSize(16)
        title.setFont(font)

        layout.addWidget(title)
        layout.addWidget(self.passinput)
        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    # Я в ИБ 4 года, всё безопасно, гарантирую
    def login(self):
        if self.passinput.text() == "pass":
            self.accept()
        else:
            QMessageBox.warning(self, 'Error', 'Wrong Password')


class ExportToCsvDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(ExportToCsvDialog, self).__init__(*args, **kwargs)

        self.setWindowTitle("Export To Csv File")
        self.setFixedWidth(300)
        self.setFixedHeight(100)

        self.saveFileDialog()

    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "",
                                                  "All Files (*);;Text Files (*.csv)", options=options)
        if fileName:
            self.exportToDict(fileName)

    def exportToDict(self, filename):

        exportFile = filename
        self.conn = sqlite3.connect("database.db")

        self.conn.row_factory = sqlite3.Row
        self.c = self.conn.cursor()
        self.c.execute('select * from employee')

        result = [dict(row) for row in self.c.fetchall()]

        self.exportToCsv(result, exportFile)

        self.c.close()
        self.conn.close()
        QMessageBox.information(QMessageBox(), 'Successful', 'Export Successful')
        self.close()

    def exportToCsv(self, result, filename):
        print(result)
        toCSV = result
        keys = toCSV[0].keys()
        with open(filename, 'w', newline='') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(toCSV)


class ImportFromCsvDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(ImportFromCsvDialog, self).__init__(*args, **kwargs)

        self.setWindowTitle("Import From Csv File")
        self.setFixedWidth(300)
        self.setFixedHeight(100)

        self.open()

    def open(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, 'Open a file', '',
                                           'Text Files (*.csv)', options=options)
        if fileName:
            self.import_to_db(fileName)

    def import_to_db(self, filename):
        self.conn = sqlite3.connect("database.db")
        self.c = self.conn.cursor()
        self.c.execute("DROP TABLE IF EXISTS employee")
        self.c.execute("""
                    CREATE TABLE IF NOT EXISTS employee(roll INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT,branch TEXT,
                    sem TEXT,mobile INTEGER,address TEXT)""")

        table_name = "employee"
        orders = pandas.read_csv(filename)  # load to DataFrame
        orders.to_sql(table_name, self.conn, if_exists='append', index=False)


class AboutDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(AboutDialog, self).__init__(*args, **kwargs)

        self.setFixedWidth(300)
        self.setFixedHeight(250)

        QBtn = QDialogButtonBox.Ok  # No cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()

        title = QLabel("Database management \nsystem")
        font = title.font()
        font.setPointSize(20)
        title.setFont(font)

        labelpic = QLabel()
        pixmap = QPixmap('icon/logo.png')
        pixmap = pixmap.scaledToWidth(275)
        labelpic.setPixmap(pixmap)
        labelpic.setFixedHeight(150)

        layout.addWidget(title)

        layout.addWidget(QLabel("Version 0.1"))
        layout.addWidget(QLabel("Created by Panov Sergey, RTU MIREA 2021"))
        layout.addWidget(labelpic)

        layout.addWidget(self.buttonBox)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Request a password to db
    passdlg = LoginDialog()

    if passdlg.exec_() == QDialog.Accepted:
        window = MainWindow()
        window.show()
        window.loaddata()
    sys.exit(app.exec_())
