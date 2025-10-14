# if (Checks a condition)
# elif (else if, chacks another condition if the first is false)
# else (runs if all other conditions are false)

age = 28
if age < 100:
    if age < 21:
        print("You can't be here.")
    else: 
        print("Welcome.")

elif age == 100:
    print("Wow, you're old.")
else: 
    print("Greetings.")

x = 10
if x > 0:
    print("There be an 'X' here.")
elif x == 0:
    print("The treasure must be buried elsewhere.")
else:
    print("There never was any treasure.")

#Shorthand if
y = 5
if y > 5: print("Y is greater or equal to 5.")

#Shorthand else
z = 2
print("even") if z % 2 == 0 else print ("odd")

#Nested statement
e = 15
if e > 0:
    if x < 20:
        print("x is positive less than 20")

#Combining conditions

age = 21
if age >= 21 and age <= 26:
    print("You're between 21 and 26 years old.")

f = 8
k = 8

if f == k:
    print("Hello.")
else:
    print("Come in.")