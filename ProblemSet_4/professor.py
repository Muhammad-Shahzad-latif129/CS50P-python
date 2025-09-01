import random


def main():
    score = 0
    l = get_level()
    for _ in range(10):
        x = generate_integer(l)
        y = generate_integer(l)
        for attempt in range(3):
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == x + y:
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
            if attempt == 2:
                print(f"{x} + {y} = {x + y}")
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        n = random.randint(0, 9)
        return n
    elif level == 2:
        n = random.randint(10, 99)
        return n
    elif level == 3:
        n = random.randint(100, 999)
        return n
    else:
        raise ValueError("Invalid level")


if __name__ == "__main__":
    main()
