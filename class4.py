# Data Types

# Numeric- integer,float
# Sequence type- list,tuple,string
# Boolean
# set
# Dictionary
# binary types


# myString = "HelloWorld"

# print(myString)
# print(myString[0])
# print(myString[0:6])
# print(myString[-5:-1])
# print(myString[::-1]) #the :: is used to reverse the string.


# #concatenate

# string = "ha"
# print(string*4)


#String is immutable

# user = 'john'
# user2 = user.upper()
# print(user)
# print(user2)

#Python string method 

# #strip() function 
# password = "       hello    "
# new = password.strip()   # This will print the original string with whitespace
# print(password)          # This will print the stripped string
# print(new)



# #Updating a entire string 

# String1 = "HelloWorld"
# print("Initial String:")
# print(String1)

# String1 = "HelloEveryone"
# print("\nUpdated String:")
# print(String1)

#Updating a character

# String1 = "Hello My name is Pawan"
# print("Initial String: ")
# print(String1)

# list1 = list(String1)
# list1[2] = 'p'
# String2 = "".join(list1)
# print("\nUpdating character of 2nd index: ")
# print(String2)

#Tuple
    #Unpacking Tuple

# fruits = ("apple", "banana","cherry")
# (green,yellow,red) = fruits
# print(green)
# print(yellow)
# print(red)

  #Unpacking Tuple with *

# fruits = ("apple","banana","cherry","orange")
# (green,yellow,*red) = fruits
# print(green)
# print(yellow) 
# print(red)

#Dictionary 

# Dictionary Items

# carDetails = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
# print (carDetails ["brand" ])
# print (carDetails. get ("model"))
# print (carDetails. keys ())
# print (carDetails. values ())
       
#Add t5o dictionary items

# carDetails = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
# carDetails["color"] = "Coal"
# print(carDetails)

#Update the dictionary item 

# carDetails = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
# carDetails.update({"mileage":8})
# print(carDetails)

# #Using pop() #it remvoes which we want

# carInfo = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
# carInfo.pop("model")
# print(carInfo)

#Using popitem() #it start to remove from the ending

# carInfo = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
# carInfo.popitem()
# print(carInfo) 

# #Loop through dictionary items

# student = {
#     "name":"John",
#     "grade":"XII",
#     "age":"21"
# }

# for x in student:
#     print(x)

# for x in student.values():
#     print(x)

# for x,y in student.items():
#     print(x,y)    


# #Creating Nested Dictionary Items

# texasStudent = {
#     "firstYear": {
#         "course":"BIT",
#         "batch": 2020
#     },
#     "secondYear":{
#         "course":"BIT",
#         "batch":2021
#     },
#     "thirdYear": {
#         "course":"BBA",
#         "batch": 2019
#     }
# }
# print(texasStudent["secondYear"]["course"])

# alt+shift=downarrow to copy paste the code downward


#Function 

#    #reversed function 

# my_list = [1,2,3,4,5]
# reversed_list = list(reversed(my_list))
# list(reversed(my_list))
# print(reversed_list)

#    #zip function 

# list1 = [1,2,3]
# list2 = ['a','b','c']
# zipped = zip(list1, list2)
# print(list(zipped))


# # Function with arguments

# def my_function(fname, lname):
#     print(fname + " "+lname)

# my_function("Pawan","Joshi")



# # Function with parameter

# def my_function(fname="John",lname="Doe"):
#     print(fname + " " + lname)

# my_function()



# # Creating my first function 

# def calculate():
#     print("Hello, Texas")

# calculate()



# #recursive function :

# def tri_function(k):
#     if(k>0):
#         result = k + tri_function(k-1)
#         print(result)
#     else:
#         result=0 
#     return result

# tri_function(6)       





""" Q1. Develop a game where the computer randomly selects a number within a specified range, and the user has to guess the number.
Provide hints if the guessed number is too high or too low.
After user guess correct number display guess attempts and the exact answer too.
Make sure user does not input other than integer, if its other data type show them invalid input.

Hint: Use while loop, generate random number use python random.randint() function """


import random

def guess_number():
     lower_band =1
     upper_band = 100
    
    # Initialize variables
attempts = 0
guessed = False
    
    # Start the game
print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100. Can you guess it?")
    
while not guessed:
        try:
            # Prompt the user for a guess
            guess = int(input("What is the number: "))
            
            # Validate the guess
            if guess < 1 or guess > 100:
                print("Invalid input. Please enter a number between 1 and 100.")
                continue
            
            # Increase the number of attempts
            attempts += 1
            
            # Check if the guess is correct
            if guess == guess_number:
                guessed = True
                print("Correct! Congratulations!")
                print("Number of attempts:", attempts)
                print("The secret number was:", int(guess_number))
            elif guess < int(guess_number):
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
print("Thank you for playing the Number Guessing Game!")

# Call the function to start the game
guess_number()















