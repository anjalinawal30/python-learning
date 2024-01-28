#operators in Python
# Addtion +
#Subtraction -
#Multiplication *
#Division /
#Floor Division with round down //
#Remainder %
num = 10
print(num//3)

#Order of operation
# Parentheses -> Exponents -> Multiplication and Division -> Addtion and Subtraction
result_1 = 1032 + 26 * 2
print(result_1)

result_2 = 1032 + (26 * 2)
print(result_2)

#Work with numbers
dint = int('26')
print(dint)
dflot = float('26.2')
print(dflot)

#absolute values -> convert negative number to absolute
num1 = 16-39
num2 = 39-16
print(num1)
print(abs(num1))
print(abs(num2))

#round() ->  if the decimal value is greater than .5, or down if it's less than .5. If the decimal value is equal to .5, the function rounds up or down to the nearest even integer.
print(round(1.4))
print(round(1.5))
print(round(1.6))
print(round(2.5))
print(round(2.6))

#Math library - ceil(round up) and floor(round down)
from math import ceil, floor
num3 = ceil(1.5)
num4 = floor(1.5)
print(num3, num4) 