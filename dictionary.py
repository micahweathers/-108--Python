#Store data in KEY : Value pairs
#Like a mini database or real-life dictionary (word -> meaning)

#Written with {}
#like objects/arrays? how is this different?

students = {
    "name": "Micah",
    "age": "28",
    "major": "n/a"
}

print(students)

#Accessing items by key
print(students["name"])
print(students.get("major")) #Alt way/still valid

#Adding items to dictionary
students["graduation_year"] = 2025
print(students)

#Change values
students["age"] = 29
print(students)

#Remove items
students.pop("major")
print(students)

#Checking for items
if "name" in students:
    print("Yes")
else:
    print("No")

#Nested
students = {
    "student1": {"name": "Micah", "age": 28},
    "student2": {"name": "Geoffry", "age": 75}
}

print(students["student1"]["name"])
print("--------*Mini Challenge*--------")

#MC

#Create report card dictionary
report_card = {
    "name": "Micah",
    "subject": "Math",
    "grades": (85, 76, 92)
}

#Print name and subject
print(f"Student: {report_card['name']}")
print(f"Subject: {report_card['subject']}")

#Calculate and add average

report_card["average"] = (report_card["grades"][0] + report_card["grades"][1] + report_card["grades"][2]) /3
print(f"Average: {report_card["average"]:.2f}")

#Check average and print message
if report_card["average"] >= 90:
    print("Excellent!")
elif report_card["average"] >=70:
    print("Good Job!")
else:
    print("See me after class.")

#Remove subject and print update
del report_card["subject"]
print(f"""
      Updated Report card: 
      {report_card}
""")

#Remove Decimals
grades = [90, 56, 44]

average = int(sum(grades) / len(grades))
print(average)

#round()
average = round(sum(grades) / len(grades))
print(average)

#only 2 decimals *Visual only*
num = 87.666666666667
print(f"num:.2f")#87.66
print(f"num:.1f")#87.6
print(f"num:.0f")#87