import csv
import sys

if len(sys.argv) < 3:
    sys.exit("Too few command-line argument")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line argument")

try:
    with open(sys.argv[1], "r", newline="") as file, open(sys.argv[2], "w", newline="") as new:
        reader = csv.DictReader(file)
        writer = csv.DictWriter(new, fieldnames=['first', 'last', 'house'])
        writer.writeheader()

        for row in reader:
            first, last = row['name'].split(", ")
            writer.writerow(
                {
                    "first":first,
                    "last":last,
                    "house":row['house']
                }
            )
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")