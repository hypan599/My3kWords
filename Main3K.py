# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main3K.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Main_window(object):
    def setupUi(self, Main_window):
        Main_window.setObjectName("Main_window")
        Main_window.resize(509, 316)
        self.centralwidget = QtWidgets.QWidget(Main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 471, 235))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.list_box = QtWidgets.QSpinBox(self.layoutWidget)
        self.list_box.setMinimum(1)
        self.list_box.setProperty("value", 1)
        self.list_box.setObjectName("list_box")
        self.horizontalLayout_2.addWidget(self.list_box)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.unit_box = QtWidgets.QSpinBox(self.layoutWidget)
        self.unit_box.setMinimum(1)
        self.unit_box.setMaximum(10)
        self.unit_box.setObjectName("unit_box")
        self.horizontalLayout_2.addWidget(self.unit_box)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 1)
        self.horizontalLayout_2.setStretch(3, 1)
        self.horizontalLayout_2.setStretch(4, 4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.checkBox = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout.addWidget(self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout.addWidget(self.checkBox_3)
        self.checkBox_4 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout.addWidget(self.checkBox_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.checkBox_5 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_5.setObjectName("checkBox_5")
        self.horizontalLayout_3.addWidget(self.checkBox_5)
        self.review_box = QtWidgets.QSpinBox(self.layoutWidget)
        self.review_box.setMinimum(1)
        self.review_box.setMaximum(10)
        self.review_box.setObjectName("review_box")
        self.horizontalLayout_3.addWidget(self.review_box)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2, 0, QtCore.Qt.AlignBottom)
        Main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 509, 22))
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        Main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Main_window)
        self.statusbar.setObjectName("statusbar")
        Main_window.setStatusBar(self.statusbar)
        self.actionAbout_me = QtWidgets.QAction(Main_window)
        self.actionAbout_me.setCheckable(True)
        self.actionAbout_me.setObjectName("actionAbout_me")
        self.actionguanbo = QtWidgets.QAction(Main_window)
        self.actionguanbo.setObjectName("actionguanbo")
        self.menuAbout.addAction(self.actionAbout_me)
        self.menuAbout.addAction(self.actionguanbo)
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(Main_window)
        self.pushButton.clicked.connect(Main_window.load_word_book)
        self.checkBox.stateChanged['int'].connect(Main_window.random)
        self.checkBox_2.stateChanged['int'].connect(Main_window.shuffle)
        self.checkBox_3.stateChanged['int'].connect(Main_window.fast_review)
        self.checkBox_4.stateChanged['int'].connect(Main_window.star_only)
        self.pushButton_3.clicked.connect(Main_window.load_default)
        self.checkBox_5.clicked.connect(Main_window.set_review)
        QtCore.QMetaObject.connectSlotsByName(Main_window)

    def retranslateUi(self, Main_window):
        _translate = QtCore.QCoreApplication.translate
        Main_window.setWindowTitle(_translate("Main_window", "MainWindow"))
        self.label.setText(_translate("Main_window", "Choose Config"))
        self.pushButton.setText(_translate("Main_window", "Load"))
        self.pushButton.setShortcut(_translate("Main_window", "L"))
        self.pushButton_3.setText(_translate("Main_window", "Default"))
        self.label_2.setText(_translate("Main_window", "Start from List: "))
        self.label_3.setText(_translate("Main_window", "Unit: "))
        self.checkBox.setText(_translate("Main_window", "Random"))
        self.checkBox_2.setText(_translate("Main_window", "In-group shuffle"))
        self.checkBox_3.setText(_translate("Main_window", "Fast Review"))
        self.checkBox_4.setText(_translate("Main_window", "Stared Words Only"))
        self.checkBox_5.setText(_translate("Main_window", "Review every"))
        self.label_4.setText(_translate("Main_window", "list"))
        self.pushButton_2.setText(_translate("Main_window", "START LEARN"))
        self.menuAbout.setTitle(_translate("Main_window", "About"))
        self.actionAbout_me.setText(_translate("Main_window", "About me"))
        self.actionAbout_me.setShortcut(_translate("Main_window", "Ctrl+/"))
        self.actionguanbo.setText(_translate("Main_window", "guanbo"))

