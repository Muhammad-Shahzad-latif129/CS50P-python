from datetime import date
import sys
import inflect

def main():
    print(convert(input("Date of Birth: ")))

def convert(birthday):
    try:
        dob = date.fromisoformat(birthday)
    except ValueError:
        sys.exit("Invalid date.")

    today = date.today()

    delta = today - dob
    total_minutes = delta.days * 24 * 60

    p = inflect.engine()
    words = p.number_to_words(total_minutes, andword= "")
    return words.capitalize() + " minutes"


if __name__ == "__main__":
    main()
