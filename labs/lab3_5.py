#Lab 3 Question 5
#Jin Zhou
#1091825
#This program finds the sum of the single-digit numbers sequentially input without seperating 

def string_total(number_string:str)->str:
    '''find the sum of input numbers'''
    total = 0
    num = 0
    for i in range(len(number_string)):
        #covert the character to integer
        num = int(number_string[i])
        #add each number
        total+= num
    return total
    

def main():
    # Get a string of numbers as input from the user.
    number_string = input('Enter a sequence of digits with nothing separating them: ')

    # Call string_total function, and store the total.
    total = string_total(number_string)

    # Display the total.
    print('The total of the digits in the string you entered is', total)

#call the main function.
if __name__ =="__main__":
    main()

##Test run 1:
##Enter a sequence of digits with nothing separating them: 4563
##The total of the digits in the string you entered is 18
##>>> 

##Test run 2:
##Enter a sequence of digits with nothing separating them: 653214
##The total of the digits in the string you entered is 21
##>>> 

##Test run 3:
##Enter a sequence of digits with nothing separating them: 28435
##The total of the digits in the string you entered is 22
##>>> 



