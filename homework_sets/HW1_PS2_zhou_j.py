#Jin Zhou
#1091825
#Homework 1 Program Set 2
#This program finds the amount of money Kool Doode paid for the stock.

#Data/input
stock_name = input("Enter Stock name: ")
num_of_shares = int(input("Enter Number of shares :"))
purchase_price = float(input("Enter Purchase price : "))
selling_price = float(input("Enter Selling price : "))
commission_in_per = float(input("Enter Commission : "))

#Calculations
amt_buy_stocks = num_of_shares * purchase_price
commission_purchase = amt_buy_stocks * commission_in_per
amt_sold_stocks = num_of_shares * selling_price
commission_sale = amt_sold_stocks * commission_in_per
profit = (amt_sold_stocks -commission_sale)-(amt_buy_stocks+commission_purchase)

#Output
print("Amount paid for the stock:          $",format(amt_buy_stocks,'13,.2f'))
print("Commission paid on the purchase:    $",format(commission_purchase,'13,.2f'))
print("Amount the stock sold for:          $",format(amt_sold_stocks,'13,.2f'))
print("Commission paid on the sale:        $",format(commission_sale,'13,.2f'))
print("Profit (or loss if negative):       $",format(profit,'13,.2f'))


##Test run 1
##Enter Stock name: Kaplack, Inc.
##Enter Number of shares :10000
##Enter Purchase price : 33.92
##Enter Selling price : 35.92
##Enter Commission : 0.04
##Amount paid for the stock:          $    339,200.00
##Commission paid on the purchase:    $     13,568.00
##Amount the stock sold for:          $    359,200.00
##Commission paid on the sale:        $     14,368.00
##Profit (or loss if negative):       $     -7,936.00


##Test run 2
##Enter Stock name: IBM
##Enter Number of shares :15000
##Enter Purchase price : 50.25
##Enter Selling price : 100.20
##Enter Commission : 0.02
##Amount paid for the stock:          $    753,750.00
##Commission paid on the purchase:    $     15,075.00
##Amount the stock sold for:          $  1,503,000.00
##Commission paid on the sale:        $     30,060.00
##Profit (or loss if negative):       $    704,115.00

##Test run 3
##Enter Stock name: Amazon
##Enter Number of shares :20000
##Enter Purchase price : 3277.71
##Enter Selling price : 3524.32
##Enter Commission : 0.05
##Amount paid for the stock:          $ 65,554,200.00
##Commission paid on the purchase:    $  3,277,710.00
##Amount the stock sold for:          $ 70,486,400.00
##Commission paid on the sale:        $  3,524,320.00
##Profit (or loss if negative):       $ -1,869,830.00

##Test run 3
##Enter Stock name: Tesla
##Enter Number of shares :50000
##Enter Purchase price : 816.12
##Enter Selling price : 1000.23
##Enter Commission : 0.04
##Amount paid for the stock:          $ 40,806,000.00
##Commission paid on the purchase:    $  1,632,240.00
##Amount the stock sold for:          $ 50,011,500.00
##Commission paid on the sale:        $  2,000,460.00
##Profit (or loss if negative):       $  5,572,800.00

##Test run 4
##Enter Stock name: Facebook
##Enter Number of shares :60123
##Enter Purchase price : 156.84
##Enter Selling price : 270.50
##Enter Commission : 0.05
##Amount paid for the stock:          $  9,429,691.32
##Commission paid on the purchase:    $    471,484.57
##Amount the stock sold for:          $ 16,263,271.50
##Commission paid on the sale:        $    813,163.58
##Profit (or loss if negative):       $  5,548,932.04

##Test run 5
##Enter Stock name: Google
##Enter Number of shares :4000
##Enter Purchase price : 136.76
##Enter Selling price : 150.94
##Enter Commission : 0.04
##Amount paid for the stock:          $    547,040.00
##Commission paid on the purchase:    $     21,881.60
##Amount the stock sold for:          $    603,760.00
##Commission paid on the sale:        $     24,150.40
##Profit (or loss if negative):       $     10,688.00
##
