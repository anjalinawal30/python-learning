# Use Boolean logic in Python 

#write if statement
'''
>, <, >=, <=, ==, !=
'''

x = 20
y = 10
if x >= y:
    print(x)
    
#write else statement

x = 15
y = 5
if x <= y:
    print(x)
else:
    print(y)
    
#writ elif (else if) statement

x = 93
y = 75
if x == y:
    print("x is equal to y")
elif x < y:
    print("y is greater than x")
else:
    print("x is greater than y")
   
# nested logic statement

a = 15
b = 20
c = 25

if a > b:
    if b > c:
        print(" a is greater than b,c and b is greater than c")
    else:
        print("a is greater than but less than c")
elif a == b:
    print("a is equal to b")
else:
    print("a is less than b")
    
# and & or operator

if a == b and b > a:
    print("Hello")
else:
    print("Ok")

if a < b or b < c:
    print("Nice")
else:
    print("Ok2")

#Use string 
fact = "The Moon has no atmosphere"
print(fact)

#string are immutable
fact = "The Moon has no atmosphere"
fact = fact + " No Sound can be heard on moon"
print(fact)

fact = "The Moon has no atmosphere"
new_fact = fact + " No Sound can be heard on moon"
print(new_fact)

print("The Moon has a radius of 1,080 miles.")
print('The "near side" is the part of the Moon that faces the Earth.')
print("We only see about 60% of the Moon's surface.")
print("""We only see about 60% of the Moon's surface, this is known as the "near side".""")

#Use a newline character (\n).
#Use triple quotation marks (""").

multiline = "Facts about the Moon:\n There is no atmosphere.\n There is no sound"
print(multiline)

multilines = """Facts about the Moon:
 There is no atmosphere. 
 There is no sound."""
print(multilines)

# .title() returns the string in initial caps and can be used with a string directly:
print("temperature is very high today in bangalore".title())

news = "temperature is very high today in bangalore"
news_cap = news.title()
print(news_cap)

#Split a string
#Without arguments, the method will separate the string at every space. 
#This would create a list of every word or number that's separated by a space

temperature = "Day: 30 degree C, Night: 15 degree C"
temp = temperature.split()
print(temp)

temperature1 = "Day: 30 degree C, Night: 15 degree C"
temp1 = temperature1.split(',')
print(temp1)

#Using [-1] on the list returns the last item
print(temp1[-1])

#Search for a string - use "in"
print("Moon" in "facts and challenges with space travel")
print("Moon" in "facts about the Moon")

#the position of a specific word in a string is to use the .find()
temperature2 = "Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."
print(temperature2.find("Moon"))
print(temperature2.find("Mars"))

#use the .count() method, which returns the total number of occurrences of a certain word
print(temperature2.count("Moon"))
print(temperature2.count("Mars"))

#LowerCase and UpperCase"
var1 = "The Moon And The Earth"
print(var1.lower())
print(var1.upper())

#.isnumeric() method, .isdecimal()
mars = "The highest temperature on Mars is about 30 C"
for item in mars.split():
    if item.isnumeric():
        print(item)

print("-60".startswith('-'))
item = "30 C"
if item.endswith('F'):
    print("Temperature is in Fahrenheit")
else:
    print("Temperature is in Celsius")
    
fact = "Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."
print(fact.replace("Celsius", "C"))

text = "Temperatures on the Moon can vary wildly."
print("temperatures" in text)

text = "Temperatures on the Moon can vary wildly."
print("temperatures" in text.lower())

moonfacts = ["The Moon is drifting away from the Earth.", "On average, the Moon is moving about 4cm every year."]
print(' '.join(moonfacts))
#' ' is used to join every item in the list.

moon = "Moon"
earth = "Earth"
print("""Both sides of the %s get the same amount of sunlight, but only one side is seen from %s because the %s rotates around its own axis when it orbits %s.""" % (moon, earth, moon, earth))

mass = "1/6"
moon1 = "the Moon"
earth1 = "Earth"
print("On the Moon, you would weigh about {} of your weight on Earth.".format(mass))
print("On {0}, you would weigh about {1} of your weight on {2}.".format(moon1, mass, earth1))

#about f-string
print(f"On the Moon, you would weigh about {mass} of your weight on Earth.") #As of Python version 3.6

subject = "interesting facts about the moon"
heading = f"{subject.title()}"
print(heading)

print(round(100/6, 1)) #here 2 is after decimal two digit 16.67 # 1 = 16.7

#-------------------#
name = 'Ganymede'
planet = 'Mars'
gravity = '1.43'

template = """Gravity Facts about {name}
----------------------------------------
Planet Name: {planet}
Gravity on {name}: {gravity} m/s2"""
print(template.format(name=name,planet=planet,gravity=gravity))