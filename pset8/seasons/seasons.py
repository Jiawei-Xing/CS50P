from datetime import date
import sys
import inflect


def main():
    birthday = input("Date of Birth: ")
    try:
        d = date.fromisoformat(birthday)
    except ValueError:
        print("Invalid date")
        sys.exit(1)
    else:
        minutes = delta(d)
        print(f"{words(minutes).capitalize().replace(' and','')} minutes")


def delta(d):
    day = date.today() - d
    return day.days * 24 * 60


def words(n):
    p = inflect.engine()
    return p.number_to_words(n)


if __name__ == "__main__":
    main()