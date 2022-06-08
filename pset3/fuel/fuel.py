while True:
    f = input("Fraction: ")
    try:
        x, y = f.split("/")
        p = int(x) / int(y) * 100
    except (ValueError, ZeroDivisionError):
        pass
    else:
        if int(x) > int(y):
            continue
        elif p < 1:
            print("E")
        elif p > 99:
            print("F")
        else:
            print(f"{round(p)}%")
        break
