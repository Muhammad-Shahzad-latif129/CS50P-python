import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")
count = 0
try:
    with open(sys.argv[1], "r") as file:
        reader = file.readlines()
        for line in reader:
            if (not line.lstrip().startswith("#")) and line != '\n':
                count += 1    
        print(f"Lines: {count}")        

except FileNotFoundError:
    sys.exit("File does not exist")
