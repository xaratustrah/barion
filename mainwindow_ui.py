# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rsrc/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1069, 742)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.spinBox_zz = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_zz.setProperty("value", 6)
        self.spinBox_zz.setObjectName("spinBox_zz")
        self.gridLayout.addWidget(self.spinBox_zz, 1, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.groupBox)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 2, 0, 1, 1)
        self.spinBox_nn = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_nn.setProperty("value", 6)
        self.spinBox_nn.setObjectName("spinBox_nn")
        self.gridLayout.addWidget(self.spinBox_nn, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.spinBox_qq = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_qq.setMinimum(1)
        self.spinBox_qq.setMaximum(150)
        self.spinBox_qq.setProperty("value", 6)
        self.spinBox_qq.setObjectName("spinBox_qq")
        self.gridLayout.addWidget(self.spinBox_qq, 3, 1, 1, 1)
        self.comboBox_name = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_name.setObjectName("comboBox_name")
        self.gridLayout.addWidget(self.comboBox_name, 0, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.groupBox)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.label_name = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_name.setFont(font)
        self.label_name.setLineWidth(1)
        self.label_name.setText("")
        self.label_name.setTextFormat(QtCore.Qt.AutoText)
        self.label_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name.setObjectName("label_name")
        self.verticalLayout_2.addWidget(self.label_name)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_nav_nw = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_nav_nw.setObjectName("pushButton_nav_nw")
        self.gridLayout_2.addWidget(self.pushButton_nav_nw, 0, 0, 1, 1)
        self.pushButton_nav_n = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_nav_n.setObjectName("pushButton_nav_n")
        self.gridLayout_2.addWidget(self.pushButton_nav_n, 0, 1, 1, 1)
        self.pushButton_nav_ne = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_nav_ne.setObjectName("pushButton_nav_ne")
        self.gridLayout_2.addWidget(self.pushButton_nav_ne, 0, 2, 1, 1)
        self.pushButton_nav_w = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_nav_w.setObjectName("pushButton_nav_w")
        self.gridLayout_2.addWidget(self.pushButton_nav_w, 1, 0, 1, 1)
        self.pushButton_nav_e = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_nav_e.setObjectName("pushButton_nav_e")
        self.gridLayout_2.addWidget(self.pushButton_nav_e, 1, 2, 1, 1)
        self.pushButton_nav_sw = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_nav_sw.setObjectName("pushButton_nav_sw")
        self.gridLayout_2.addWidget(self.pushButton_nav_sw, 2, 0, 1, 1)
        self.pushButton_nav_s = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_nav_s.setObjectName("pushButton_nav_s")
        self.gridLayout_2.addWidget(self.pushButton_nav_s, 2, 1, 1, 1)
        self.pushButton_nav_se = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_nav_se.setObjectName("pushButton_nav_se")
        self.gridLayout_2.addWidget(self.pushButton_nav_se, 2, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 6, 2, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.groupBox_2)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 9, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 2, 2, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.groupBox_2)
        self.label_18.setObjectName("label_18")
        self.gridLayout_3.addWidget(self.label_18, 3, 2, 1, 1)
        self.checkBox_circum = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_circum.setObjectName("checkBox_circum")
        self.gridLayout_3.addWidget(self.checkBox_circum, 4, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 0, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 1, 2, 1, 1)
        self.comboBox_ring = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_ring.setObjectName("comboBox_ring")
        self.comboBox_ring.addItem("")
        self.comboBox_ring.addItem("")
        self.comboBox_ring.addItem("")
        self.comboBox_ring.addItem("")
        self.comboBox_ring.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_ring, 4, 1, 1, 1)
        self.doubleSpinBox_energy = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_energy.setDecimals(4)
        self.doubleSpinBox_energy.setMaximum(10000.0)
        self.doubleSpinBox_energy.setSingleStep(0.0001)
        self.doubleSpinBox_energy.setProperty("value", 400.0)
        self.doubleSpinBox_energy.setObjectName("doubleSpinBox_energy")
        self.gridLayout_3.addWidget(self.doubleSpinBox_energy, 0, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.groupBox_2)
        self.label_17.setObjectName("label_17")
        self.gridLayout_3.addWidget(self.label_17, 4, 0, 1, 1)
        self.doubleSpinBox_f_unknown = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_f_unknown.setDecimals(4)
        self.doubleSpinBox_f_unknown.setMaximum(10000.0)
        self.doubleSpinBox_f_unknown.setSingleStep(0.0001)
        self.doubleSpinBox_f_unknown.setProperty("value", 245.0)
        self.doubleSpinBox_f_unknown.setObjectName("doubleSpinBox_f_unknown")
        self.gridLayout_3.addWidget(self.doubleSpinBox_f_unknown, 9, 1, 1, 1)
        self.doubleSpinBox_f_actual = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_f_actual.setDecimals(4)
        self.doubleSpinBox_f_actual.setMaximum(10000.0)
        self.doubleSpinBox_f_actual.setSingleStep(0.0001)
        self.doubleSpinBox_f_actual.setProperty("value", 245.0)
        self.doubleSpinBox_f_actual.setObjectName("doubleSpinBox_f_actual")
        self.gridLayout_3.addWidget(self.doubleSpinBox_f_actual, 6, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 2, 0, 1, 1)
        self.doubleSpinBox_path_length = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_path_length.setDecimals(3)
        self.doubleSpinBox_path_length.setMaximum(100000.0)
        self.doubleSpinBox_path_length.setSingleStep(0.0001)
        self.doubleSpinBox_path_length.setProperty("value", 108.5)
        self.doubleSpinBox_path_length.setObjectName("doubleSpinBox_path_length")
        self.gridLayout_3.addWidget(self.doubleSpinBox_path_length, 3, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.groupBox_2)
        self.label_19.setObjectName("label_19")
        self.gridLayout_3.addWidget(self.label_19, 3, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.groupBox_2)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 9, 0, 1, 1)
        self.doubleSpinBox_f_analysis = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_f_analysis.setDecimals(4)
        self.doubleSpinBox_f_analysis.setMaximum(10000.0)
        self.doubleSpinBox_f_analysis.setSingleStep(0.0001)
        self.doubleSpinBox_f_analysis.setProperty("value", 245.0)
        self.doubleSpinBox_f_analysis.setObjectName("doubleSpinBox_f_analysis")
        self.gridLayout_3.addWidget(self.doubleSpinBox_f_analysis, 1, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 6, 0, 1, 1)
        self.doubleSpinBox_beam_current = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_beam_current.setDecimals(4)
        self.doubleSpinBox_beam_current.setMaximum(10000.0)
        self.doubleSpinBox_beam_current.setSingleStep(0.0001)
        self.doubleSpinBox_beam_current.setProperty("value", 1.0)
        self.doubleSpinBox_beam_current.setObjectName("doubleSpinBox_beam_current")
        self.gridLayout_3.addWidget(self.doubleSpinBox_beam_current, 2, 1, 1, 1)
        self.line = QtWidgets.QFrame(self.groupBox_2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_3.addWidget(self.line, 5, 1, 1, 1)
        self.horizontalLayout_2.addWidget(self.groupBox_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_calculate = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_calculate.setObjectName("pushButton_calculate")
        self.verticalLayout.addWidget(self.pushButton_calculate)
        self.pushButton_table_data = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_table_data.setObjectName("pushButton_table_data")
        self.verticalLayout.addWidget(self.pushButton_table_data)
        self.line_4 = QtWidgets.QFrame(self.groupBox_5)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.line_4)
        self.pushButton_isotopes = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_isotopes.setObjectName("pushButton_isotopes")
        self.verticalLayout.addWidget(self.pushButton_isotopes)
        self.pushButton_isobars = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_isobars.setObjectName("pushButton_isobars")
        self.verticalLayout.addWidget(self.pushButton_isobars)
        self.pushButton_isotones = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_isotones.setObjectName("pushButton_isotones")
        self.verticalLayout.addWidget(self.pushButton_isotones)
        self.line_2 = QtWidgets.QFrame(self.groupBox_5)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.pushButton_identify = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_identify.setObjectName("pushButton_identify")
        self.verticalLayout.addWidget(self.pushButton_identify)
        self.line_3 = QtWidgets.QFrame(self.groupBox_5)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.pushButton_save = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_save.setObjectName("pushButton_save")
        self.verticalLayout.addWidget(self.pushButton_save)
        self.pushButton_clear = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.verticalLayout.addWidget(self.pushButton_clear)
        self.horizontalLayout.addWidget(self.groupBox_5)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_4)
        self.textBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textBrowser.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout_3.addWidget(self.textBrowser)
        self.horizontalLayout.addWidget(self.groupBox_4)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tableView = QtWidgets.QTableView(self.groupBox_3)
        self.tableView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView.setProperty("showDropIndicator", False)
        self.tableView.setDragDropOverwriteMode(False)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setShowGrid(True)
        self.tableView.setGridStyle(QtCore.Qt.DotLine)
        self.tableView.setSortingEnabled(True)
        self.tableView.setWordWrap(False)
        self.tableView.setCornerButtonEnabled(True)
        self.tableView.setObjectName("tableView")
        self.tableView.verticalHeader().setVisible(False)
        self.gridLayout_4.addWidget(self.tableView, 0, 0, 1, 1)
        self.horizontalLayout_4.addWidget(self.groupBox_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1069, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad_Freqlist = QtWidgets.QAction(MainWindow)
        self.actionLoad_Freqlist.setObjectName("actionLoad_Freqlist")
        self.actionClear_results = QtWidgets.QAction(MainWindow)
        self.actionClear_results.setObjectName("actionClear_results")
        self.actionSave_results = QtWidgets.QAction(MainWindow)
        self.actionSave_results.setObjectName("actionSave_results")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionAbout)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionLoad_Freqlist)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave_results)
        self.menuFile.addAction(self.actionClear_results)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.checkBox_circum.toggled['bool'].connect(self.doubleSpinBox_path_length.setDisabled)
        self.checkBox_circum.toggled['bool'].connect(self.label_19.setDisabled)
        self.checkBox_circum.toggled['bool'].connect(self.label_18.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "barion"))
        self.groupBox.setTitle(_translate("MainWindow", "Navigation"))
        self.label_2.setText(_translate("MainWindow", "Z:"))
        self.label_20.setText(_translate("MainWindow", "N:"))
        self.label_3.setText(_translate("MainWindow", "Q:"))
        self.label_21.setText(_translate("MainWindow", "Name:"))
        self.pushButton_nav_nw.setText(_translate("MainWindow", "↖︎"))
        self.pushButton_nav_n.setText(_translate("MainWindow", "↑"))
        self.pushButton_nav_ne.setText(_translate("MainWindow", "↗︎"))
        self.pushButton_nav_w.setText(_translate("MainWindow", "←"))
        self.pushButton_nav_e.setText(_translate("MainWindow", "→"))
        self.pushButton_nav_sw.setText(_translate("MainWindow", "↙︎"))
        self.pushButton_nav_s.setText(_translate("MainWindow", "↓"))
        self.pushButton_nav_se.setText(_translate("MainWindow", "↘︎"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Parameters"))
        self.label_13.setText(_translate("MainWindow", "MHz"))
        self.label_15.setText(_translate("MainWindow", "MHz"))
        self.label_9.setText(_translate("MainWindow", "µA"))
        self.label_18.setText(_translate("MainWindow", "m"))
        self.checkBox_circum.setText(_translate("MainWindow", "Use circum."))
        self.label_10.setText(_translate("MainWindow", "Analysis Freq."))
        self.label_7.setText(_translate("MainWindow", "MeV/u"))
        self.label_4.setText(_translate("MainWindow", "Energy:"))
        self.label_11.setText(_translate("MainWindow", "MHz"))
        self.comboBox_ring.setItemText(0, _translate("MainWindow", "ESR"))
        self.comboBox_ring.setItemText(1, _translate("MainWindow", "CRYRING"))
        self.comboBox_ring.setItemText(2, _translate("MainWindow", "CR"))
        self.comboBox_ring.setItemText(3, _translate("MainWindow", "CSRe"))
        self.comboBox_ring.setItemText(4, _translate("MainWindow", "RIRING"))
        self.label_17.setText(_translate("MainWindow", "Ring:"))
        self.label_8.setText(_translate("MainWindow", "Beam Current:"))
        self.label_19.setText(_translate("MainWindow", "Path length:"))
        self.label_14.setText(_translate("MainWindow", "Unknown particle:"))
        self.label_12.setText(_translate("MainWindow", "Actual Freq."))
        self.groupBox_5.setTitle(_translate("MainWindow", "Actions"))
        self.pushButton_calculate.setText(_translate("MainWindow", "Calculate"))
        self.pushButton_table_data.setText(_translate("MainWindow", "Table Data"))
        self.pushButton_isotopes.setText(_translate("MainWindow", "Isotopes"))
        self.pushButton_isobars.setText(_translate("MainWindow", "Isobars"))
        self.pushButton_isotones.setText(_translate("MainWindow", "Isotones"))
        self.pushButton_identify.setText(_translate("MainWindow", "Identify"))
        self.pushButton_save.setText(_translate("MainWindow", "Save"))
        self.pushButton_clear.setText(_translate("MainWindow", "Clear"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Results Pane"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Results Table"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionLoad_Freqlist.setText(_translate("MainWindow", "Load Freq. List"))
        self.actionLoad_Freqlist.setShortcut(_translate("MainWindow", "Ctrl+L"))
        self.actionClear_results.setText(_translate("MainWindow", "Clear results"))
        self.actionClear_results.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionSave_results.setText(_translate("MainWindow", "Save results"))
        self.actionSave_results.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionAbout.setText(_translate("MainWindow", "About"))

