#Lab 2 Question 5
#Jin Zhou
#1091825
#This program prints the number of horizontal asterisks input by user.

#input
num = int(input("How many stars you want?"))
start_num =1

#processing and output
while start_num<=num:
    print("*",end='')
    start_num+=1

##Test run 1
##How many stars you want?20
##********************

##Test run 2
##How many stars you want?5
##*****

##Test run 3
##How many stars you want?15
##***************

##Test run 4
##How many stars you want?3
##***
    
##Test run 5
##How many stars you want?9
##*********
