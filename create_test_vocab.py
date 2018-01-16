import string
import random


def main(outfile, n=100):
    with open(outfile, "w") as f:
        f.write("#\tword\tmeaning\n")
        for i in range(n):
            f.write("%s\t%s\n" % ("".join([random.choice(string.ascii_uppercase) for _ in range(random.randint(3, 5))]),
                                  "".join(
                                      [random.choice(string.ascii_lowercase) for _ in range(random.randint(4, 8))])))


if __name__ == "__main__":
    main("words.txt")
