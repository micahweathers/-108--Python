shopping_list = ["Bread", "Milk", "Butter", "Honey", "Eggs"]
print("Full List:", shopping_list)

print("Printing First and Last Item: ", shopping_list[0], shopping_list[-1])
 
shopping_list[1] = "Chocolate Syrup"
print(shopping_list)
print("!Changing second Item to: ", shopping_list[1])

shopping_list.append("Ice Cream")
print("Adding to end: ", shopping_list[-1])

shopping_list.remove("Eggs")
print("Removed Item, Final List: ", shopping_list)

print("Length of list: ", len(shopping_list))