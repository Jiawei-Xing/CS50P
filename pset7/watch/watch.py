import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    match = re.search(r'"https?://(www\.)?youtube\.com/embed/(\w+)"', s)
    if not match:
        return None

    return "https://youtu.be/" + match.group(2)


if __name__ == "__main__":
    main()