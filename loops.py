# #While loops repeat a block of code as long as a condition is true
# #Infinite loops occur if a condition never becomes false

# count = 1

# while count <= 5:
#     print(f"Current count is: {count}") #Infinite by self
#     count += 1 #Creates a close

# #Create a break to stop loop

# count = 1

# while count <= 10:
#     if count == 5:
#         print("Breaking at 5!")
#         break #Exits loop early
#     print(count)
#     count += 1

# count = 0
# while count < 5:
#     count += 1
#     if count == 3:
#         continue #Similar to break but skips
#     print(count)

# #Else with while loop runs when loop becomes false
# print("------------")
# count = 1

# while count < 3:
#     print(count)
#     count += 1
# else:
#     print("Loop Finished.")

# #MC

# #Ask for password
# password = (input("Enter your password: "))
# #While password is wrong, loop back to input
# while password != "Password": 
#     print("Incorrect, try again.")
#     password = input("Enter your password: ")
# else:
#     #Else if correct skip loop and grant access
#     print("Access Granted")

# #For loops are used for looping a sequence: List, Tuple, Dictionary, String etc.
# #Loop through a list

# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits: #  Temp variable inside variable
#     print(fruit)

# #Loop through a list
# print("------------")

# for letter in "Hello":
#     print(letter)

# #Using Range(which is a sequence of numbers)
# print("------------")

# for x in range(5):
#     print(x)

# print("------------")
# #Start, Stop
# for x in range(2, 6):
#     print(x)

# print("------------")
# #Start, Stop, Step(Skip number)
# for x in range(0, 10, 2):
#     print(x)

# #Else in for loop

# print("------------")

# for x in range(3):
#     print(x)
# else:
#     print("Loop Complete!")

# #Break and Continue
# print("------------")

# for x in range(10):
#     if x == 5:
#         continue
#     if x == 8:
#         break
#     print(x)

#MC2

#make a counter for items length
counter = 0

#make list
my_list = ["Clothes", "Pie", "Bread", "Croc", "Neon", "Highlighter"]

#count which are more than 5 word
for items in my_list:
   if len(items) >= 5:
      counter += 1

#print counter
print(f"Out of {len(my_list)} items, there were {counter} with 5 or more letters in my list.")