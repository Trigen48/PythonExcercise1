
#clear the screen
import os
os.system('cls')

shoppingCart = []
inputItem = input("Enter item name: ")

while inputItem != "":
    shoppingCart.append(inputItem)
    inputItem = input("Enter item name: ")

print("")
print("Items in the shopping cart:")
for item in shoppingCart:
    print(item)