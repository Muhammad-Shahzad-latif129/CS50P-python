import inflect

p = inflect.engine()
l = []


def main():
    while True:
        try:
            s = input("Name: ").strip()
            l.append(s)
        except EOFError:
            print()
            break

    t = p.join(l)
    print(f"Adieu, adieu, to {t}", )


if __name__ == "__main__":
    main()
