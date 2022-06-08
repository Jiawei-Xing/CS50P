import sys

if len(sys.argv) < 2:
    print("Too few command-line arguments")
    sys.exit(1)

if len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit(1)

if sys.argv[1][-3:] != ".py":
    print("Not a python file")
    sys.exit(1)

c = 0
try:
    f = open(sys.argv[1])
except FileNotFoundError:
    print("File does not exist")
    sys.exit(1)
else:
    for line in f:
        if line.strip() == '' or line.lstrip().startswith("#"):
            continue
        else:
            c += 1

f.close()
print(c)