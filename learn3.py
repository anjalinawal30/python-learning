#Basics of Python functions
#Function with no arguments
def rocketparts():
    print("payload, propellant, structure")
 
rocketparts()
#---------------------------------------------#
def rocketparts():
    return "payload, propellant, structure"
 
output = rocketparts()
print(output)

#Requiring an argument
def rocketparts(parts):
    if parts == 'payload':
        return True
    else:
        return False

output = rocketparts('payload')
print(output)

#Multiple required arguments
def daystocomplete(distance, speed):
    hours = distance * speed
    print(hours/24)

daystocomplete(100, 23)

#Functions as arguments
#round(daystocomplete(100, 23))

#Use keyword arguments 
from datetime import timedelta, datetime

def arrival_time(hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    print(arrival.strftime("Arrival: %A %H: %M"))

arrival_time()
arrival_time(hours=0)

def arrival_time(destination, hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    print(arrival.strftime(f"{destination} Arrival: %A %H:%M"))
    
arrival_time("moon")

#Use variable arguments as tuple
def variable(*args):
    print(args)

variable()
variable("one","two")
variable(1,2)
variable(1)
variable(None)

def total_time(*args):
    total = sum(args)
    if total < 60:
        print(f"Total time to launch is : {total} min") 
    else:
        print(f"Total time to launch is : {total/60} hours")
    
total_time(4,14,18)
total_time(4,14,48)

#Variable keyword arguments
def variable_key(**kwargs):
    print(kwargs)
    
    for key,value in kwargs.items():
        print(f"{key}:{value}")

variable_key(tanks=1,day="Wednesday",pilots=3)

#Error handling
#tracebacks to find errors

#open("/path/to/mars.jpg") #will throw error check open.py

#Try and except blocks
try:
    open("/path/to/mars.jpg")
except FileNotFoundError:
    print("File not found")
    
#Raise exceptions
def water_left(astronauts, water_left, days_left):
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    print(f"Total water left after {days_left} days is: {total_water_left} liters")

water_left(5, 100, 2)

def water_left(astronauts, water_left, days_left):
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    if total_water_left < 0:
        raise RuntimeError(f"There is not enough water for {astronauts} astronauts after {days_left} days!")
    print(f"Total water left after {days_left} days is: {total_water_left} liters")

#water_left(5, 100, 2) directly calling function will give error

try:
    water_left(5, 100, 2)
except RuntimeError as err:
    print(err)