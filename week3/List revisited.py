#!/usr/bin/env python3

myFavoriteFruits = ["banana","apple","avocado","watermelon","grapes"]
for fruit in myFavoriteFruits:
    print(fruit)
#len shows number of elements in the list
print(len(myFavoriteFruits))

friends = ["David","Fiona","Kanyi","Khaemba","Msupa"]
print(friends)
friends[0] = "Mary"
print(friends)

#append=adds an element into a list
#clear=removes all elements in a list
#copy=copies all elements
#remove=removes item from a list(specified value)
#sort=sorts the  list
#reverse=
#pop= removes the last element
#insert=adds an element in a specified position
#extend=adds element to the end of a list
#index=
#count=length
#sort=

print("-------------")
new_friends = friends.copy()
print(new_friends)

new_friends.sort() 
print(new_friends)

new_friends.pop()
print(new_friends)

