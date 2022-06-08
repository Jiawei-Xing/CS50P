m = 50

while m > 0:
    print(f"Amount Due: {m}")
    n = int(input("Insert Coin: "))
    if n == 25 or n == 10 or n == 5:
        m -= n

print("Change Owed: " + str(abs(m)))