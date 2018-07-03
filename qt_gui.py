from PyQt5 import QtWidgets, QtGui
from untitled import Ui_hanihani
import sys
import pandas as pd


class MyWindow(QtWidgets.QWidget, Ui_hanihani):
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
        self.meaning_browser.setPlainText("祝你学习愉快")
        self.info_browser.setPlainText("当前词书：%s" % self.file)
        self.word_browser.setPlainText(_help)

    def refresh(self):
        self.info_browser.setText("当前词书：%s\nList: %d, Group: %d, Star: %s" %
                                  (self.file,
                                   self.curr_dict["list"],
                                   self.curr_dict["group"],
                                   "True" if self.curr_dict["star"] else "False"))
        self.word_browser.setText(self.curr_dict["word"])
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
            self.curr_dict["word"] = self.words.loc[self.counter, "word"]
            self.curr_dict["meaning"] = "\n".join(self.words.loc[self.counter, "meaning"].split(";"))
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


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    myshow = MyWindow()
    myshow.show()
    sys.exit(app.exec_())
