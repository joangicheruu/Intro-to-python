# if else
import os

name = input("Enter your name: ")

age = input("Enter your age:")

if not age.isnumeric():
    print("Your age is invalid")
    # terminate
    os._exit(0)

if int(age) >= 18:
    print(name + " is an adult")
else:
    print(name + " is a child")
# lists, booleans, tuples, dictionary, loops

