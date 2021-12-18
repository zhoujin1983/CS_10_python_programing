#Jin Zhou
#1091825
#Homework 3 Program Set 1
#This program finds the amount of money Joe paid for the stock by using functions


#1. write function to get the data
def getData()->(str,int,float,float,float):
    '''let the user input the stock's name, number of shares,purchase price, selling price and commission'''
    stock_name = input("Enter Stock name: ")
    num_of_shares = int(input("Enter Number of shares :"))
    purchase_price = float(input("Enter Purchase price : "))
    selling_price = float(input("Enter Selling price : "))
    commission_in_per = float(input("Enter Commission : "))
    return stock_name,num_of_shares,purchase_price,selling_price,commission_in_per


#2. write fuctions to caculate 
def amoutPaid(num_of_shares: int,purchase_price:float)->float:
    '''caculate the amount of money Joe paid for the stock'''
    amt_buy_stocks = num_of_shares * purchase_price
    return amt_buy_stocks


def commPurchase(amt_buy_stocks: float,commission_in_per:float)->float:
    '''caculate the amount of commission Joe paid when he bought the stock'''
    commission_purchase = amt_buy_stocks * commission_in_per
    return commission_purchase


def amountSold(num_of_shares:int,selling_price:float)->float:
    '''caculate the amount of money Joe sold the stock'''
    amt_sold_stocks = num_of_shares * selling_price
    return amt_sold_stocks


def commSale(amt_sold_stocks:float,commission_in_per:float)->float:
    '''caculate the amount of commission Joe paid when he sold the stock'''
    commission_sale = amt_sold_stocks * commission_in_per
    return commission_sale


def getProfit(amt_sold_stocks:float,commission_sale:float,amt_buy_stocks:float,commission_purchase:float)->float:
    '''caculate the profit or loss'''
    profit = (amt_sold_stocks -commission_sale)-(amt_buy_stocks+commission_purchase)
    return profit


#3. write function to display the data
def displayData(stock_name:str,amt_buy_stocks:float,commission_purchase:float,amt_sold_stocks:float,commission_sale:float,profit:float)->(str,float):
    '''dispaly the data passed into the function'''
    print("Stock name : ",stock_name)
    print("Amount paid for the stock:          $",format(amt_buy_stocks,'13,.2f'))
    print("Commission paid on the purchase:    $",format(commission_purchase,'13,.2f'))
    print("Amount the stock sold for:          $",format(amt_sold_stocks,'13,.2f'))
    print("Commission paid on the sale:        $",format(commission_sale,'13,.2f'))
    print("Profit (or loss if negative):       $",format(profit,'13,.2f'))


#write the main()function to call the above functions
def main():
    #input
    info = input("Enter your stock information? Type 'y' for yes, or 'n' for no:")
    print()

    #check the input infomation is yes or no
    while info != 'n' and (info =='y'or info=='Y'):
        stock_name,num_of_shares,purchase_price,selling_price,commission_in_per = getData()
        amt_buy_stocks = amoutPaid(num_of_shares,purchase_price)
        commission_purchase = commPurchase(amt_buy_stocks,commission_in_per)
        amt_sold_stocks = amountSold(num_of_shares,selling_price)
        commission_sale = commSale(amt_sold_stocks,commission_in_per)
        profit = getProfit(amt_sold_stocks,commission_sale,amt_buy_stocks,commission_purchase)
        print()
        print()
        displayData(stock_name,amt_buy_stocks,commission_purchase,amt_sold_stocks,commission_sale,profit)
        print()
        print()
        info = input("Enter your stock information? Type 'y' for yes, or 'n' for no:")
        print()

if __name__ == "__main__":
    main()     


##Test run 1:
##Enter your stock information? Type 'y' for yes, or 'n' for no:y
##
##Enter Stock name: Kaplack, Inc.
##Enter Number of shares :10000
##Enter Purchase price : 33.92
##Enter Selling price : 35.92
##Enter Commission : 0.04
##
##
##Stock name :  Kaplack, Inc.
##Amount paid for the stock:          $    339,200.00
##Commission paid on the purchase:    $     13,568.00
##Amount the stock sold for:          $    359,200.00
##Commission paid on the sale:        $     14,368.00
##Profit (or loss if negative):       $     -7,936.00
##
##
##Enter your stock information? Type 'y' for yes, or 'n' for no:y
##
##Enter Stock name: IBM
##Enter Number of shares :15000
##Enter Purchase price : 50.25
##Enter Selling price : 100.20
##Enter Commission : 0.02
##
##
##Stock name :  IBM
##Amount paid for the stock:          $    753,750.00
##Commission paid on the purchase:    $     15,075.00
##Amount the stock sold for:          $  1,503,000.00
##Commission paid on the sale:        $     30,060.00
##Profit (or loss if negative):       $    704,115.00
##
##
##Enter your stock information? Type 'y' for yes, or 'n' for no:n
##
##>>>

##Test run 2:
##Enter your stock information? Type 'y' for yes, or 'n' for no:n
##
##>>>

    
##Test run 3:
##Enter your stock information? Type 'y' for yes, or 'n' for no:y
##
##Enter Stock name: Tesla, Inc.
##Enter Number of shares :500
##Enter Purchase price : 712.03
##Enter Selling price : 689.41
##Enter Commission : 0.05
##
##
##Stock name :  Tesla, Inc.
##Amount paid for the stock:          $    356,015.00
##Commission paid on the purchase:    $     17,800.75
##Amount the stock sold for:          $    344,705.00
##Commission paid on the sale:        $     17,235.25
##Profit (or loss if negative):       $    -46,346.00
##
##
##Enter your stock information? Type 'y' for yes, or 'n' for no:n
##
##>>>


##Test run 4:
##Enter your stock information? Type 'y' for yes, or 'n' for no:y
##
##Enter Stock name: Amazon
##Enter Number of shares :468
##Enter Purchase price : 3015.89
##Enter Selling price : 4786.12
##Enter Commission : 0.03
##
##
##Stock name :  Amazon
##Amount paid for the stock:          $  1,411,436.52
##Commission paid on the purchase:    $     42,343.10
##Amount the stock sold for:          $  2,239,904.16
##Commission paid on the sale:        $     67,197.12
##Profit (or loss if negative):       $    718,927.42
##
##
##Enter your stock information? Type 'y' for yes, or 'n' for no:y
##
##Enter Stock name: Google
##Enter Number of shares :247
##Enter Purchase price : 325.48
##Enter Selling price : 426.86
##Enter Commission : 0.04
##
##
##Stock name :  Google
##Amount paid for the stock:          $     80,393.56
##Commission paid on the purchase:    $      3,215.74
##Amount the stock sold for:          $    105,434.42
##Commission paid on the sale:        $      4,217.38
##Profit (or loss if negative):       $     17,607.74
##
##
##Enter your stock information? Type 'y' for yes, or 'n' for no:n
##
##>>> 

##Test run 5:
##Enter your stock information? Type 'y' for yes, or 'n' for no:n
##
##>>> 
