def main():
    fraction = input("Fraction: ")
    percentage = convert(f)
    print(gauge(round(percentage)))

def convert(fraction):
    try:
        x, y = fraction.split("/")
        percentage = int(x) / int(y) * 100
    except ValueError:
        raise ValueError
    except ZeroDivisionError:
        raise ZeroDivisionError
    else:
        return percentage

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage) + "%"