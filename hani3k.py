# -*- coding: utf-8 -*-
from pandas import read_csv, Series  # , DataFrame


# todo: load file;
# todo: add user defined dict anytime;
# todo: export dict
# todo: add meaning to a word
# todo: 检测， 近义词表
# todo: choose list
# todo: 显示第几个单词
# todo: 单词乱序
# todo：创建个人学习日记，每个单词学习过几遍，在什么时候学的
# todo：提供学习表格
# todo: 分类选择，从未学习过的单词中选择单词
# todo：提供用户+密码的形式，访问学习记录，创建对应的 用户-密码-词书-学习记录
# todo: log file
class Engine:

    def __init__(self, _file_name="3000_new.csv"):
        # self.words.columns: ['repeat', 'word', 'meaning']
        self.quit = False
        self.words = read_csv(_file_name, sep="*", index_col=0)
        # print(self.words.columns)
        self.word2id = Series(self.words.index, index=self.words.word)
        self.help = "supported commands: help, all"

    @staticmethod
    def format_display(word, flag="word", box_wid=80):  # todo: what about the flag?
        word = word.split(";")
        print("+" + flag.center((box_wid - 1), "-") + "+")
        if len(word) == 1:
            print("|" + " " * (box_wid - 1) + "|")
            print("|" + word[0].center((box_wid - 1)) + "|")
            print("|" + " " * (box_wid - 1) + "|")
        elif len(word) >= 2:
            for i in range(len(word)):
                print("|" + word[i].center((box_wid - 1)) + "|")
        print("+" + "-" * (box_wid - 1) + "+")

    def run(self, _command):
        if _command == "q":
            self.quit = True
        elif _command == "help":
            print(self.help)
        elif _command == "all":
            self.start_recite()
        elif _command == "list":
            word_range = self.start_from_list()
            self.start_recite(_range=word_range)
        else:
            print("unrecognized command, please type again!")

    def start_from_list(self):
        list_break = 0
        while list_break == 0:
            word_start = int(input('please enter the start number: '))
            word_end = int(input('please enter the end number: '))
            if word_start > 0 & word_start <= word_end:
                list_break = 1
            else:
                list_break = 0
                print('please reenter the list range')
        _word_range = (word_start - 1, word_end)
        print("start from word", word_start, 'to word', word_end)
        return _word_range

    def start_recite(self, _range="all"):
        if _range == "all":
            words_range = self.words.index
        else:
            words_range = self.words.index[_range[0]: _range[1]]

        for key in words_range:
            self.format_display(self.words.loc[key, "word"])
            tmp = input("press enter to see meaning.$>>")
            if tmp == "q":
                self.quit = True
                break
            # print("meaning:\t" + self.words[key])
            self.format_display(self.words.loc[key, "meaning"], flag="meaning")
            tmp = input("print enter to continue")
            if tmp == "q":
                self.quit = True
                break

    def save_and_quit(self, _file_name="3000_new.csv"):
        self.words.to_csv(_file_name, sep="*", index=True, header=True)
        print("save finish")


if __name__ == "__main__":
    engine = Engine()
    while not engine.quit:
        command = input("type in your command.$>>")
        engine.run(command)
    else:
        engine.save_and_quit()
