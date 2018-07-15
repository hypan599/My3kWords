from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QMessageBox, QMainWindow
from hani3K import Ui_hani3K
import sys
import random
import time
import pandas as pd


class MainWindow(QMainWindow, Ui_hani3K):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.all_words = None
        self.word_seq = None
        self.total_len = 0
        self.word = ""
        self.meaning = ""
        self.current_pointer = 0
        self.star = False
        self.known = False
        self.show_meaning_flag = False
        self.number_left = 0
        self.learning = False

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', 'You sure to quit?\nChanges will be lost.',
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.Yes)

        if reply == QMessageBox.Yes:
            # add things here
            event.accept()
        else:
            event.ignore()

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_D or e.key() == QtCore.Qt.Key_Right:
            self.next_word()
        elif e.key() == QtCore.Qt.Key_S or e.key() == QtCore.Qt.Key_Down:
            self.show_meaning()
        elif e.key() == QtCore.Qt.Key_W or e.key() == QtCore.Qt.Key_Up:
            self.star_word()
        elif e.key() == QtCore.Qt.Key_A or e.key() == QtCore.Qt.Key_Left:
            self.set_known_word()

    def use_default(self):
        self.word_book.setText("default_3000.csv")

    def load_book(self):
        if not self.word_book.text():
            self.book_info.setText("please choose book first")
        else:
            try:
                self.all_words = pd.read_csv(self.word_book.text(), sep="*", index_col=0, header=0)
                self.book_info.setText("load file:\n%s\nfinish!" % self.word_book.text())
            except FileNotFoundError:
                self.book_info.setText("file not found! please try again")
        self.from_bsr.setText("1")
        self.to_bsr.setText("10")
        self.word_bsr.setText(self.learn_type.currentText())

    def start_learn(self):
        self.word_bsr.setFocus()
        if self.learn_type.currentText() == "Star":
            self.book_info.setText("not implemented! Try again")
        elif self.learn_type.currentText() == "Unknown":
            self.book_info.setText("not implemented! Try again")
        else:
            start_pos = int(self.from_bsr.text())
            end_pos = int(self.to_bsr.text())
            if start_pos > end_pos or end_pos >= self.all_words.shape[0]:
                self.book_info.setText("invlaid range!")
                return
            self.word_seq = self.all_words.loc[start_pos - 1:end_pos, :]
            self.total_len = end_pos - start_pos + 1
        self.learning = True
        self.next_word()

    def refresh(self):
        self.word_bsr.setText(self.word)
        self.word_bsr.setAlignment(QtCore.Qt.AlignCenter)
        self.meaning_bsr.setText(self.meaning if self.show_meaning_flag else "")
        self.meaning_bsr.setAlignment(QtCore.Qt.AlignCenter)
        self.log_bsr.setText("Current at:\n%s\n%s\nLeft: %d/%d\n" % ("Star" if self.star else "no star",
                                                                     "Known" if self.known else "unknown",
                                                                     self.number_left, self.total_len))

    def save_log(self):
        pass

    def next_word(self):
        if not self.learning:
            return
        try:
            self.star = False
            self.known = False
            self.word, self.meaning = self.word_seq.iloc[self.current_pointer, :]
            self.number_left = self.word_seq.shape[0] - self.current_pointer - 1
            self.refresh()
            self.current_pointer += 1

        except IndexError:
            self.finish()

    def show_meaning(self):
        if self.learning:
            self.show_meaning_flag = not self.show_meaning_flag
            self.refresh()

    def star_word(self):
        if self.learning:
            self.star = not self.star
            self.refresh()

    def finish(self):
        self.word_bsr.setText("finish!")
        self.word_bsr.setAlignment(QtCore.Qt.AlignCenter)
        self.meaning_bsr.setText("")
        self.log_bsr.setText("")
        self.learning = False

    def set_known_word(self):
        if self.learning:
            self.known = not self.known
            self.refresh()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

