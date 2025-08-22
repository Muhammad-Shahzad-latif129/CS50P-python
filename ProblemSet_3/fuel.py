def main():
    while True:
        try:
            v = (input("Fraction: ")).strip()
            n, d = v.split(sep="/")
            n, d = int(n), int(d)
            if n > d:
                continue
            f = round((n / d) * 100)
        except (ValueError, ZeroDivisionError):
            pass  
        else:
            break 

    if f <= 1:
        print("E")
    elif f >= 99:
        print("F")  
    else:
        print(f"{f}%")    

main()
