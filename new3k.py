from pandas import read_csv, Series  # , DataFrame
import json
import os
import platform


def get_system():
    curr_os = platform.system()
    if "darwin" in curr_os:
        return "mac"
    elif "windows" in curr_os:
        return "windows"
    elif "linux" in curr_os:
        return "linux"
    else:
        print(curr_os)
        raise ValueError("Unknown system!")


def my_center(s, wid=80, char=" "):
    length = len(s)
    num_chn = 0
    for i in s:
        if '\u4e00' <= i <= '\u9fff':
            num_chn += 1
    left_space = (wid - length - num_chn) // 2
    right_space = wid - length - num_chn - left_space
    return char * left_space + s + right_space * char


class App:

    def __init__(self):
        self.state = "main"
        self.file_prefix = ""
        self.menu = ["学习 L", "复习 R", "游戏 G", "选择词书 S"]
        self.menu_title = "主菜单"
        self.words = None

    def if_file(self):
        if self.file_prefix:
            return True
        return False

    def main_menu(self):
        while True:
            self.display_menu()
            _cmd = input("请输入命令对应的字母 >>")
            if _cmd and _cmd in "LRGSQlrgsq":
                return _cmd

    def display_menu(self, title="", menu=[], box_wid=80, box_height=14):
        if not menu:
            menu = self.menu
        if not title:
            title = self.menu_title
        args_len = len(menu)
        empty_num = box_height - args_len * 2 - 2

        print("+" + title.center(box_wid, "-") + "+")
        for i in range(empty_num):
            print("|" + " " * box_wid + "|")
        for arg in list((*menu, "退出 Q")):
            print("|" + str(arg).center(box_wid, " ") + "|")
            print("|" + " " * box_wid + "|")

        print("|" + "-" * box_wid + "|")

    def format_display(self, key, n, left_n, label="word", box_wid=80, title=""):  # todo: what about the flag?
        box_wid = box_wid // 2 * 2
        if label == "word":
            contents = [self.words.loc[key, label]]
        else:
            meaning = self.words.loc[key, "modified"] if self.words.loc[key, "modified"] else self.words.loc[key, label]
            contents = meaning.split(";")

        print("+" + my_center(title, char="-") + "+")
        for i in range(5 - len(contents)):
            print("|" + " " * box_wid + "|")
        for i in contents:
            print("|" + my_center(i) + "|")
        print("|" + ("L%dU%d" % (key // 100 + 1, key // 10 % 10 + 1)).ljust(box_wid // 2) + (
                "星标: %s" % self.words.loc[key, "star"]).rjust(box_wid // 2) + "|")
        print("|" + ("已背: %d" % n).ljust(box_wid // 2) + (
                "编辑: %s" % self.words.loc[key, "modify_flag"]).rjust(box_wid // 2) + "|")
        print("|" + ("剩余: %d" % left_n).ljust(box_wid // 2) + (
                "备注: %s" % bool(self.words.loc[key, "remarks"])).rjust(box_wid // 2) + "|")
        print("+" + "-" * box_wid + "+")

    def change_state(self, new_state):
        self.state = new_state

    def change_file(self, new_file):
        self.file_prefix = new_file

    def change_setting(self):
        if not self.file_prefix:
            print("当前词书： 无")
        else:
            print("当前词书: %s.csv" % self.file_prefix)
        new_prefix = input("请输入词书（输入 d 以使用默认词书， q以退出） >>")
        if new_prefix == "q":
            print("无改变返回主菜单")
            return
        elif new_prefix in ["default", "d"]:
            self.file_prefix = "default_3000"
        else:
            self.file_prefix = new_prefix
        print("切换到 %s.csv\n返回主菜单" % self.file_prefix)

    def close(self):
        print("leaving...Good Bye!")
        self.state = "quit"


class LearnApp(App):
    def __init__(self):
        super().__init__()
        with open(self.file_prefix + ".config", "r", encoding="utf8") as f:
            self.config = json.load(f)
        with open(self.file_prefix + ".log", "r", encoding="utf8") as f:
            self.log = json.load(f)
        self.words = read_csv(self.file_prefix + ".csv", sep="*", index_col=0, header=0)


class ReviewApp(App):
    def __init__(self, prefix):
        super().__init__()
        self.menu = ["依列表选择 L", "依星标选择 R", "依次数选择 N", "选项设置 S"]
        self.menu_title = "主菜单：复习模式"
        with open(prefix + ".config", "r", encoding="utf8") as f:
            self.config = json.load(f)
        with open(prefix + ".log", "r", encoding="utf8") as f:
            self.log = json.load(f)
        self.words = read_csv(prefix + ".csv", sep="*", index_col=0, header=0)
        self.words.fillna("", inplace=True)

    def change_setting(self):
        leave = False
        while not leave:
            self.display_menu(title="review settings", menu=list(self.config.keys()))
            _cmd = input("请输入命令对应的字母 >>")
            if _cmd in "OoRrQq":
                if _cmd.lower() == "q":
                    leave = True
                elif _cmd.lower() == "o":
                    print("wait...")  # todo : date offset
                elif _cmd.lower() == "r":
                    print("wait...")  # todo: random settings

    def main_menu(self):
        leave = False
        while not leave:
            self.display_menu()
            _cmd = input("请输入命令对应的字母 >>")
            if _cmd in "LSNQRlsnqr":
                if _cmd.lower() == "q":
                    leave = True
                elif _cmd.lower() == "s":
                    self.change_setting()
                elif _cmd.lower() == "l":
                    lists = [int(i) for i in input("请输入list的序号，空格分隔 >>").split()]
                    self.start([((i - 1) * 100, i * 100) for i in lists])
                elif _cmd.lower() == "r":
                    pass
                elif _cmd.lower() == "n":
                    pass

    def start(self, lists):
        def iter_words():
            total_num = 0
            for s, e in lists:
                total_num += e - s
            count = 0
            for s, e in lists:
                for i in range(s, e):
                    count += 1
                    # self.config["last_loc"] = i
                    yield i, count, total_num - count

        _cmd = None
        for key, n, left in iter_words():
            for l, t in zip(["word", "meaning"], ["单词", "释义"]):
                self.format_display(key, n, left, label=l, title=t)
                _cmd = input("按 q 退出，回车继续")
                if _cmd == "q":
                    break
            if _cmd == "q":
                break
        print("finish")


class GameApp(App):
    def __init__(self):
        super().__init__()
        with open(self.file_prefix + ".config", "r", encoding="utf8") as f:
            self.config = json.load(f)
        with open(self.file_prefix + ".log", "r", encoding="utf8") as f:
            self.log = json.load(f)
        self.words = read_csv(self.file_prefix + ".csv", sep="*", index_col=0, header=0)


if __name__ == "__main__":
    print("系统正在启动...")
    app = App()
    cmd = app.main_menu()
    while cmd:
        if cmd.lower() == "r":
            if app.if_file():
                review = ReviewApp(app.file_prefix)
                review.main_menu()
            else:
                print("当前无词书，请先设置词书")
        elif cmd.lower() == "l":
            if app.if_file():
                learn = LearnApp()
                learn.main_menu()
            else:
                print("当前无词书，请先设置词书")
                continue
        elif cmd.lower() == "g":
            if app.if_file():
                game = GameApp()
                game.main_menu()
            else:
                print("当前无词书，请先设置词书")
                continue
        elif cmd.lower() == "s":
            app.change_setting()
        elif cmd.lower() == "q":  # only way to leave while loop
            app.close()
            break
        cmd = app.main_menu()
