#Tuples are like lists - store multi items
#They can't be changed after created
#Written using ()
#An Array but immutable?

my_tuple = ("apple", "banana", "kiwi")
print(my_tuple)

#Access Items(Same as array)
print(my_tuple[0])
print(my_tuple[2])

#Check if item exists
if "banana" in my_tuple:
    print("Yes")

#Find length
print(len(my_tuple))

#Single Item tuple
single = ("chair",)
print(single)

#Nested tuple
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
combine = (tuple1, tuple2)
print(combine)

#MC

#Create a travel bag
travel_bag = ("Clothes", "Toiletries", "Shoes", "First aid kit", "Swimsuit")

#print the 2nd and 4th items
print(f"On this trip I have to bring {travel_bag[1]} and {travel_bag[3]}.")

#check to see if shoes are in the list
if "Shoes" in travel_bag:
    print("You're ready to go!")
else:
    print("You probably need to repack...")

#create secondary tuple called essentials
essentials = ("Bug spray", "Suncreen", "Inhaler")

#combine the two tuples
final_bag = travel_bag + essentials

#print the final amount of items from the combined tuples
print(f"I had to add some things so that brings me to: {len(final_bag)} items.")

#print the very last item in combined tuples
print(f"An absolute must is my {final_bag[-1]}.")