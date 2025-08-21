l = ['a', 'e', 'i', 'o', 'u']
def main():
    s = input("Input: ").strip()
    s = s.lower()
    print("Output: ", end="")

    for i in s:
        if not isvowel(i):
            print(i, end="")
            
    print() 

def isvowel(s):
    if s in l:
        return True
    else:
        return False               
        

main()    