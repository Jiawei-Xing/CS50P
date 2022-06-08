import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if match := re.search(r"([0-9]+):([0-9]+) ([AP]M) to ([0-9]+):([0-9]+) ([AP]M)", s):
        a = int(match.group(1))
        b = int(match.group(2))
        m = match.group(3)
        c = int(match.group(4))
        d = int(match.group(5))
        n = match.group(6)
    elif match := re.search(r"([0-9]+) ([AP]M) to ([0-9]+) ([AP]M)", s):
        a = int(match.group(1))
        b = 0
        m = match.group(2)
        c = int(match.group(3))
        d = 0
        n = match.group(4)
    else:
        raise ValueError

    # valid hour and minute
    if not (0 < a < 13) or not (0 < c < 13):
        raise ValueError
    if not (0 <= b < 60) or not (0 <= d < 60):
        raise ValueError

    # 12 AM to 0
    if a == 12 and m == 'AM':
        a = 0
    if c == 12 and n == 'AM':
        c = 0

    # PM adds 12
    if a != 12 and m == 'PM':
        a += 12
    if c != 12 and n == 'PM':
        c += 12

    return f"{a:02}:{b:02} to {c:02}:{d:02}"


if __name__ == "__main__":
    main()