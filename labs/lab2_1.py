#Lab 2 Question 1
#Jin Zhou
#1091825
#This program determines whether a person is elligible to vote, if not, finds how many years are left to be eligible.

#input
age = int(input("Enter the age:"))

#calculate
left = 18-age

#check the age and determine
if left <= 0:
    print("You are eligible to cast your vote")
else:
    print("You have to wait for another",left,"years to cast your vote")


##Test run 1
##Enter the age:10
##You have to wait for another 8 years to cast your vote

##Test run 2
##Enter the age:25
##You are eligible to cast your vote

##Test run 3
##Enter the age:16
##You have to wait for another 2 years to cast your vote
    
##Test run 4
##Enter the age:13
##You have to wait for another 5 years to cast your vote

##Test run 5
##Enter the age:35
##You are eligible to cast your vote
