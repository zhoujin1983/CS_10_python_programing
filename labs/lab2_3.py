#Lab 2 Question 3
#Jin Zhou
#1091825
#This program finds whether the character entered is a vowel or not

#input
letter = input("Enter any character:")

#check whether the character is a vowel or not
if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
    print(letter,"is a vowel")
else:
    print(letter,"is not a vowel")


##Test run 1
##Enter any character:h
##h is not a vowel

##Test run 2
##Enter any character:e
##e is a vowel

##Test run 3
##Enter any character:k
##k is not a vowel

##Test run 4
##Enter any character:u
##u is a vowel

##Test run 5
##Enter any character:o
##o is a vowel
