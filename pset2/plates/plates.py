def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not s[:2].isalpha():
        return False

    if not s.isalnum():
        return False

    if len(s) > 6 or len(s) < 2:
        return False

    for n in s:
        # First number
        if n.isnumeric():
            if n == '0':
                return False
            break

    num=[]
    for i in range(len(s)):
        if s[i].isnumeric():
            num.append(i)

    if not num:
        return True
    elif num[-1] == len(s) - 1 and num[0] == len(s) - len(num):
        return True
    else:
        return False


main()