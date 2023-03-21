import sys
from PyQt5.QtWidgets import *
from service import Service
from PyQt5.QtGui import QFont, QFontDatabase
from PyQt5 import QtCore

class App(QWidget):
	def __init__(self):
		super().__init__()
		self.title = 'System Processes'
		self.left = 0
		self.top = 0
		self.width = 600
		self.height = 400

		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)

		self.createTable()

		self.layout = QVBoxLayout()
		self.layout.addWidget(self.tableWidget)
		self.setLayout(self.layout)

		#Show window
		self.show()

	#Create table
	def createTable(self):
		service = Service()
		data = service.get_process_data()
		self.tableWidget = QTableWidget()

		#Row count
		self.tableWidget.setRowCount(len(data))
		row = 0

		#Column count
		self.tableWidget.setColumnCount(12)
		column = 0

		for data_row in data:
			# print(data_row)
			row+=1
			self.tableWidget.resizeRowsToContents()
			self.tableWidget.setItem(row,0, QTableWidgetItem(data_row['PID']))
			self.tableWidget.setItem(row,1, QTableWidgetItem(data_row['USER']))
			self.tableWidget.setItem(row,2, QTableWidgetItem(data_row['PRIORITY']))
			self.tableWidget.setItem(row,3, QTableWidgetItem(data_row['NICE VALUE']))
			self.tableWidget.setItem(row,4, QTableWidgetItem(data_row['VIRTUAL']))
			self.tableWidget.setItem(row,5, QTableWidgetItem(data_row['RESERVED']))
			self.tableWidget.setItem(row,6, QTableWidgetItem(data_row['SHARED']))
			self.tableWidget.setItem(row,7, QTableWidgetItem(data_row['STATUS']))
			self.tableWidget.setItem(row,8, QTableWidgetItem(data_row['%CPU']))
			self.tableWidget.setItem(row,9, QTableWidgetItem(data_row['%MEMORY']))
			self.tableWidget.setItem(row,10, QTableWidgetItem(data_row['TIME']))
			self.tableWidget.setItem(row,11, QTableWidgetItem(data_row['COMMAND']))


		for data_column in data:
			column=+1
			#self.tableWidget.setColumnWidth(10,100)
			self.tableWidget.resizeColumnsToContents()
			self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem('PID'))
			self.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem('USER'))
			self.tableWidget.setHorizontalHeaderItem(2, QTableWidgetItem('PRIORITY'))
			self.tableWidget.setHorizontalHeaderItem(3, QTableWidgetItem("NICENESS_VALUE"))
			self.tableWidget.setHorizontalHeaderItem(4, QTableWidgetItem('VIRTUAL'))
			self.tableWidget.setHorizontalHeaderItem(5, QTableWidgetItem('RESERVED'))
			self.tableWidget.setHorizontalHeaderItem(6, QTableWidgetItem('SHARED'))
			self.tableWidget.setHorizontalHeaderItem(7, QTableWidgetItem('STATUS'))
			self.tableWidget.setHorizontalHeaderItem(8, QTableWidgetItem('%CPU'))
			self.tableWidget.setHorizontalHeaderItem(9, QTableWidgetItem('%MEMORY'))
			self.tableWidget.setHorizontalHeaderItem(10, QTableWidgetItem('TIME'))
			self.tableWidget.setHorizontalHeaderItem(11, QTableWidgetItem('COMMAND'))



		#Table will fit the screen horizontally
		#self.tableWidget.horizontalHeader().setStretchLastSection(True)
		#self.tableWidget.horizontalHeader().setSectionResizeMode(
		#	QHeaderView.Stretch)
		
	def update(self):
		self.adjustSize()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())
