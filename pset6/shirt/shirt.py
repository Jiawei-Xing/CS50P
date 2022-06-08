import sys
import os
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    print("Too few command-line arguments")
    sys.exit(1)

if len(sys.argv) > 3:
    print("Too many command-line arguments")
    sys.exit(1)

if sys.argv[1][-4:] != ".jpg" and sys.argv[1][-4:] != ".png" and sys.argv[1][-5:] != ".jpeg":
    print("Invalid input")
    sys.exit(1)

if os.path.splitext(sys.argv[1])[1] != os.path.splitext(sys.argv[2])[1]:
    print("Input and output have different extensions")
    sys.exit(1)

try:
    shirt = Image.open("shirt.png")
    muppet = Image.open(sys.argv[1])
except FileNotFoundError:
    print("Could not read the file")
    sys.exit(1)
else:
    muppet = ImageOps.fit(image=muppet, size=shirt.size)
    muppet.paste(shirt, shirt)
    muppet.save(sys.argv[2])