#Jin Zhou
#1091825
#Homework 1 Program Set 1
#This program finds the monthly payment and total payment where the annual interest rate, the number of years and loan ammount are input by user

#Data/input
annual_int_rate = float(input("Enter annual interest rate,(e.g., 7.25):"))
years =int(input("Enter number of years as an integer,(e.g., 5):"))
loan_amt =float(input("Enter loan ammount,(e.g., 120000.95):"))

#Processing/Calculations
monthly_int_rate = annual_int_rate / 1200
monthly_payment = loan_amt * monthly_int_rate /(1-1/(1+ monthly_int_rate)**(years * 12))
totalPayment =  monthly_payment * years * 12

#output
print("The monthly payment is", format(monthly_payment,',.2f'))
print("The total payment is", format(totalPayment,',.2f'))


##Test run 1
##
##Enter annual interest rate,(e.g., 7.25):4.5
##Enter number of years as an integer,(e.g., 5):30
##Enter loan ammount,(e.g., 120000.95):350000.50
##The monthly payment is 1,773.40
##The total payment is 638,424.40


##Test run 2
##
##Enter annual interest rate,(e.g., 7.25):2.25
##Enter number of years as an integer,(e.g., 5):25
##Enter loan ammount,(e.g., 120000.95):425600.35
##The monthly payment is 1,856.17
##The total payment is 556,852.13


##Test run 3
##
##Enter annual interest rate,(e.g., 7.25):3.45
##Enter number of years as an integer,(e.g., 5):50
##Enter loan ammount,(e.g., 120000.95):123456789.05
##The monthly payment is 432,121.45
##The total payment is 259,272,872.88


##Test run 4
##Enter annual interest rate,(e.g., 7.25):4.25
##Enter number of years as an integer,(e.g., 5):27
##Enter loan ammount,(e.g., 120000.95):500125.23
##The monthly payment is 2,597.46
##The total payment is 841,577.08


##Test run 5
##Enter annual interest rate,(e.g., 7.25):4.86
##Enter number of years as an integer,(e.g., 5):27
##Enter loan ammount,(e.g., 120000.95):500021.36
##The monthly payment is 2,773.87
##The total payment is 898,733.52
##
