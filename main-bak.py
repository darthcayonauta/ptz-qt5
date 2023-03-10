# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
# Developed by Ing. Claudio Guzman Herrera
# 22 / FEB / 2023
# 
# Uso de interfaz gráfica PyQT5 , Threadings, ONVIF-PTZ y clases externas 
# Enjoy

#medidas 640 x 360
from PyQt5 import QtCore, QtGui, QtWidgets
import videoThread2 

from PyQt5.QtCore import QThread, QTimer
from PyQt5.QtGui import QFont, QPixmap, QImage
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QGridLayout,QMessageBox
import sys
from claseMov import *
import threading


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        self.user    = 'admin'
        self.passw   = 'Admin321'
        self.ip      = '192.168.78.90'
        self.url = f'rtsp://{self.user}:{self.passw}@{self.ip}:554/h264/ch1/main/av_stream'    
        self.w = 960
        self.h = 540

        self.obj_mover = MoverCam(self.ip,self.user,self.passw)

        print("Esto es equivalente al constructor!!!")
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1300, 560)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.videoLabel = QtWidgets.QLabel(self.centralwidget)
        self.videoLabel.setGeometry(QtCore.QRect(5, 10, 960, 540))
        self.videoLabel.setStyleSheet("background-color : rgb(0, 0, 0);")
        self.videoLabel.setText("")
        self.videoLabel.setObjectName("videoLabel")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1100, 20, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(970, 60, 500, 300))
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.btn_up = QtWidgets.QPushButton(self.widget)
        self.btn_up.setGeometry(QtCore.QRect(125, 120, 93, 28))
        self.btn_up.setObjectName("btn_up")
        self.btn_down = QtWidgets.QPushButton(self.widget)
        self.btn_down.setGeometry(QtCore.QRect(125, 210, 93, 28))
        self.btn_down.setObjectName("btn_down")
        self.btn_left = QtWidgets.QPushButton(self.widget)
        self.btn_left.setGeometry(QtCore.QRect(30, 160, 93, 28))
        self.btn_left.setObjectName("btn_left")
        self.btn_right = QtWidgets.QPushButton(self.widget)
        self.btn_right.setGeometry(QtCore.QRect(220, 160, 93, 28))
        self.btn_right.setObjectName("btn_right")
        self.btn_diag_sup_izq = QtWidgets.QPushButton(self.widget)
        self.btn_diag_sup_izq.setGeometry(QtCore.QRect(30, 120, 93, 28))
        self.btn_diag_sup_izq.setObjectName("btn_diag_sup_izq")
        self.btn_diag_inf_izq = QtWidgets.QPushButton(self.widget)
        self.btn_diag_inf_izq.setGeometry(QtCore.QRect(30, 210, 93, 28))
        self.btn_diag_inf_izq.setObjectName("btn_diag_inf_izq")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(170, 160, 21, 16))
        self.label.setObjectName("label")
        self.btn_diag_sup_der = QtWidgets.QPushButton(self.widget)
        self.btn_diag_sup_der.setGeometry(QtCore.QRect(220, 120, 93, 28))
        self.btn_diag_sup_der.setObjectName("btn_diag_sup_der")
        self.btn_diag_der_inf = QtWidgets.QPushButton(self.widget)
        self.btn_diag_der_inf.setGeometry(QtCore.QRect(220, 210, 93, 28))
        self.btn_diag_der_inf.setObjectName("btn_diag_der_inf")

        self.btn_zoomIn = QtWidgets.QPushButton(self.widget)
        self.btn_zoomIn.setGeometry(QtCore.QRect(30, 250, 93, 28))
        self.btn_zoomIn.setObjectName("zoomIn")

        self.btn_zoomOut = QtWidgets.QPushButton(self.widget)
        self.btn_zoomOut.setGeometry(QtCore.QRect(125, 250, 93, 28))
        self.btn_zoomOut.setObjectName("zoomOut")


        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1200, 20, 55, 16))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        
        self.label_2.setText(_translate("MainWindow", "PTZ TEST"))
        self.btn_up.setText(_translate("MainWindow", "Up"))
        self.btn_down.setText(_translate("MainWindow", "Down"))
        self.btn_left.setText(_translate("MainWindow", "left"))
        self.btn_right.setText(_translate("MainWindow", "Right"))
        self.btn_diag_sup_izq.setText(_translate("MainWindow", "Diagonal Sup Iz"))
        self.btn_diag_inf_izq.setText(_translate("MainWindow", "Diagonal Inf Iz"))
        self.btn_zoomIn.setText(_translate("MainWindow", "Zoom In (+)"))
        self.btn_zoomOut.setText(_translate("MainWindow", "Zoom Out (-)"))

        self.label.setText(_translate("MainWindow", "X"))
        self.btn_diag_sup_der.setText(_translate("MainWindow", "Diagonal Sup Der"))
        self.btn_diag_der_inf.setText(_translate("MainWindow", "Diagonal Inf Der"))
        self.label_3.setText(_translate("MainWindow", "By CGH"))
        self.videoLabel.setText("NO IMAGE")
        self.videoLabel.setStyleSheet("background-color: #000000;color:#FFFFFF;text-align:center;")
        print("llamando funciones....")
        self.showCam()

        #llamando a funciones PTZ
        self.btn_up.clicked.connect(self.moveUp)
        self.btn_down.clicked.connect(self.moveDown)
        self.btn_left.clicked.connect(self.moveLeft)
        self.btn_right.clicked.connect(self.moveRight)
        self.btn_diag_sup_izq.clicked.connect(self.diagonalIzqSup)
        self.btn_diag_sup_der.clicked.connect(self.diagonalDerSup)
        self.btn_diag_der_inf.clicked.connect(self.diagonalDerInf)
        self.btn_diag_inf_izq.clicked.connect(self.diagonalIzqInf)
        self.btn_zoomIn.clicked.connect(self.zoomIn)
        self.btn_zoomOut.clicked.connect(self.zoomOut)

    
    #mostrar imagenes
    def showCam(self) :
        self.thread = QThread()
        self.videoPTZ = videoThread2.CamsTh( self.url  )
        self.videoPTZ.ch_signal.connect( self.ch_signal )
        self.videoPTZ.moveToThread( self.thread )
        self.thread.started.connect( self.videoPTZ.run )
        self.thread.start()

    def ch_signal(self,px) : 
        QImg = QImage(px, self.w, self.h, QImage.Format_RGB888)        
        pixMap = QPixmap.fromImage(QImg)
        self.videoLabel.setPixmap( pixMap)

    #movimientos PTZ // Calling movement functions
    def moveUp(self):
        #self.obj_mover.moves(1)
        hilo = threading.Thread(target=self.obj_mover.moves,kwargs={'num':1})
        hilo.start()

    def moveDown(self):
        #self.obj_mover.moves(2)
        hilo = threading.Thread(target=self.obj_mover.moves,kwargs={'num':2})
        hilo.start()
    
    def moveLeft(self):
        #self.obj_mover.moves(3)
        hilo = threading.Thread(target=self.obj_mover.moves,kwargs={'num':3})
        hilo.start()

    def moveRight(self):
        #self.obj_mover.moves(4)
        hilo = threading.Thread(target=self.obj_mover.moves,kwargs={'num':4})
        hilo.start()

    def zoomIn(self) :
        #self.obj_mover.moves(5)
        hilo = threading.Thread(target=self.obj_mover.moves,kwargs={'num':5})
        hilo.start()

    def zoomOut(self) :
        #self.obj_mover.moves(6)
        hilo = threading.Thread(target=self.obj_mover.moves,kwargs={'num':6})
        hilo.start()

    def diagonalIzqSup(self) :
        hilo = threading.Thread(target=self.obj_mover.moves, kwargs={'num':9})
        hilo.start()

    def diagonalIzqInf(self) :
        hilo = threading.Thread(target=self.obj_mover.moves, kwargs={'num':10})
        hilo.start()

    def diagonalDerSup(self) :
        hilo = threading.Thread(target=self.obj_mover.moves, kwargs={'num':7})
        hilo.start()

    def diagonalDerInf(self) :
        hilo = threading.Thread(target=self.obj_mover.moves, kwargs={'num':8})
        hilo.start()
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    #app.setStyleSheet('background-color:#000000;')
    MainWindow = QtWidgets.QMainWindow()
    #MainWindow.setStyleSheet('background-color:#efefef;')
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
