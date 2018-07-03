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
        hanihani.resize(737, 398)
        self.layoutWidget = QtWidgets.QWidget(hanihani)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 731, 391))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.word_browser = QtWidgets.QTextBrowser(self.layoutWidget)
        self.word_browser.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.word_browser.setFont(font)
        self.word_browser.setObjectName("word_browser")
        self.horizontalLayout_3.addWidget(self.word_browser)
        self.meaning_browser = QtWidgets.QTextBrowser(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.meaning_browser.setFont(font)
        self.meaning_browser.setObjectName("meaning_browser")
        self.horizontalLayout_3.addWidget(self.meaning_browser)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.show_button = QtWidgets.QPushButton(self.layoutWidget)
        self.show_button.setObjectName("show_button")
        self.horizontalLayout.addWidget(self.show_button)
        self.next_button = QtWidgets.QPushButton(self.layoutWidget)
        self.next_button.setObjectName("next_button")
        self.horizontalLayout.addWidget(self.next_button)
        self.star_button = QtWidgets.QPushButton(self.layoutWidget)
        self.star_button.setObjectName("star_button")
        self.horizontalLayout.addWidget(self.star_button)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.info_browser = QtWidgets.QTextBrowser(self.layoutWidget)
        self.info_browser.setObjectName("info_browser")
        self.horizontalLayout_2.addWidget(self.info_browser)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(0, 9)
        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(hanihani)
        self.show_button.clicked.connect(hanihani.show_meaning)
        self.next_button.clicked.connect(hanihani.next_word)
        self.star_button.clicked.connect(hanihani.star_word)
        QtCore.QMetaObject.connectSlotsByName(hanihani)

    def retranslateUi(self, hanihani):
        _translate = QtCore.QCoreApplication.translate
        hanihani.setWindowTitle(_translate("hanihani", "hani"))
        self.show_button.setText(_translate("hanihani", "show"))
        self.next_button.setText(_translate("hanihani", "next"))
        self.star_button.setText(_translate("hanihani", "star"))

