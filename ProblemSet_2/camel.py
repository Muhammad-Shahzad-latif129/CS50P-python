def main():
    s = input("camelCase: ")
    print("snake_case: ", end="")
    for c in s:
        if c.isupper():
            print("_", end="")
            print(c.lower(), end="")
        else:   
            print(c, end="") 
    print()

main()        
