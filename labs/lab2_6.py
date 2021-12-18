#Lab 2 Question 6
#Jin Zhou
#1091825
#This program caculates the property tax based the lot number and property value input by the user

#constant
TAX_FACTOR = 0.0065
print("Enter the property lot number or enter -999 to end")

#input
lot_num = int(input("Enter the lot number:"))

#processing and output
while lot_num !=-999:
    value = float(input("Enter property value:"))
    tax = value*TAX_FACTOR
    print("Property tax:",format(tax,'.2f'))
    print("\nEnter the property lot number or enter -999 to end")
    lot_num = int(input("Enter the lot number:"))
print(" ")

##Test run 1
##Enter the property lot number or enter -999 to end
##Enter the lot number:100
##Enter property value:100000.00
##Property tax: 650.00
##
##Enter the property lot number or enter -999 to end
##Enter the lot number:200
##Enter property value:5000.00
##Property tax: 32.50
##
##Enter the property lot number or enter -999 to end
##Enter the lot number:-999
## 

##Test run 2
##Enter the property lot number or enter -999 to end
##Enter the lot number:300
##Enter property value:64582.03
##Property tax: 419.78
##
##Enter the property lot number or enter -999 to end
##Enter the lot number:-999

##Test run 3
##Enter the property lot number or enter -999 to end
##Enter the lot number:300
##Enter property value:1526398.23
##Property tax: 9921.59
##
##Enter the property lot number or enter -999 to end
##Enter the lot number:700
##Enter property value:100000.00
##Property tax: 650.00
##
##Enter the property lot number or enter -999 to end
##Enter the lot number:-999
 
##Test run 4
##Enter the property lot number or enter -999 to end
##Enter the lot number:5
##Enter property value:1000
##Property tax: 6.50
##
##Enter the property lot number or enter -999 to end
##Enter the lot number:-999

##Test run 5
##Enter the property lot number or enter -999 to end
##Enter the lot number:600
##Enter property value:3000
##Property tax: 19.50
##
##Enter the property lot number or enter -999 to end
##Enter the lot number:-999
