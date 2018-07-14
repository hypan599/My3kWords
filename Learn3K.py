# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Learn3K.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Learn(object):
    def setupUi(self, Learn):
        Learn.setObjectName("Learn")
        Learn.resize(553, 441)
        self.layoutWidget = QtWidgets.QWidget(Learn)
        self.layoutWidget.setGeometry(QtCore.QRect(11, 10, 526, 381))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.word_browser = QtWidgets.QTextBrowser(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.word_browser.setFont(font)
        self.word_browser.setObjectName("word_browser")
        self.horizontalLayout_3.addWidget(self.word_browser)
        self.meaning_browser = QtWidgets.QTextBrowser(self.layoutWidget)
        self.meaning_browser.setObjectName("meaning_browser")
        self.horizontalLayout_3.addWidget(self.meaning_browser)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton, 0, QtCore.Qt.AlignTop)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2, 0, QtCore.Qt.AlignTop)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.info_browser = QtWidgets.QTextBrowser(self.layoutWidget)
        self.info_browser.setObjectName("info_browser")
        self.horizontalLayout_2.addWidget(self.info_browser)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(0, 5)
        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(Learn)
        self.pushButton_2.clicked.connect(Learn.next_word)
        self.pushButton_3.clicked.connect(Learn.show_meaning)
        self.pushButton.clicked.connect(Learn.star_word)
        QtCore.QMetaObject.connectSlotsByName(Learn)

    def retranslateUi(self, Learn):
        _translate = QtCore.QCoreApplication.translate
        Learn.setWindowTitle(_translate("Learn", "LearnWords"))
        self.pushButton.setText(_translate("Learn", "star"))
        self.pushButton_2.setText(_translate("Learn", "next"))
        self.pushButton_3.setText(_translate("Learn", "show"))

