#Lab 2 Question 4
#Jin Zhou
#1091825
#This program determimes wherher the input from the user is a number or a character. If it is a character, determine whether it is in uppercase or lowercase.

#input
char = input("Enter any character:")

#processing
if (char>='0' and char<='9'):
    print("A number was entered")
elif (char >='a' and char<='z'):
    print("Lowercase character was entered")
elif(char>='A' and char<='Z'):
    print("Uppercase character was entered")
    
    
##Test run 1
##Enter any character:C
##Uppercase character was entered

##Test run 2
##Enter any character:b
##Lowercase character was entered

##Test run 3
##Enter any character:2
##A number was entered

##Test run 4
##Enter any character:t
##Lowercase character was entered

##Test run 5
##Enter any character:6
##A number was entered
