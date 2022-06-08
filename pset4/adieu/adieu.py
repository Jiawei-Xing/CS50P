import inflect

p = inflect.engine()

n = []
while True:
    try:
        n.append(input("Name: "))
    except EOFError:
        break

print("Adieu, adieu, to", p.join(n))