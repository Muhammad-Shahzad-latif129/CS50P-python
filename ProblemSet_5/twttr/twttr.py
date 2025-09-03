VOWELS = ['a', 'e', 'i', 'o', 'u']
def main():
    s = input("Input: ").strip()
    print("Output:", shorten(s))

def shorten(word):
    result = ""
    for i in word:
        if not i.lower() in VOWELS:
            result += i

    return result

if __name__ == "__main__":
    main()        
