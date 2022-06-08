from random import randint

while True:
    try:
        l = int(input("Level: "))
    except ValueError:
        pass
    else:
        if l <= 0:
            pass
        else:
            r = randint(1, l)
            break

while True:
    try:
        n = int(input("Guess: "))
    except ValueError:
        pass
    else:
        if n <= 0:
            pass
        elif n < r:
            print("Too small!")
        elif n > r:
            print("Too large!")
        else:
            print("Just right!")
            break
