import random


def main():
    l = get_int("Level: ")
    ran_no = random.randint(1, l)
    guess(ran_no)


def guess(ran_no):

    while True:
        g = get_int("Guess: ")
        if g > ran_no:
            print("Too large!")
        elif g < ran_no:
            print("Too small!")
        else:
            print("Just right!")
            break


def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
        except ValueError:
            pass


if __name__ == "__main__":
    main()
