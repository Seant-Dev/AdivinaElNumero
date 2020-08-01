# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import random
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    attempt_limit = 5
    attempts = 0
    mm_count = random.randint(1, 100)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(340, 226)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 321, 121))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(10, 80, 301, 31))
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 140, 301, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 140, 301, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.groupBox.raise_()
        self.pushButton_2.raise_()
        self.pushButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 340, 22))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        self.menuAyuda = QtWidgets.QMenu(self.menubar)
        self.menuAyuda.setObjectName("menuAyuda")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.showMessage("Adivina el numero entre 1 y 100")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSalir = QtWidgets.QAction(MainWindow)
        self.actionSalir.setObjectName("actionSalir")
        self.actionAcerca_de = QtWidgets.QAction(MainWindow)
        self.actionAcerca_de.setObjectName("actionAcerca_de")
        self.menuArchivo.addAction(self.actionSalir)
        self.menuAyuda.addAction(self.actionAcerca_de)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())

        self.pushButton.clicked.connect(self.lanzador)
        self.pushButton_2.clicked.connect(self.reiniciar)
        self.actionAcerca_de.triggered.connect(self.acerca)
        self.actionSalir.triggered.connect(self.close)
        self.centralwidget.activateWindow()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Adivina el número"))
        self.groupBox.setTitle(_translate("MainWindow", "Adivina el número"))
        self.label.setText(_translate("MainWindow", "?"))
        self.pushButton.setText(_translate("MainWindow", "Verificar"))
        self.pushButton_2.setText(_translate("MainWindow", "Reiniciar"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.menuAyuda.setTitle(_translate("MainWindow", "Ayuda"))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))
        self.actionAcerca_de.setText(_translate("MainWindow", "Acerca de"))

    def acerca(self):
        QMessageBox.question(self, 'Acerca de', "Desarrollada por Antonio Mejia (seant)", QMessageBox.Ok)

    def reiniciar(self):
        self.label.setText("?")
        self.mm_count = random.randint(1, 100)
        self.attempts = 0
        self.statusbar.showMessage("Adivina el numero entre 1 y 100")
        self.lineEdit.clear()
        self.pushButton_2.setHidden(True)
        self.pushButton.setVisible(True)
        self.lineEdit.setEnabled(True)
        self.pushButton.setEnabled(True)
        self.lineEdit.setFocus()

    def limpiar(self):
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setVisible(True)
        self.pushButton_2.setText("Reiniciar")
        self.pushButton.setHidden(True)
        self.pushButton.setDisabled(True)

    def lanzador(self):
        try:
            guess_text = self.lineEdit.text()
            guess = int(guess_text)
        except ValueError:
            self.lineEdit.clear()
            self.lineEdit.setFocus()
        else:
            self.attempts += 1
            self.lineEdit.setFocus()
            if (guess > 100) or (guess <= 0):
                self.lineEdit.clear()
                self.lineEdit.setFocus()
                self.attempts -= 1
            elif self.mm_count == guess:
                self.label.setText(f"Correcto el numero es: {guess}")
                self.statusbar.showMessage(f"Adivinaste en {self.attempts} intentos")
                self.lineEdit.setDisabled(True)
                self.limpiar()
            elif self.attempts < 5:
                if guess < self.mm_count:
                    self.label.setText(f"Muy Bajo! ({self.attempts})")
                    self.statusbar.showMessage(f"Tienes {self.attempt_limit - self.attempts} intentos restantes")
                    self.lineEdit.clear()
                else:
                    self.label.setText(f"Muy Alto! ({self.attempts})")
                    self.statusbar.showMessage(f"Tienes {self.attempt_limit - self.attempts} intentos restantes")
                    self.lineEdit.clear()
            else:
                self.label.setText(f"El numero era: {self.mm_count}")
                self.statusbar.showMessage(f"Tienes {self.attempt_limit - self.attempts} intentos restantes")
                self.pushButton.setDisabled(True)
                self.lineEdit.setDisabled(True)
                self.limpiar()
