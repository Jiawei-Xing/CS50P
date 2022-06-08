x, y, z = input("Expression: ").strip().split(" ")
x = int(x)
z = int(z)

if y == '+':
    r = x + z
elif y == '-':
    r = x - z
elif y == '*':
    r = x * z
elif y == '/':
    if z != 0:
        r = x / z
    else:
        print("Error: divisor must not be 0.")
else:
    print("Error: cannot recognize the expression.")

if r:
    print("%.1f" % (r))