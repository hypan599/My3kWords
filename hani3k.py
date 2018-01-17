# -*- coding: utf-8 -*-
from pandas import read_csv, Series  # , DataFrame


# todo: hh
# todo: choose list
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
        else:
            print("uncognized command, please type again!")

    def start_recite(self, _range="all"):
        for key in self.words.index:
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
