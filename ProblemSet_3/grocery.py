def main():
    grocery = {}
    while True:
        try:
            s = input("Item: ").strip().upper()
            if s in grocery:
                grocery[s] += 1
            else:   
                grocery[s] = 1            
        except EOFError:
            print("\n")    
            break

    sorted_list = sorted(grocery)  
    for item in sorted_list:
        print(f"{grocery[item]} {item}")      

main()            