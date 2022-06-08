import csv
import tabulate
import sys

if len(sys.argv) < 2:
    print("Too few command-line arguments")
    sys.exit(1)

if len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit(1)

if sys.argv[1][-4:] != ".csv":
    print("Not a csv file")
    sys.exit(1)

try:
    f = open(sys.argv[1])
except FileNotFoundError:
    print("File does not exist")
    sys.exit(1)
else:
    d = csv.DictReader(f)
    print(tabulate.tabulate(d, headers="keys", tablefmt="grid"))