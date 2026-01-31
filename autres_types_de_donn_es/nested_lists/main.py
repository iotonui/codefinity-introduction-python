vegetables = ["tomatoes", "potatoes", "onions"]

vegetables.remove("onions")
print(vegetables)

vegetables.append("carrots")
print(vegetables)
vegetables.append("cucumbers")
print(vegetables)
vegetables.sort()
print(vegetables)

print("Updated Vegetable Inventory:" , vegetables )

if "carrots" in vegetables :
    print("Carrots are already in the liste")
if "cucumber" in vegetables:
    print("Cucumber are already in the list")
