def main():
    s = input("Expression: ").strip()
    x, y, z = s.split(" ")
    x, z = float(x), float(z)

    if y == '+':
        a = x + z
        print(f"{a:.1f}")
    elif y == '-':
        a = x - z 
        print(f"{a:.1f}")
    elif y == '*':
        a = x * z
        print(f"{a:.1f}")
    elif y == '/' and z != 0:
        a = x / z
        print(f"{a:.1f}")
    else:
        print("Invalid")         

main()