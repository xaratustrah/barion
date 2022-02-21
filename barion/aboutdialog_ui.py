# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rsrc/aboutdialog.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from . import gui_rc
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AbooutDialog(object):
    def setupUi(self, AbooutDialog):
        AbooutDialog.setObjectName("AbooutDialog")
        AbooutDialog.resize(515, 389)
        self.verticalLayout = QtWidgets.QVBoxLayout(AbooutDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(AbooutDialog)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/icons/icon_128x128.png"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(AbooutDialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_version = QtWidgets.QLabel(AbooutDialog)
        self.label_version.setObjectName("label_version")
        self.verticalLayout.addWidget(
            self.label_version, 0, QtCore.Qt.AlignHCenter)
        self.label_4 = QtWidgets.QLabel(AbooutDialog)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_ok = QtWidgets.QPushButton(AbooutDialog)
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.horizontalLayout.addWidget(self.pushButton_ok)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(AbooutDialog)
        self.pushButton_ok.pressed.connect(AbooutDialog.close)
        QtCore.QMetaObject.connectSlotsByName(AbooutDialog)

    def retranslateUi(self, AbooutDialog):
        _translate = QtCore.QCoreApplication.translate
        AbooutDialog.setWindowTitle(_translate("AbooutDialog", "Dialog"))
        self.label.setText(_translate("AbooutDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                      "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                      "p, li { white-space: pre-wrap; }\n"
                                      "</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                      "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.Helvetica Neue DeskInterface\'; font-size:24pt; font-weight:600; text-decoration: underline;\">barion</span></p>\n"
                                      "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.Helvetica Neue DeskInterface\';\">A scientific calculator and data table for chemical elements</span></p>\n"
                                      "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.Helvetica Neue DeskInterface\';\">and their isotopes</span></p>\n"
                                      "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.Helvetica Neue DeskInterface\';\">for the experimental and accelerator physicist.</span></p></body></html>"))
        self.label_version.setText(_translate(
            "AbooutDialog", "version placeholder"))
        self.label_4.setText(_translate("AbooutDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                        "p, li { white-space: pre-wrap; }\n"
                                        "</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                        "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.Helvetica Neue DeskInterface\';\">Copyright (c) Shahab Sanjari 2012-2016.</span></p>\n"
                                        "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.Helvetica Neue DeskInterface\';\">License: GPL.v3</span></p></body></html>"))
        self.pushButton_ok.setText(_translate("AbooutDialog", "OK"))
