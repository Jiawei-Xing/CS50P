def main():
    time = input("What time is it? ").strip()
    h = convert(time)
    if 7 <= h <= 8:
        print("breakfast time")
    elif 12 <= h <= 13:
        print("lunch time")
    elif 18 <= h <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = map(int, time.split(" ")[0].split(":"))

    if time[-4:] == 'p.m.':
        hours += 12

    return hours + minutes / 60

if __name__ == "__main__":
    main()