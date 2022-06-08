import re
import sys


def main():
    if len(sys.argv) > 1:
        sys.exit(1)
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    match = re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip)
    if not match:
        return False

    numbers = list(map(int, ip.split(".")))
    if all(map(lambda n: 0 <= n <= 255, numbers)):
        return True
    else:
        return False


if __name__ == "__main__":
    main()