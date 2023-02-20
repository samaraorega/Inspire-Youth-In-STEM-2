#create a list of empty musicians
#using for loop add five new musicians
#copy the list to a new list called celebs
#sort the list
#pop out two celebs
#count the remaining celebs in the list

favorite_musicians =["Giveon","Brent","Oxlade","Sonder","Nikki"]
for musician in favorite_musicians:
    print(musician)
favorite_musicians.append("Ice spice")
favorite_musicians.append("Trey")
favorite_musicians.append("Bryson")
favorite_musicians.append("Usher")
favorite_musicians.append("Camilla")
for musician in favorite_musicians:
    print(musician)

celebs = favorite_musicians.copy()
print(celebs)
celebs.sort()
print(celebs)

celebs.pop()
celebs.pop()
print(celebs)


print(len(celebs))