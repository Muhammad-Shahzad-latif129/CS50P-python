import sys
import requests
import json

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    try:
        n = float(sys.argv[1])
    except ValueError:
        print("Command-line argument is not a number")    

    n = float(sys.argv[1])
    try:
        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=6662f11bf4e44504f645d2bbb0559967c1381592cff2a604c84c548672d834a1")
        response.raise_for_status()
        data = response.json()["data"]
        price = float(data['priceUsd'])
        amount = price * n
        print(f"${amount:,.4f}")

    except requests.RequestException:
        print("Error fetching data")
        pass    

if __name__ == "__main__":
    main()