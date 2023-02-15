name=("Fiona","David","Samara")
#accessing names on a list
print(name)
print(name[0])
print(name[0:2])
fruits=("mangoes","guavas","apple","peaches","kiwi")
print(fruits[0:-1])
print("My favorite fruit is",fruits[2].upper())
#Adding two lists
vegetables=("spinach","cabbage","mushrooms","carrots","cauliflower")
stationary=("ink","pens","eraser","rulers","set")
shoppings=vegetables+stationary
print(shoppings[5])

for vegetable in vegetables:
    print(vegetable)

for shopping in shoppings:
    print(shopping)
    

print("My name is " + name[2]+ " and my favorite fruit is " + fruits[2])
