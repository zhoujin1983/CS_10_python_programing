#Jin Zhou
#1091825
#Homework 3 Program Set 2
#This program is to check whether a credit card number is valid


def isValid(cardNumber:str)->bool:
    '''return true if the card number id valid'''
    if len(cardNumber) == 13 or len(cardNumber) == 16:    #check whether a card has 13 or 16 digits
        visa_start_valid = cardNumber.startswith("4")     #check whether the number starts with 4 visa card
        master_start_valid = cardNumber.startswith("5")   #check whether the number starts with 5 master card
        amex_start_valid = cardNumber.startswith("37")    #check whether the number starts with 37 american express card
        discover_start_valid = cardNumber.startswith("6") #check whether the number starts with 6 discover card 
        start_valid = visa_start_valid or master_start_valid or amex_start_valid or discover_start_valid #make sure it is any of above cases  

        #call sumOfDoubleEvenPlace() and sumOfOddPlace()function
        sums = sumOfDoubleEvenPlace(cardNumber) + sumOfOddPlace(cardNumber)

        #check whether the result is divided by 10
        if start_valid and sums%10==0:  
            return True
        else:
            return False
    else:
        return False

    
def sumOfDoubleEvenPlace(cardNumber:str)->str:
    '''return the sum of double even place of the credit card number'''
    total = 0

    #double every second digit from right to left then add all single-digit numbers
    for i in range(-2, -len(cardNumber)-1, -2):
        total += getDigit(int(cardNumber[i])*2)
    return total

    
def sumOfOddPlace(cardNumber:str)->str:
    '''return the sum of odd place digits in number'''
    total = 0
    
    #add all digits in the odd places from right to left
    for i in range(-1, -len(cardNumber)-1, -2): 
        total += int(cardNumber[i])
    return total

 
def getDigit(number:int)->int:
    '''receive the (even place number*2) from sumOfDoubleEvenPlace()'''

    #check this number if it is a single digit, if true return this number
    # otherwise keep on with summing two digits
    while len(str(number))!=1: 
        number = int(str(number)[0])+int((str(number)[1]))
    
    return number 


def main():
    #prompt the user for how many numbers he/she wants to check
    count = int(input("How many credit card numbers do you want to check? "))

    #allow the user enter multiple credit card numbers to test for validity
    for i in range(count):
        #user will input the credit card number as a string
        cardNumber = input("Enter a credit card number: ")
        
        #call the function isValid and print whether the credit card number is valid or not
        if isValid(cardNumber):   
            print(cardNumber, 'is valid')
        else:
            print(cardNumber, 'is invalid')
        print()


#call the main function
if __name__ == "__main__":
    main()


##Test run 1:
##How many credit card numbers do you want to check? 2
##Enter a credit card number: 4388576018402626
##4388576018402626 is invalid
##
##Enter a credit card number: 4388576018410707
##4388576018410707 is valid
##>>>

##Test run 2:
##How many credit card numbers do you want to check? 0
##>>> 

##Test run 3:
##How many credit card numbers do you want to check? 3
##Enter a credit card number: 12345678
##12345678 is invalid
##
##Enter a credit card number: 5169769005222217
##5169769005222217 is valid
##
##Enter a credit card number: 6011655276746808
##6011655276746808 is invalid
##>>> 

##Test run 4:
##How many credit card numbers do you want to check? 4
##Enter a credit card number: 426287961253
##426287961253 is invalid
##
##Enter a credit card number: 582136547
##582136547 is invalid
##
##Enter a credit card number: 7852142
##7852142 is invalid
##
##Enter a credit card number: 4246315295683260
##4246315295683260 is valid
##>>> 

##Test run 5:
##How many credit card numbers do you want to check? 2
##Enter a credit card number: 4246315295682080
##4246315295682080 is valid
##
##Enter a credit card number: 7324158
##7324158 is invalid
##>>>     
