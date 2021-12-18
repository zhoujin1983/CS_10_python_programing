#Lab 3 Question 2
#Jin Zhou
#1091825
#write a program to caculate the interest using function

#a. write a function to take in 3 arguments
def show_interest(principal:float, rate:float, periods:int)->float:
    '''caculate and print the interest using this 3 arguments'''
    interest = principal*rate*periods
    print("The simple interest will be $",format(interest,',.2f'),sep='')

#b. write the main function to call the show_interest function with default arguments
def main():
    show_interest(principal=10000.00,rate=0.01,periods=10)

if __name__ == "__main__":
    main()


##Test run 1:
##The simple interest will be $1,000.00
##>>>     

##Test run 2:
##The simple interest will be $1,000.00
##>>> 

##Test run 3:
##The simple interest will be $1,000.00
##>>> 
    
