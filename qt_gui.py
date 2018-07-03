from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QMessageBox
from untitled import Ui_hanihani
import sys
import pandas as pd
# todo: menu bar
# todo: status bar
# todo: keyboard listening

class MyWindow(QWidget, Ui_hanihani):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.file = "default_3000.csv"
        self.words = pd.read_csv(self.file, sep="*", index_col=0, header=0)
        self.curr_dict = {}
        self.init_display()
        self.counter = 0
        self.meaning_flag = False

    def init_display(self):
        _help = """使用方法：默认已自动加载词书，可以直接进入学习。
有需求／bug 欢迎提交至邮箱： hanyingpan@gmail.com。
我会不定期删除这些邮件 ^_^"""
        self.meaning_browser.setPlainText(_help)
        self.info_browser.setPlainText("当前词书：%s" % self.file)
        self.word_browser.setPlainText("按next开始")

    def refresh(self):
        self.info_browser.setText("List: %d, Group: %d, Number: %d, Star: %s\n当前词书：%s" %
                                  (self.curr_dict["list"],
                                   self.curr_dict["group"],
                                   self.curr_dict["number"],
                                   "True" if self.curr_dict["star"] else "False",
                                   self.file))
        self.word_browser.setText(self.curr_dict["word"])
        self.word_browser.setAlignment(QtCore.Qt.AlignCenter)
        self.meaning_browser.setText(self.curr_dict["meaning"] if self.meaning_flag else "")

    def finish(self):
        pass

    def show_meaning(self):
        self.meaning_flag = True
        self.refresh()

    def next_word(self):
        try:
            self.curr_dict["list"] = self.counter / 100 + 1
            self.curr_dict["group"] = (self.counter / 10) % 10 + 1
            self.curr_dict["number"] = self.counter % 10 + 1
            self.curr_dict["word"] = self.words.loc[self.counter, "word"]
            self.curr_dict["meaning"] = "\n".join(["%d. %s" % (i+1, j) for i, j in
                                                   enumerate(self.words.loc[self.counter, "meaning"].split(";"))])
            self.curr_dict["star"] = self.words.loc[self.counter, "star"]
            self.counter += 1
            if self.meaning_flag:
                self.meaning_flag = False
            self.refresh()
        except KeyError:
            self.finish()

    def star_word(self):
        self.curr_dict["star"] = not self.curr_dict["star"]
        self.refresh()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', 'You sure to quit?',
                                               QMessageBox.Yes | QMessageBox.No,
                                               QMessageBox.No)

        if reply == QMessageBox.Yes:
            # todo: deal with vocab post process here
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myshow = MyWindow()
    myshow.show()
    sys.exit(app.exec_())
