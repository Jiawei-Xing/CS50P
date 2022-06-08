from random import randint


def main():
    level = get_level()
    score = 0
    for _ in range(10):
        x, y = generate_integer(level)
        flag = 0
        for _ in range(3):
            try:
                a = int(input(f"{x} + {y} = "))
            except ValueError:
                print("EEE")
            else:
                if a == x + y:
                    flag = 1
                    break
                else:
                    print("EEE")

        # Not correct after three times
        if not flag:
            print(f"{x} + {y} = {x+y}")
        score += flag
    print(f"Score: {score}")


def get_level():
    while True:
        level = input("Level: ")
        if level == '1' or level == '2' or level == '3':
            break
    return int(level)


def generate_integer(level):
    if level == 1:
        x = randint(0, 9)
        y = randint(0, 9)
    elif level == 2:
        x = randint(10, 99)
        y = randint(10, 99)
    elif level == 3:
        x = randint(100, 999)
        y = randint(100, 999)
    else:
        raise ValueError
    return x, y


if __name__ == "__main__":
    main()