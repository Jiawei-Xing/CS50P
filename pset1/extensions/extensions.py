file = input("File name: ").lower().strip()
extension = file.split('.')[-1]
imageTypes = ['gif', 'jpg', 'jpeg', 'png']
appTypes = ['pdf', 'zip']

if extension in imageTypes:
    print(f"image/{extension.replace('jpg', 'jpeg')}")
elif extension in appTypes:
    print(f"application/{extension}")
elif extension == 'txt':
    print("text/plain")
else:
    print("application/octet-stream")