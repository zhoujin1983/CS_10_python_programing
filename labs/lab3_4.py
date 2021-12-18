#Lab 3 Question 4
#Jin Zhou
#1091825
# This program calculates a salesperson's pay

def get_sales()->float:
    sales = float(input("Enter the monthly sales:"))
    '''let the user input the amount of sales'''
    return sales

def get_advanced_pay()->float:
    print("Enter the amount of advanced pay,or")
    print("enter 0 if no advanced pay was given.")
    advanced_pay = float(input("Advanced pay:"))
    '''load the amount of advanced pay input by user '''
    return advanced_pay

def determine_comm_rate(sales:float)->float:
    '''determine the rate based on the sales'''
    if  0<=sales<10000.00:
        comm_rate = 0.10
        return comm_rate
    if 10000.00<=sales<=14999.99:
        comm_rate = 0.12
        return comm_rate
    if 15000.00<=sales<=17999.99:
        comm_rate = 0.14
        return comm_rate
    if 18000.00<=sales<=219999.99:
        comm_rate = 0.16
        return comm_rate
    else:
        comm_rate = 0.18
        return comm_rate

        
def main():
    # Get the amount of sales from user
    sales = get_sales()

    #Get the amount of advanced pay from user.
    advanced_pay = get_advanced_pay()

    #Determine the commission rate.
    comm_rate = determine_comm_rate(sales)

    #Calculate the pay.
    pay = sales * comm_rate - advanced_pay

    #Display the amount of pay.
    print('The pay is $', format(pay, ',.2f'), sep='')

    #Determine whether the pay is negative.
    if pay < 0:
        print('The salesperson must reimburse')
        print('the company.')

if __name__=="__main__":
    main()


##Test run 1:
##Enter the monthly sales:14550.00
##Enter the amount of advanced pay,or
##enter 0 if no advanced pay was given.
##Advanced pay:1000.00
##The pay is $746.00
##>>> 


##Test run 2:
##Enter the monthly sales:9500
##Enter the amount of advanced pay,or
##enter 0 if no advanced pay was given.
##Advanced pay:0
##The pay is $950.00
##>>> 

##Test run 3:
##Enter the monthly sales:12000.00
##Enter the amount of advanced pay,or
##enter 0 if no advanced pay was given.
##Advanced pay:2000.00
##The pay is $-560.00
##The salesperson must reimburse
##the company.
##>>> 
