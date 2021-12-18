#Lab 1 Question 7
#Jin Zhou
#Description of program - This program displays the four-digit number input by user in reverse order

#input data by user
num_input = int(input("Enter an integer: "))

#find the last digit of this number
last =int(num_input % 10)

#find the third digit of the number
third =int((num_input / 10)%10)

#find the second digit of the number
second =int((num_input / 100)%10)

#find the first digit of the number
first =int((num_input / 1000)%10)

#Output
print(last)
print(third)
print(second)
print(first)


##Test run 1 for Q7
##Enter an integer: 3125
##5
##2
##1
##3


##Test run 2 for Q7
##Enter an integer: 4798
##8
##9
##7
##4


##Test run 3 for Q7
##Enter an integer: 3589
##9
##8
##5
##3






