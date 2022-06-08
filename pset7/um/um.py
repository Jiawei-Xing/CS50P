import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    return len(re.findall(r"\b[uU][mM]\b", s))


if __name__ == "__main__":
    main()