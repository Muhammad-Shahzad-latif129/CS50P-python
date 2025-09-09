import sys
from PIL import Image
from PIL import ImageOps
import os

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
if not sys.argv[1].lower().endswith((".png", "jpg", "jpeg")) or not sys.argv[
    2
].lower().endswith((".png", "jpg", "jpeg")):
    sys.exit("Invalid input")

ext1 = os.path.splitext(sys.argv[1])
ext2 = os.path.splitext(sys.argv[2])

if ext1[1].lower() != ext2[1].lower():
    sys.exit("Input and output have different extensions")

try:
    photo = Image.open(sys.argv[1])
    shirt = Image.open("shirt.png")
except FileNotFoundError:
    sys.exit("File doesnot exist")

size = shirt.size
photo_resized = ImageOps.fit(photo, size)
photo_resized.paste(shirt, shirt)
photo_resized.save(sys.argv[2])
