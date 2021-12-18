#Lab 2 Question 7
#Jin Zhou
#1091825
#This program validates the wholesale prices where user input and caculates retail prices

#input
cost = float(input("Enter the item's wholesale cost:"))

#validation
while cost < 0:
    print("ERROR:the cost cannot be negative")
    cost = float(input("Enter the correct wholesale cost:"))

#caculation
price = cost * 2.5
print("Retail price is $", format(price,'.2f'),sep='')

#input
item = input("Do you have another item?(Enter y for yes):")

#processing
while item != 'n' and (item =='y'or item=='Y'):
    cost = float(input("Enter the correct wholesale cost:"))
    while cost < 0:
        print("ERROR:the cost cannot be negative")
        cost = float(input("Enter the correct wholesale cost:"))
    price = cost * 2.5
    print("Retail price is $", format(price,'.2f'),sep='')
    item = input("Do you have another item?(Enter y for yes):")


##Test run 1
##Enter the item's wholesale cost:-.50
##ERROR:the cost cannot be negative
##Enter the correct wholesale cost:.50
##Retail price is $1.25
##Do you have another item?(Enter y for yes):n        
##

##Test run 2
##Enter the item's wholesale cost:.75
##Retail price is $1.88
##Do you have another item?(Enter y for yes):Y
##Enter the correct wholesale cost:.50
##Retail price is $1.25
##Do you have another item?(Enter y for yes):n
    

##Test run 3
##Enter the item's wholesale cost:-1.23
##ERROR:the cost cannot be negative
##Enter the correct wholesale cost:1.23
##Retail price is $3.08
##Do you have another item?(Enter y for yes):n

##Test run 4    
##Enter the item's wholesale cost:4.50
##Retail price is $11.25
##Do you have another item?(Enter y for yes):y
##Enter the correct wholesale cost:3.12
##Retail price is $7.80
##Do you have another item?(Enter y for yes):n
##>>> 


##Test run 5
##Enter the item's wholesale cost:4.61
##Retail price is $11.53
##Do you have another item?(Enter y for yes):y
##Enter the correct wholesale cost:-3.1
##ERROR:the cost cannot be negative
##Enter the correct wholesale cost:3.1
##Retail price is $7.75
##Do you have another item?(Enter y for yes):n
##>>> 
    
