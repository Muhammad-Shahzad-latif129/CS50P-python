def main():
        v = (input("Fraction: ")).strip()
        try:
            f = convert(v)
            print(f"{gauge(f)}")
        except (ValueError, ZeroDivisionError):
            pass    


def convert(fraction):
    n, d = fraction.split(sep="/")
    n, d = int(n), int(d)
    if d == 0:
        raise ZeroDivisionError
    if n > d:
        raise ValueError
    f = round(n/d * 100) % 100
    return f


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
