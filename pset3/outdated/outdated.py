months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


while True:
    date = input("Date: ")
    try:
        m, d, y = map(int, date.split("/"))
    except ValueError:

        try:
            m, d, y = date.split()
            m = int(months.index(m) + 1)
            d = int(d[:-1])
            y = int(y)
        except (ValueError, IndexError):
            continue

    if 1 <= m <= 12 and 1 <= d <= 31:
        print(f"{y:04}-{m:02}-{d:02}")
        break