camel = input("camelCase: ")

print("snake_case: ", end='')

for n in camel:
    if n.islower():
        print(n, end='')
    else:
        print('_' + n.lower(), end='')
print()