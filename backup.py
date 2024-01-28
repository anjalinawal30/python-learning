import sys

#python backup.py 27-01-2024

print(sys.argv)
print(sys.argv[0])
print(sys.argv[1])

'''output
['backup.py', '27-01-2024']
backup.py
27-01-2024 
'''

print("Welcome to greeting program")
name = input("Enter your name : ") #input() will not working with python 2.7 use raw_input() for string
print("Greetings " + name)

print("Calculator program")
first_number = input("Enter number: ")
second_number = input("Enter number: ")
print(first_number+second_number)
