dic = {
    "Apple": 130, "Avocado": 50, "Banana":110,
    "Cantaloupe":50, "Grapefruit":60, "Grapes":90,
    "Honeydew Melon":50, "Kiwifruit":90, "Lemon":15,
    "Lime":20, "Nectarine":60, "Orange":80,
    "Peach":60, "Pear":100, "Plums":70,
    "Sweet Cherries":100, "Tangerine":50, "Watermelon":80,
    "Pineapple":50, "Strawberries":50
}
# Making all keys lower through dictionary comprehension
dic = {k.lower(): v for k, v in dic.items()}
def main():
    item = input("Item: ").strip()
    item = item.lower()
    if item in dic:
        print(f"Calories: {dic[item]}")
    else:
        print("Item not found")    

main()        