from datetime import date

sum = 1+2
print(sum)

product = sum*2
print(product)

plant_in_solar_system = 8 #int
distance_to_alpha_centauri = 4.367 #float
can_liftoff = True #boolean
shuttle_landed_on_the_moon = "Apollo 11" #string

print(type(plant_in_solar_system))
print(type(distance_to_alpha_centauri))
print(type(can_liftoff))
print(type(shuttle_landed_on_the_moon))

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second_number: "))

add = first_number + second_number
sub = first_number - second_number
div = first_number / second_number
mul = first_number * second_number

print("Addition: ", add)
print("Subtraction: ", sub)
print("Division: ", div)
print("Multiplication: ", mul)

x = 7

x += 7
print(x)

x -= 7
print(x)

x *= 7
print(x)

x /= 7
print(x)

print("show in the console")

print("Today's date: " + str(date.today()))