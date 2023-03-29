import sys
from PyQt5.QtWidgets import *
from service import Service
#from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QTimer
from main import get_process_data
from datetime import datetime



class App(QWidget):
	def __init__(self):
		super().__init__()
		self.title = 'System Processes'
		self.left = 0
		self.top = 0
		self.width = 1200
		self.height = 500

		self.setWindowTitle(self.title)	
		self.setGeometry(self.left, self.top, self.width, self.height)

		self.get_data()
		self.createTable()
		self.layout = QVBoxLayout()
		self.layout.addWidget(self.ref_btn())
		self.layout.addSpacing(20)
		#self.layout.addWidget(self.clr_btn())
		self.layout.addSpacing(20)
		self.layout.addWidget(self.tableWidget, stretch = 1)
		self.setLayout(self.layout)

		#Show window
		self.show()
		self.ref_btn()
		self.clicked_btn()
		#self.clr_btn()
		#self.clearContent()	
		self.upload_data()
		# self.auto_refresh()
		

	#Create table
	def get_data(self):
		self.service = Service()
		self.data = self.service.get_process_data()

	def createTable(self):
		self.tableWidget = QTableWidget()
		
		self.upload_data()

		# #Row count
		# self.tableWidget.setRowCount(len(data))
		# row = 0

		# #Column count
		# self.tableWidget.setColumnCount(12)
		# #column = 0 

	def upload_data(self):
		#Row count
		self.tableWidget.setRowCount(len(self.data))
		row = 0

		#Column count
		self.tableWidget.setColumnCount(12)
		#column = 0
		for data_row in self.data:
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




	# def auto_refresh(self):
	# 	self.timer = QTimer()
	# 	self.timer.setInterval(15000)
	# 	self.timer.timeout.connect(self.clicked_btn)
	# 	self.timer.start()

	

	def ref_btn(self):
		self.btn = QPushButton('Refresh', self)
		self.btn.clicked.connect(self.clicked_btn)

	def clicked_btn(self):
		self.tableWidget.clearContents()

		self.get_data()
		self.upload_data()



		# start = datetime.now()
		#self.createTable()
		#self.upload_data()
		# print('Table update took: ' + str((datetime.now() - start).total_seconds()) + ' secs')



	# def clr_btn(self):
	# 	self.clrBtn = QPushButton('Clear Table', self)
	# 	self.clrBtn.clicked.connect(self.clearContent)

	# def clearContent(self):
	# 	self.tableWidget.clearContents()
	# 	self.tableWidget.setRowCount(0)
	# 	self.tableWidget.setColumnCount(0)

	




	def update(self):
		self.adjustSize()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())