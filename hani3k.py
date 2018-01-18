# -*- coding: utf-8 -*-
from pandas import read_csv, Series  # , DataFrame
import json


# todo: load file;
# todo: add user defined dict anytime;
# todo: export dict
# done: add meaning to a word
# todo: 检测， 近义词表
# done: choose list
# done: log file

class Engine:

    def __init__(self, _file_name="3000_new.csv"):
        # init properties
        self.quit = False
        self.mode = "Learn"
        self.help = "supported commands: help, chmod"
        self.file_name = _file_name
        # load config file
        with open(self.file_name, "r") as f:
            self.config = json.loads(f.readline())

        # load words # words.columns: repeat, star, modify_flag, word, meaning, modified, remarks

        self.words = read_csv(self.file_name, sep="*", index_col=0, skiprows=2, header=0)
        self.word2id = Series(self.words.index, index=self.words[["word"]])

    @staticmethod
    def ask_for_range():
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

    @staticmethod
    def format_display(word, left_n, flag="word", box_wid=80):  # todo: what about the flag?
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

    def show_prompt(self):
        if self.mode == "Learn":
            return "MODE: Learn. Choose list to learn."
        elif self.mode == "Review":
            return "MODE: Review. Choose list to review."
        elif self.mode == "Game":
            return "MODE: Game. DO NOT play game while learning. haha."
        elif self.mode == "Debug":
            return "Welcome to debug mode, Good Luck."
        else:
            return "Type in your command."

    def run(self, _command):
        _command = _command.strip()
        if " " not in _command:
            if _command == "q":
                self.quit = True
            elif _command == "h":
                print(self.help)
            elif _command == "a":
                self.review(_all=True)
            elif _command in ["r", "range"]:
                word_range = self.ask_for_range()
                self.review(_range=word_range)
            elif _command == "D":
                self.debug()
            else:
                print("unrecognized command, please type in again!")
        else:
            cmd, content = _command.split(" ", 1)
            if cmd == "chmod":
                if content in ["Learn", "Review", "Debug", "Game"]:
                    self.mode = content
                else:
                    print("invalid mode, type again!")
            elif cmd in ["l", "list"]:
                lists = [int(i) for i in content.split(" ")]
                self.review(_lists=lists)
            else:
                print("unrecognized command, please type again!")

    def debug(self):
        while True:
            _cmd = input("You are in debug mode, type in a command >>")
            if _cmd == "show_config":
                print(self.config)
            elif _cmd == "add_config":
                _key = input("type in a config key: >>")
                _value = input("type in a config value: >>")
                if input("add %s : %s to config. continue? y/[n]") == "y":
                    self.config[_key] = _value  # todo: ``how to use
            elif _cmd == "quit":
                print("quit debug mode")
                break

    def review(self, _range=None, _all=False, _lists=None, _hist=None):
        def iter_words():
            iter_lists = []
            total_num = 0
            if _all:
                iter_lists.append((0, self.words.shape[0]))
                total_num = self.words.shape[0]
            elif _lists:
                for _l in _lists:
                    iter_lists.append(((_l - 1) * 100, _l * 100))
                    total_num += 100
            elif _range:
                iter_lists.append(_range)
                total_num += _range[1] - _range[0]
            self.config["last_lists"] = iter_lists
            self.config["last_total"] = total_num

            for s, e in iter_lists:
                for i in range(s, e):
                    self.config["last_loc"] = i
                    yield i, total_num - i

        for key, left in iter_words():
            self.format_display(self.words.loc[key, "word"], left)
            _quit = False
            while not _quit:
                cmd = input("Press ENTER to continue. >>")
                if cmd == "q":
                    self.quit = True
                    _quit = True
                elif cmd == "s":
                    print("mmmmm")
                    _quit = True
                elif cmd == "h":
                    print("s: star, h: show this help")
                elif not cmd:
                    _quit = True
            if self.quit:
                break
            # print("meaning:\t" + self.words[key])
            self.format_display(self.words.loc[key, "meaning"], left, flag="meaning")
            _quit = False
            while not _quit:
                cmd = input("Press ENTER to continue. >>")
                if cmd == "q":
                    self.quit = True
                    _quit = True
                elif cmd == "m":
                    new_meaning = input("type in new meaning >>")
                    while True:
                        mode = input("select one mode: (a)ppend or (r)eplace or re(e)nter")
                        if mode in ["append", "a"]:
                            self.words.loc[key, "modified"] = self.words.loc[key, "meaning"] + new_meaning
                            self.words.loc[key, "modify_flag"] = True
                            print("append successful")
                            break
                        elif mode in ["replace", "r"]:
                            self.words.loc[key, "modified"] = new_meaning
                            self.words.loc[key, "modify_flag"] = True
                            print("replace successful")
                            break
                        elif mode in ["e", "reenter"]:
                            new_meaning = input("type in new meaning >>")
                elif cmd == "s":
                    if self.words.loc[key, "star"]:
                        self.words.loc[key, "star"] = False
                        print("unstared word %s" % self.words.loc[key, "word"])
                    else:
                        self.words.loc[key, "star"] = True
                        print("stared word %s" % self.words.loc[key, "word"])
                elif cmd == "h":
                    print("m: modify, s: star, h: show this help")
                elif not cmd:
                    _quit = True
            if self.quit:
                break

        if not self.quit:
            print("congratulations! you finished those words!")

    def save_and_quit(self):
        with open(self.file_name, "w") as f:
            f.write(json.dumps(self.config))
            f.write("\n\n")
        self.words.to_csv(self.file_name, mode="a", sep="*", index=True, header=True)
        print("Save finish.\nBye Bye")


if __name__ == "__main__":
    engine = Engine()
    while not engine.quit:
        command = input(engine.show_prompt() + " >>")
        engine.run(command)
    else:
        engine.save_and_quit()
