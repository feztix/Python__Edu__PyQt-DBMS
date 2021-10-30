import sqlite3

from main import *


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.conn = sqlite3.connect("database.db")
        self.c = self.conn.cursor()
        self.c.execute(
            "CREATE TABLE IF NOT EXISTS employee(roll INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT,branch TEXT,"
            "sem TEXT,mobile INTEGER,address TEXT)")
        self.c.close()

        file_menu = self.menuBar().addMenu("&File")

        help_menu = self.menuBar().addMenu("&About")
        self.setWindowTitle("Database management system")

        self.setMinimumSize(800, 600)

        self.tableWidget = QTableWidget()
        self.setCentralWidget(self.tableWidget)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.tableWidget.setHorizontalHeaderLabels(("ID", "Name", "Role", "Access Level", "Mobile", "Department"))

        toolbar = QToolBar()
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        statusbar = QStatusBar()
        self.setStatusBar(statusbar)

        btn_ac_adduser = QAction(QIcon("icon/add.png"), "Add Employee", self)
        btn_ac_adduser.triggered.connect(self.insert)
        btn_ac_adduser.setStatusTip("Add Student")
        toolbar.addAction(btn_ac_adduser)

        btn_ac_changeuser = QAction(QIcon("icon/shuffle.png"), "Update Employee", self)
        btn_ac_changeuser.triggered.connect(self.update)
        btn_ac_changeuser.setStatusTip("Update Employee")
        toolbar.addAction(btn_ac_changeuser)

        btn_ac_refresh = QAction(QIcon("icon/refresh.png"), "Refresh", self)
        btn_ac_refresh.triggered.connect(self.loaddata)
        btn_ac_refresh.setStatusTip("Refresh Table")
        toolbar.addAction(btn_ac_refresh)

        btn_ac_search = QAction(QIcon("icon/search.png"), "Search", self)
        btn_ac_search.triggered.connect(self.search)
        btn_ac_search.setStatusTip("Search User")
        toolbar.addAction(btn_ac_search)

        btn_ac_delete = QAction(QIcon("icon/trash.png"), "Delete", self)
        btn_ac_delete.triggered.connect(self.delete)
        btn_ac_delete.setStatusTip("Delete User")
        toolbar.addAction(btn_ac_delete)

        adduser_action = QAction(QIcon("icon/add.png"), "Insert Employee", self)
        adduser_action.triggered.connect(self.insert)
        file_menu.addAction(adduser_action)

        changeuser_action = QAction(QIcon("icon/shuffle.png"), "Update Employee", self)
        changeuser_action.triggered.connect(self.update)
        file_menu.addAction(changeuser_action)

        searchuser_action = QAction(QIcon("icon/search.png"), "Search Employee", self)
        searchuser_action.triggered.connect(self.search)
        file_menu.addAction(searchuser_action)

        deluser_action = QAction(QIcon("icon/trash.png"), "Delete", self)
        deluser_action.triggered.connect(self.delete)
        file_menu.addAction(deluser_action)

        export_csv_action = QAction(QIcon(""), "Export CSV", self)
        export_csv_action.triggered.connect(self.export)
        file_menu.addAction(export_csv_action)

        import_csv_action = QAction(QIcon(""), "Import CSV", self)
        import_csv_action.triggered.connect(self._import)
        file_menu.addAction(import_csv_action)

        about_action = QAction(QIcon("icon/info.png"), "About", self)
        about_action.triggered.connect(self.about)
        help_menu.addAction(about_action)

    def loaddata(self):
        self.connection = sqlite3.connect("database.db")
        query = "SELECT * FROM employee"
        result = self.connection.execute(query)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        self.connection.close()

    def insert(self):
        dlg = InsertDialog()
        dlg.exec_()

    def update(self):
        dlg = UpdateDialog()
        dlg.exec_()

    def delete(self):
        dlg = DeleteDialog()
        dlg.exec_()

    def search(self):
        dlg = SearchDialog()
        dlg.exec_()

    def export(self):
        dlg = ExportToCsvDialog()

    def _import(self):
        dlg = ImportFromCsvDialog()
        # dlg.exec_()

    def about(self):
        dlg = AboutDialog()
        dlg.exec_()
