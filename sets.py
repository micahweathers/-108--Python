#Sets store multiple items in a single variable
#Sets are unordered(semi-randomized?why?), non-indexed and no duplicates
#Sets are used with {}

fruits = {"apple", "banana", "cherry"}
print(fruits)

#No duplicates allowed

fruits = {"apple", "orange", "cherry", "apple"}
print(fruits)

#Check for item
print("banana" in fruits)

#Add items
fruits.add("pear")
print(fruits)

#Add multi items
fruits.update(["kiwi", "mango"])
print(fruits)

#Remove items
fruits.remove("pear")
print(fruits)

#If you're unsure if item is there use discard
fruits.discard("papaya")
print(fruits)

fruits.discard("mango")
print(fruits)

#set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.union(set2))        #combine both no duplications
print(set1.intersection(set2)) #combines only duplicate elements
print(set1.difference(fruits)) #shows you the first set non dupes

#MC

invited_friends = {"Alex","Mina","Sam","Leo","Lucia"}
rsvped = {"Mina", "Sam", "Jordan"}

print(f"-I decided to invite {invited_friends.union(rsvped)}. \nSo far only {rsvped} have said they're coming.")
print(f"-I still haven't heard back from {invited_friends.difference(rsvped)}.")
invited_friends.update(["Angela", "Marco"])
print(f"-I had to invite the new couple so that makes my list {invited_friends.union(rsvped)}.")
invited_friends.remove("Alex")
leo_coming = input("-Is Leo coming? (yes/no): ").lower()
if leo_coming == "yes":
    rsvped.add("Leo")
    print("-Perfect! Leo is on the list!")
else:
    print("-Unconfirmed.")

print(f"-So that means I have {len(rsvped)} people confirmed so far.")