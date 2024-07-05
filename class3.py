
# Write a program to calculate the electricity bill(accept number of unit from user)
#according to the following criteria:

# unit = int(input("Enter your unit"))
# if unit <= 100:
#    print("No charge !! ")
# elif unit <=200 and unit>100:
#     print("Your total bill amount"+ str((unit-100)*5))
# elif unit > 200:
#     print("Your total bill amount"+ str(500+(unit-200)*10))


#Loop condition 
                  #For Loop
                  #While Loop
                  #Nested Loop


#For loop example
        # text="Pythonprograaming"
        # for i in text:
        # print(i)

# #For loop with example:
fruits=["apple","banana","grapes"]
for index in range(len(fruits)):
 print(len(fruits))
else:
 print("Inside Else Block")




# #while loop

# count = 0
# while (count < 3):
# #  count = count + 1
#  print ("Hello Programming")
# count = count + 1


#nested loop

# adj = ["red","big","tasty"]
# fruits = ["apple","grapes","cherry"]
# for x in adj:
#     for y in fruits:
#         print(x,'\t',y,'\n')


# for pyramid
# for i in range(1,5):      # 1 first ma 1 huncha
#     for j in range(i):    # 1 chalxa
#         print(j,end='')   # 1 print
#     print()               # to new line



#nested while

# i=1
# while i<10:
#     j=i
#     while j<10:
#         print(f"{j}",end="")
#         j = j+1
#     print("")
#     i = i+1
# print("Complete")

# Assignment 

# """""
# Q1. Write a program to print multiplication table of a given number(accept number from user)
# eg. if user input 3
# 3 x 1 = 3
# 3 x 2 = 6 and so on
# """

# number = input("Enter a number:")
# number = int(number)

# print(f"Multiplication Table of {number}:")

# for i in range(1,11):
#     print(f"{number} x {i} = {number * i}")



# # Q2. Accept 10 numbers from user and display average of it.

# number1 = int(input ("Enter 1st number: "))
# number2 = int(input ("Enter 2nd number: "))
# number3 = int(input ("Enter 3rd number: "))
# number4 = int(input ("Enter 4th number: "))
# number5 = int(input ("Enter 5th number: "))
# number6 = int(input ("Enter 6th number: "))
# number7 = int(input ("Enter 7th number: "))
# number8 = int(input ("Enter 8th number: "))
# number9 = int(input ("Enter 9th number: "))
# number10 = int(input ("Enter 10th number: "))
# average = (number1+number2+number3+number4+number5+number6+number7+number8+number9+number10)/10
# print(f"Average of 10 given numbers:{average}")



"""
# Q2. Accept 10 numbers from user and display average of it.

total = 0

print("Please Enter 10 numbers")

for i in range(1,11):
    number = input(f"Enter number {i}: ")
    number = float(number)
    
    total += number
    
average = total/10

print(f"Average of given 10 numbers is: {average:.2f} ")
"""


# Q3. Write a program to display numbers which is divisible by only 11 from 100 to 300.

# print("Numbers divisible by only 11 from 100 to 300:")

# for i in range(100,301):
#     if i%11==0 and i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0:
#         print(i)