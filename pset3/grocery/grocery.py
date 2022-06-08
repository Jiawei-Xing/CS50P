d = {}

while True:
    try:
        item = input().upper()
    except EOFError:
        print()
        break
    else:
        if item in d:
            d[item] += 1
        else:
            d[item] = 1

for k, v in sorted(d.items()):
    print(int(v), k)