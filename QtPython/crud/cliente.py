# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(704, 456)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 701, 171))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.edtendereco = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.edtendereco.setObjectName("edtendereco")
        self.gridLayout.addWidget(self.edtendereco, 10, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 10, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 9, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        self.edtnome = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.edtnome.setObjectName("edtnome")
        self.gridLayout.addWidget(self.edtnome, 0, 1, 1, 1)
        self.edttelefone = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.edttelefone.setObjectName("edttelefone")
        self.gridLayout.addWidget(self.edttelefone, 5, 1, 1, 1)
        self.edtcelular = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.edtcelular.setObjectName("edtcelular")
        self.gridLayout.addWidget(self.edtcelular, 9, 1, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 170, 631, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnnovo = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnnovo.setObjectName("btnnovo")
        self.horizontalLayout.addWidget(self.btnnovo)
        self.btnalterar = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnalterar.setObjectName("btnalterar")
        self.horizontalLayout.addWidget(self.btnalterar)
        self.btncancelar = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btncancelar.setObjectName("btncancelar")
        self.horizontalLayout.addWidget(self.btncancelar)
        self.btnsalvar = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnsalvar.setObjectName("btnsalvar")
        self.horizontalLayout.addWidget(self.btnsalvar)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, 210, 701, 221))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listView = QtWidgets.QListView(self.verticalLayoutWidget)
        self.listView.setObjectName("listView")
        self.verticalLayout.addWidget(self.listView)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.edtnome, self.edttelefone)
        MainWindow.setTabOrder(self.edttelefone, self.edtcelular)
        MainWindow.setTabOrder(self.edtcelular, self.edtendereco)
        MainWindow.setTabOrder(self.edtendereco, self.btnnovo)
        MainWindow.setTabOrder(self.btnnovo, self.btnalterar)
        MainWindow.setTabOrder(self.btnalterar, self.btncancelar)
        MainWindow.setTabOrder(self.btncancelar, self.btnsalvar)
        MainWindow.setTabOrder(self.btnsalvar, self.listView)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Nome"))
        self.label.setText(_translate("MainWindow", "Endereco"))
        self.label_3.setText(_translate("MainWindow", "Celular"))
        self.label_4.setText(_translate("MainWindow", "Telefone"))
        self.btnnovo.setText(_translate("MainWindow", "Novo"))
        self.btnalterar.setText(_translate("MainWindow", "Alterar"))
        self.btncancelar.setText(_translate("MainWindow", "Salvar"))
        self.btnsalvar.setText(_translate("MainWindow", "Cancelar"))