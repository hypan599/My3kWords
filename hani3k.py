# -*- coding: utf-8 -*-

# todo: log file
class Engine:

    def __init__(self, _file_name="words.txt"):

        def read_words():
            _words = {}
            _repeat = {}
            with open(_file_name, "r") as f:
                for line in f:
                    if line[0] == "#":
                        continue
                    word, meaning = line.strip().split()
                    _words[word] = meaning
                    _repeat[word] = 0
            return _words, _repeat

        self.quit = False
        self.words, self.repeat_times = read_words()
        self.help = "supported commands: help, all"


    def run(self, _command):
        if _command == "help":
            print(self.help)
        elif _command == "all":
            self.start_recite()
        else:
            print("uncognized command, please type again!")

    def format_input(self, word, flag = "next-word"):
        print("+" + flag.center(18, "-") + "+")
        print("|" + " " * 18 + "|")
        print("|" + word.center(18) + "|")
        print("|" + " " * 18 + "|")
        print("+" + "-" * 18 + "+")

    def start_recite(self, _range="all"):
        for key in self.words:
            self.format_input(key)
            remember = input("press enter to see meaning.$>>")
            if remember == "q":
                exit(1)
            # print("meaning:\t" + self.words[key])
            self.format_input(self.words[key], "meaning")
            _ = input("print enter to continue")


if __name__ == "__main__":
    file = "words.txt"
    engine = Engine(file)
    while not engine.quit:
        command = input("type in your command.$>>")
        engine.run(command)

