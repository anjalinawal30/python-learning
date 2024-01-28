#Lists in Python LIFO 
#Create a list - Each value is separated by a comma and surrounded by brackets ([]). 
planets = ['Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune'] #can be use "" and ''
print(planets[0])
print(planets[3])
planets[3] = "Red Planet"
print(planets[3])

#length of the list
print(len(planets))
#print(planets[8]) #will not work

#add value to the list
planets.append("Pluto")
print(len(planets))
print(planets[8]) #will work

#remove value to the list
planets.pop()
print(len(planets))

#use negative index - it will show value from last
print(planets[-1]) #output - Neptune
print(planets[-2]) #output - Uranus

#find a value in list 
find_earth = planets.index("Earth")
print(find_earth+1)
#find_pluto = planets.index("Pluto") will not work as pluto is not there.
#print(find_pluto)

#work with number in list
#Store numbers in lists
planets_gravity = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
bus_weight = 124054  #In Newtons on earth
print("On Earth, a double-decker bus weighs", bus_weight * planets_gravity[2], "N")
print("On Mercury, a double-decker bus weighs", bus_weight * planets_gravity[0], "N")

#Use min() and max() with lists
print("The lightest bus weight" , bus_weight*min(planets_gravity), "N")
print("The Heaviest bus weight" , bus_weight*max(planets_gravity), "N")

#manipulate list data
#Slice list
print(planets[0:2]) #2 is not included it will print 0 and 1 value
print(planets[3:8])
print(planets[0:])
#A slice creates a new list. It doesn't modify the current list.

#Join lists by using + operator
amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]
regular_satellite_moons = amalthea_group + galilean_moons
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

regular_satellite_moons.sort()
#Sort lists
#Python sorts a list of strings in alphabetical order and a list of numbers in numeric order:
print("The regular satellite moons of Jupiter are", regular_satellite_moons)
regular_satellite_moons.sort(reverse=True)
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

#Using sort modifies the current list.

#Exercise

#Create the list of planets
planets = ["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"]

#Prompt the user for the reference planet
userinput = input("Enter the planet name (Start with Capital Letter) ")

#Prompt the user for the reference planet
find_planet = planets.index(userinput)

#Display planets closer to the sun
print("Here are planet closer than " + userinput)
print(planets[0:find_planet])

#Display planets closer to the sun
print("Here are planet further than " + userinput)
print(planets[find_planet+1:])

#------------------------#
#While Loop
user_input = '';
inputs = []

while user_input.lower() != 'done':
    if user_input:
        inputs.append(user_input)
    user_input = input('Enter a value or done when done ')

print(inputs)

#For Loop - syntax - for variable in sequence
from time import sleep
countdown = [4,3,2,1,0]
for i in countdown:
    print(i)
    #sleep(1)
print("Blast off")

#for and while loop
usernumber = ''
numbers = []
while usernumber != 'done':
    if usernumber:
        numbers.append(usernumber)
    usernumber = input("Enter number ")

for number in numbers:
    print(number)
    #sleep(1)

print("Happy New Year")

#Dictionaries in Python

#before using dictionaries 
earth_name = 'Earth'
earth_moons = 1
jupiter_name = 'Jupiter'
jupiter_moons = 79

#after using dictionaries

#create dictionary
planet = {
    'name' : 'Earth',
    'moon' : 1
}

#read value both same but
#If a key isn't available, get returns None, and [ ] raises a KeyError.
print(planet.get('name')) 
print(planet['name'])

#print(planet.get('gravity'))  #return None
#print(planet['gravity'])    #throw Keyerror

#modify dictionary
planet.update({'name':'Makemake'})
print(planet['name'])
planet['name'] = 'makemake'
print(planet['name'])

planet['diameter (km)'] = {
    'polar': 133709,
    'equatorial': 142984
}
print(f'{planet["name"]} polar diameter: {planet["diameter (km)"]["polar"]}')

#Add and remove keys
planet['orbital period'] = 333

#planet.pop('name')
planet.pop('orbital period')
print(planet)

#Exercise
#Managing planet data
planet = {
    'name': 'Mars',
    'moons': 2
}
#Display planet data
print(f'{planet["name"]} has {planet["moons"]} moon(s)')

#Add circumference information
planet['circumference (km)'] = {
    'polar': 6752,
    'equatorial': 6792
}
print(f'{planet["name"]} has a polar circumference of {planet["circumference (km)"]["polar"]}')

#Dynamic programming with dictionaries
#Retrieve all keys and values
rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}
for key in rainfall.keys():
    print(f'{key}:{rainfall[key]}cm')
    
#Determine if a key exists in a dictionary
if 'december' in rainfall:
    rainfall['december'] = rainfall['december'] + 1
else:
    rainfall['december'] = 1

#Retrieve all values
#Similar to keys(), values() returns the list of all values in a dictionary without their respective keys. 
total_rainfall = 0
for value in rainfall.values():
    total_rainfall = value + total_rainfall
print(total_rainfall)