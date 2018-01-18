# -*- coding: utf-8 -*-
from pandas import read_csv, Series  # , DataFrame
import json


# todo: load file;
# todo: add user defined dict anytime;
# todo: export dict
# todo: add meaning to a word
# todo: 检测， 近义词表
# todo: choose list
# todo: log file
class Engine:

    def __init__(self, _file_name="3000_new.csv", _config_file_name="config.json"):
        # init properties
        self.quit = False
        self.mode = "Learn"
        self.help = "supported commands: help, all"
        # load words # words.columns: ['repeat', 'word', 'meaning']
        self.words = read_csv(_file_name, sep="*", index_col=0)
        self.word2id = Series(self.words.index, index=self.words.word)

        # load config file
        self.config_file_name = _config_file_name
        with open(self.config_file_name, "r") as f:
            self.config = json.load(f)



    @staticmethod
    def format_display(word, flag="word", box_wid=80):  # todo: what about the flag?
        def my_center(s, wid=box_wid, char=" "):
            length = len(s)
            num_chn = 0
            for i in s:
                if '\u4e00' <= i <= '\u9fff':
                    num_chn += 1
            left_space = (wid - length - num_chn) // 2
            right_space = wid - length - num_chn - left_space
            return char * left_space + s + right_space * char

        word = word.split(";")
        print("+" + my_center(flag, char="-") + "+")
        if len(word) == 1:
            print("|" + " " * box_wid + "|")
            print("|" + my_center(word[0]) + "|")
            print("|" + " " * box_wid + "|")
        elif len(word) >= 2:
            for i in range(len(word)):
                print("|" + my_center(word[i]) + "|")
        print("+" + "-" * box_wid + "+")

    def run(self, _command):
        if _command == "q":
            self.quit = True
        elif _command == "help":
            print(self.help)
        elif _command == "all":
            self.start_recite()
        elif _command == "list":
            word_range = self.start_from_list()
            self.start_recite(word_range)
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
            tmp = input("Press ENTER to continue. >>")
            if tmp == "q":
                self.quit = True
                break
            # print("meaning:\t" + self.words[key])
            self.format_display(self.words.loc[key, "meaning"], flag="meaning")
            tmp = input("Press ENTER to continue. >>")
            if tmp == "q":
                self.quit = True
                break

    def save_and_quit(self, _file_name="3000_new.csv"):
        self.words.to_csv(_file_name, sep="*", index=True, header=True)
        with open(self.config_file_name, "w") as f:
            json.dump(self.config, f)
        print("save finish")


if __name__ == "__main__":
    engine = Engine()
    while not engine.quit:
        command = input("Enter command or type h to see help. >>")
        engine.run(command)
    else:
        engine.save_and_quit()
