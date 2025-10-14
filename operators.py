#1. Arithmetic (Math)
"""
x = 1
y = 2
res = 0

res = x + y #Addition
print(res)

res = x - y #Subtraction
print(res)

res = x * y #Multiplication
print(res)

res = x / y #Division
print(res)

res = x ** y #Exponentiation
print(res)

res = x // y # Floor Division
print(res)

#2. Assignment (Puts values into variables)

x = 5
x += 5
x -= 3
x *= 3
x /= 3

print(x)

#3. Comparison (Checks if things are different)

# == (Equals to), != (Not equal to), < > (Less/Greater than)

#4. Logical (Combines True or False conditions)

#  and (Means both must be true), or (One must be true), not (Flips true and false)

x = 3
y = 10
z = 3

print(x == y and y == z)
print(x == y or y == z)
print(not x == y)

#5. Identity (Checks if 2 objects are the same)

#is (Checks if the same), is not (checks if they're different)

x = 3
y = 3
print(x is y)
print(x is not y)


#6. Membership (Checks if things are inside a list)
# in (Checks if it exists in sequence), not in (Checks if something doesn't exist)

x = [1, 2, 3, 4, 5]

print(4 in x)
print(6 in x)
print(6 not in x)

"""
#List 
mix_list = [1, "Apple", 3.5, True] # Prints everything in list (Kinda just names as things are catalogged by index)
print(mix_list)

fruits = ["Apple", "Banana", "Cherry"]
print(fruits[0]) # []Index Selector
print(fruits[2])
print(fruits[-1]) # Prints the last index

#Modify Lists
fruits[1] = "Lemon"
print(fruits)

#Add to list
fruits.append("Grapes") # Always adds to the end
print(fruits)

fruits.insert(1, "Kiwi") # Adds to specific position
print(fruits)

#Remove from list
fruits.remove("Apple") # Have to call specific value instead of index
print(fruits)

fruits.pop() # Removes last item on list
print(fruits)

#Check if item is in list
if "Kiwi" in fruits:
    print("Yaass Queen!") # Prints only if the item is there

if "Apple" in fruits:
    print("Lil poison over here!")

#Length of List
print(len(fruits)) # Returns amount of items
