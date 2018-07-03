# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_hanihani(object):
    def setupUi(self, hanihani):
        hanihani.setObjectName("hanihani")
        hanihani.resize(632, 405)
        self.layoutWidget = QtWidgets.QWidget(hanihani)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 0, 618, 398))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 5, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.info_browser = QtWidgets.QTextBrowser(self.layoutWidget)
        self.info_browser.setObjectName("info_browser")
        self.verticalLayout_3.addWidget(self.info_browser)
        self.word_browser = QtWidgets.QTextBrowser(self.layoutWidget)
        self.word_browser.setEnabled(True)
        self.word_browser.setObjectName("word_browser")
        self.verticalLayout_3.addWidget(self.word_browser)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 5)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.meaning_browser = QtWidgets.QTextBrowser(self.layoutWidget)
        self.meaning_browser.setObjectName("meaning_browser")
        self.verticalLayout_2.addWidget(self.meaning_browser)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.next_button = QtWidgets.QPushButton(self.layoutWidget)
        self.next_button.setObjectName("next_button")
        self.horizontalLayout.addWidget(self.next_button)
        self.star_button = QtWidgets.QPushButton(self.layoutWidget)
        self.star_button.setObjectName("star_button")
        self.horizontalLayout.addWidget(self.star_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.retranslateUi(hanihani)
        self.pushButton_2.clicked.connect(hanihani.show_meaning)
        self.next_button.clicked.connect(hanihani.next_word)
        self.star_button.clicked.connect(hanihani.star_word)
        QtCore.QMetaObject.connectSlotsByName(hanihani)

    def retranslateUi(self, hanihani):
        _translate = QtCore.QCoreApplication.translate
        hanihani.setWindowTitle(_translate("hanihani", "hani"))
        self.pushButton_2.setText(_translate("hanihani", "show"))
        self.next_button.setText(_translate("hanihani", "next"))
        self.star_button.setText(_translate("hanihani", "star"))

