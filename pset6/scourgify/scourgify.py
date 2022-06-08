import csv
import sys

if len(sys.argv) < 3:
    print("Too few command-line arguments")
    sys.exit(1)

if len(sys.argv) > 3:
    print("Too many command-line arguments")
    sys.exit(1)

if sys.argv[1][-4:] != ".csv":
    print("Not a csv file")
    sys.exit(1)

try:
    f = open(sys.argv[1])
except FileNotFoundError:
    print(f"Could not read {sys.argv[1]}")
    sys.exit(1)
else:
    d_old = csv.DictReader(f)
    d_new = []
    for each in d_old:
        last, first = each["name"].split(", ")
        d_new.append({"first": first, "last": last, "house": each["house"]})
f.close()

with open(sys.argv[2], 'w', newline='') as outf:
    writer = csv.DictWriter(outf, fieldnames=['first', 'last', 'house'])
    writer.writeheader()
    for each in d_new:
        writer.writerow(each)
