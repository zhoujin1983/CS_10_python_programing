#Jin Zhou
#1091825
#Homework 2 Program Set 1
#This program determines whaether a single two-digit number entered by user matches the two-digit number randomly generated

import random

#generate random two-digit number
rdm = random.randint(10,100)
print("Random number is:",rdm)

#input a two-digit number
guess = int(input("Enter your lottery pick(2 digits)or -999 to quit:"))

#split two digits
rdmDg1 = rdm // 10
rdmDg2 = rdm % 10
guessDg1 = guess // 10
guessDg2 = guess % 10

#processing and output
while guess!=-999:
    if rdmDg1==guessDg1 and rdmDg2==guessDg2:
        print("Exact mathch: You win $10,000!")
    elif rdmDg1==guessDg2 and rdmDg2==guessDg1:
        print("Match all digits: You win $3,000")        
    elif rdmDg1==guessDg1 or rdmDg2==guessDg1 or rdmDg1==guessDg2 or rdmDg2==guessDg2:
        print("Match one digit: You win $1,000")
    else:
        print("Sorry no match")
    guess = int(input("Enter your lottery pick(2 digits)or -999 to quit:")) 
    guessDg1 = guess // 10
    guessDg2 = guess % 10


##Test run 1
##Random number is: 13
##Enter your lottery pick(2 digits)or -999 to quit:44
##Sorry no match
##Enter your lottery pick(2 digits)or -999 to quit:23
##Match one digit: You win $1,000
##Enter your lottery pick(2 digits)or -999 to quit:68
##Sorry no match
##Enter your lottery pick(2 digits)or -999 to quit:12
##Match one digit: You win $1,000
##Enter your lottery pick(2 digits)or -999 to quit:45
##Sorry no match
##Enter your lottery pick(2 digits)or -999 to quit:-999
##>>> 


##Test run 2
#Random number is: #32
##Enter your lottery pick(2 digits)or -999 to quit:32
##Exact mathch: You win $10,000!
##Enter your lottery pick(2 digits)or -999 to quit:23
##Match all digits: You win $3,000
##Enter your lottery pick(2 digits)or -999 to quit:65
##Sorry no match
##Enter your lottery pick(2 digits)or -999 to quit:35
##Match one digit: You win $1,000
##Enter your lottery pick(2 digits)or -999 to quit:22
##Match one digit: You win $1,000
##Enter your lottery pick(2 digits)or -999 to quit:-999
##>>> 


##Test run 3
##Random number is: 82
##Enter your lottery pick(2 digits)or -999 to quit:82
##Exact mathch: You win $10,000!
##Enter your lottery pick(2 digits)or -999 to quit:62
##Match one digit: You win $1,000
##Enter your lottery pick(2 digits)or -999 to quit:16
##Sorry no match
##Enter your lottery pick(2 digits)or -999 to quit:80
##Match one digit: You win $1,000
##Enter your lottery pick(2 digits)or -999 to quit:28
##Match all digits: You win $3,000
##Enter your lottery pick(2 digits)or -999 to quit:-999
##>>> 

##Test run 4
##Random number is: 95
##Enter your lottery pick(2 digits)or -999 to quit:45
##Match one digit: You win $1,000
##Enter your lottery pick(2 digits)or -999 to quit:60
##Sorry no match
##Enter your lottery pick(2 digits)or -999 to quit:19
##Match one digit: You win $1,000
##Enter your lottery pick(2 digits)or -999 to quit:95
##Exact mathch: You win $10,000!
##Enter your lottery pick(2 digits)or -999 to quit:59
##Match all digits: You win $3,000
##Enter your lottery pick(2 digits)or -999 to quit:-999
##>>> 

##Test run 5
##Random number is: 79
##Enter your lottery pick(2 digits)or -999 to quit:36
##Sorry no match
##Enter your lottery pick(2 digits)or -999 to quit:17
##Match one digit: You win $1,000
##Enter your lottery pick(2 digits)or -999 to quit:29
##Match one digit: You win $1,000
##Enter your lottery pick(2 digits)or -999 to quit:97
##Match all digits: You win $3,000
##Enter your lottery pick(2 digits)or -999 to quit:-999
##>>> 
