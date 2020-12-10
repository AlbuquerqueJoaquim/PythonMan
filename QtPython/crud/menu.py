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
        MainWindow.resize(568, 297)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 568, 22))
        self.menubar.setObjectName("menubar")
        self.menu_Cadastro = QtWidgets.QMenu(self.menubar)
        self.menu_Cadastro.setObjectName("menu_Cadastro")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_Cliente = QtWidgets.QAction(MainWindow)
        self.action_Cliente.setObjectName("action_Cliente")
        self.action_Fornecedor = QtWidgets.QAction(MainWindow)
        self.action_Fornecedor.setObjectName("action_Fornecedor")
        self.menu_Cadastro.addSeparator()
        self.menu_Cadastro.addAction(self.action_Cliente)
        self.menu_Cadastro.addAction(self.action_Fornecedor)
        self.menubar.addAction(self.menu_Cadastro.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu_Cadastro.setTitle(_translate("MainWindow", "&Cadastro"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.action_Cliente.setText(_translate("MainWindow", "&Cliente"))
        self.action_Fornecedor.setText(_translate("MainWindow", "&Fornecedor"))
