#Homework 5 Program Set 1 - OOP
#Jin Zhou
#1091825
#Program to calculate and display the loan for buying a car


class loan:
    # construct a loan class object
    def __init__(self, annualInterestRate=2.5, numberOfYears=1, loanAmount=1000, borrower="")->(float,float,float,str):
        '''initializes the annual interest rate to 2.5, number of years to 1, the loan amount to 1000'''
        self.__annualInterestRate = annualInterestRate/100   #make the data fileds private
        self.__numberOfYears = numberOfYears
        self.__loanAmount = loanAmount
        self.__borrower = borrower
        
    #create accessors for all data fields
    def get_apr(self)->float:
        """create accessor for getting the annual interest rate"""
        return self.__annualInterestRate

    def get_years(self)->float:
        '''create accessor for getting the number of years'''
        return self.__numberOfYears

    def get_amount(self)->float:
        '''create accessor for getting the loan amount'''
        return self.__loanAmount

    def get_name(self)->str:
        '''create accessor for getting the name of borrower'''
        return self.__borrower

    #create mutators for all the data fields
    def set_apr(self, annualInterestRate):
        '''create a mutator to set the annual interest rate'''
        self.__annualInterestRate = annualInterestRate

    def set_years(self, numberOfYears):
        '''create a mutator to set the number of years'''
        self.__numberOfYears = numberOfYears

    def set_amount(self, loanAmount):
        '''create a mutator to set the loan amount'''
        self.__loanAmount = loanAmount

    def set_name(self, borrower):
        '''create a mutator to set the name of borrower'''
        self.__borrower = borrower

    #create a class method
    def getMonthlyPayment(self)->float:
        '''create a function to calculate the monthly payment'''
        monlthlyInterestRate = self.__annualInterestRate/12
        monthly_payment = self.__loanAmount * monlthlyInterestRate/(1-(1/(1+monlthlyInterestRate)**(self.__numberOfYears * 12)))
        return monthly_payment

    def getTotalPayment(self)->float:
        '''create a function to calculate the total payment '''
        total_payment = self.getMonthlyPayment() * self.__numberOfYears * 12
        return total_payment

def print_loan(loan):
    '''create a function to display all the data fielsds'''
    print("The loan is for", loan.get_name())
    print("The monthly payment is", round(loan.getMonthlyPayment(), 2))
    print("the total payment is", round(loan.getTotalPayment(), 2))
    print()

def main():
    apr = float(input("Enter yearly interest rate: "))
    years = int(input("Enter number of years as an integer: "))
    amount = float(input("Enter loan amount: "))
    name = str(input("Enter a borrower's name: "))

    person_loan = loan(annualInterestRate=apr, numberOfYears=years, loanAmount=amount, borrower=name)
    print_loan(person_loan)

    again = str(input("Do you want to change the loan amount? Y for yes or enter to quit"))
    while again.lower() == "y":
        amount = float(input("Enter new loan amount: "))
        person_loan.set_amount(amount)
        print_loan(person_loan)
        print()
        again = str(input("Do you want to change the loan amount? Y for yes or enter to quit"))
        

if __name__ == '__main__':
    main()


##Test run 1
##Enter yearly interest rate: 2.5
##Enter number of years as an integer: 5
##Enter loan amount: 1000.00
##Enter a borrower's name: John Jones
##The loan is for John Jones
##The monthly payment is 17.75
##the total payment is 1064.84
##
##Do you want to change the loan amount? Y for yes or enter to quity
##Enter new loan amount: 50000
##The loan is for John Jones
##The monthly payment is 887.37
##the total payment is 53242.08
##
##
##Do you want to change the loan amount? Y for yes or enter to quit
##>>> 

##Test run 2
##Enter yearly interest rate: 1.23
##Enter number of years as an integer: 4
##Enter loan amount: 20000
##Enter a borrower's name: John Smith
##The loan is for John Smith
##The monthly payment is 427.21
##the total payment is 20506.28
##
##Do you want to change the loan amount? Y for yes or enter to quit
##>>> 

#Test run 3
##Enter yearly interest rate: 0.58
##Enter number of years as an integer: 8
##Enter loan amount: 500
##Enter a borrower's name: Alex Bob
##The loan is for Alex Bob
##The monthly payment is 5.33
##the total payment is 511.81
##
##Do you want to change the loan amount? Y for yes or enter to quity
##Enter new loan amount: 6001
##The loan is for Alex Bob
##The monthly payment is 63.99
##the total payment is 6142.75
##
##
##Do you want to change the loan amount? Y for yes or enter to quit
##>>>     

#Test run 4
##Enter yearly interest rate: 1.78
##Enter number of years as an integer: 2
##Enter loan amount: 8245
##Enter a borrower's name: Alex Wang
##The loan is for Alex Wang
##The monthly payment is 349.95
##the total payment is 8398.74
##
##Do you want to change the loan amount? Y for yes or enter to quit
##>>>

##Test run 5
##Enter yearly interest rate: 2.89
##Enter number of years as an integer: 4
##Enter loan amount: 4897
##Enter a borrower's name: Max Owen
##The loan is for Max Owen
##The monthly payment is 108.15
##the total payment is 5191.39
##
##Do you want to change the loan amount? Y for yes or enter to quity
##Enter new loan amount: 1245
##The loan is for Max Owen
##The monthly payment is 27.5
##the total payment is 1319.84
##
##
##Do you want to change the loan amount? Y for yes or enter to quit
##>>>     
