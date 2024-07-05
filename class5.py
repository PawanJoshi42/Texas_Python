def case(string):

 count = {
    "UPPER_CASE":0,
    "LOWER_CASE":0
}

 for character in string:
    if character.isupper():
        count["UPPER_CASE"] +=1
    elif character.islower():
        count["LOWER_CASE"] +=1
    else:
        pass

 print("Original String:", string)
 print("Number of Upper Letter: ",count["UPPER_CASE"])
 print("Number of Lower Letter: ",count["LOWER_CASE"])

user = input("Enter a paragraph: ")
case(user)






