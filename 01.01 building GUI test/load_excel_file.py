import sys, os
from PySide6.QtWidgets import (QApplication, QWidget, QTableWidget, QFileDialog,
                             QTableWidgetItem, QPushButton, QHeaderView, QHBoxLayout, QVBoxLayout)
from PySide6.QtCore import Qt
from ui_load_excel_file import Ui_Form
import pandas as pd  # pip install pandas


class MyApp(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.excel_file_path = ""
        self.worksheet_name = 'Sheet1'

        self.setWindowTitle('Load Excel (or CSV) data to QTableWidget')
        # self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

        self.open_btn.clicked.connect(self.getFileName)
        self.load_btn.clicked.connect(self.loadExcelData)


    def getFileName(self):

        file_filter = 'Data File (*.xlsx *.csv *.dat);; Excel File (*.xlsx *.xls)'
        response = QFileDialog.getOpenFileName(
            parent=self,
            caption='Select a data file',
            dir=os.getcwd(),
            filter=file_filter,
            selectedFilter='Excel File (*.xlsx *.xls)'
        )
        print(response)
        self.excel_file_path = response[0]
        file_name = self.excel_file_path.split("/")[-1]
        self.show_name.setText(file_name)
        self.show_name.setAlignment(Qt.AlignCenter)

    def loadExcelData(self):
        df = pd.read_excel(self.excel_file_path, self.worksheet_name)
        if df.size == 0:
            return

        df.fillna('', inplace=True)
        self.table.setRowCount(df.shape[0])
        self.table.setColumnCount(df.shape[1])
        style = "::section {""background-color: lightblue; }"
        self.table.horizontalHeader().setStyleSheet(style)
        self.table.setHorizontalHeaderLabels(df.columns)

        # returns pandas array object
        max_value = 0
        for row in df.itertuples():
            for i in range(len(row)-1):
                row_idx = row[0]
                col_idx = i
                value = row[i]
                tbl_itm = QTableWidgetItem(str(value))
                # if col_idx == 3 and len(str(value)) > max_value:
                #     print(f"{value = }, {len(str(value)) = }")
                #     max_value = len(str(value))
                self.table.setItem(row_idx, col_idx, tbl_itm)


        # max(df["종목명"].apply(lambda x: len(x)))

        #
        # for row in df.iterrows():
        #     values = row[1]
        #     for col_index, value in enumerate(values):
        #         if isinstance(value, (float, int)):
        #             value = '{0:0,.0f}'.format(value)
        #         tableItem = QTableWidgetItem(str(value))
        #         self.table.setItem(row[0], col_index, tableItem)

        # self.table.setColumnWidth(3, 220)
        # self.table.setColumnWidth(4, 200)

if __name__ == '__main__':
    # don't auto scale when drag app to a different monitor.
    # QGuiApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

    app = QApplication(sys.argv)
    app.setStyleSheet('''
        QWidget {
            font-size: 20px;
        }
    ''')

    myApp = MyApp()
    myApp.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Closing Window...')