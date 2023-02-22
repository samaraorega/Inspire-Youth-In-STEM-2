#Advanced data types

#Mutable vs Immutable
#Mutable- Data types that can be changed during programme life cycle
#You can add or remove elements

#Immutable-Data types that cannot be edit during life cycle

#List-It is mutable
friends = ["Ann","Fiona","David"]
# or friends = []
# add ---> append(),extend()
# remove -->pop()

students = ["Clive","Kanyi"]

friends.extend(students)
friends.append("Hannah")
friends.sort()
friends.reverse()

#Tuples(immutable)
#()
stationaries = ("pens","ink","eraser","sharpener","stapler")

#you can replace the whole tuple
stationaries = ("ruler","clips","highlighter")

for stationary in stationaries:
    print(stationary)

numbers = (1,2,3,4,5,6)

#Dictionaries aka dict
#uses key and value pair to store data

student = {"Name" : "Orega", "age" : 20,}
print(student["Name"])
print(student["age"])
#name is the key ---> Orega is the value

friend = {"Favorite color" : "Red", "Hobby" : "Baking", "Course" : "Welding", "Height" : 150, "Residence" : "Riara", "Favorite food" : "Chapo"}
print(friend["Favorite color"])
print(friend["Course"])
print(friend["Height"])
print(friend["Favorite food"])
print(friend["Residence"])
print(friend["Hobby"])

#Sets
