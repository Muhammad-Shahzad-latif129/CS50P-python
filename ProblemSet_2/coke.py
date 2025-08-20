def main():
    amount = 50 
    while amount > 0:
        print(f"Amount Due: {amount}")  
        i = int(input("Insert Coin: "))
        if i in [25,10, 5]:
            amount -= i
        else:
            continue
    print(f"Change Owed: {amount}")           
            
main()