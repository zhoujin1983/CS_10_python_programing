#Lab 1 Question 6
#Jin Zhou
#This program displays a cookie recipe according to the specific number of cookies input by user

#Constants for ingredients
SUGAR_FOR_48_COOKIES  = 1.5  #cups
BUTTER_FOR_48_COOKIES = 1    #cupS
FLOUR_FOR_48_COOKIES  = 2.75 #cups

#Input data by user
num_of_cookies = int(input("Enter the number of cookies:"))

#caculate the amount of sugar you need
sugar_amt = SUGAR_FOR_48_COOKIES / 48 * num_of_cookies

#caculate the amount of butter you nedd
butter_amt = BUTTER_FOR_48_COOKIES /48 * num_of_cookies

#caculate the amount of flour you need
flour_amt = FLOUR_FOR_48_COOKIES /48 * num_of_cookies

#Output
print("\nTo make", format(num_of_cookies,'.1f'),"cookies, you will need:")
print(format(sugar_amt, '.2f'),"cups of sugar")
print(format(butter_amt, '.2f'),"cups of butter")
print(format(flour_amt, '.2f'),"cups of flour")


##Test run 1 for Q6 
##Enter the number of cookies:56
##
##To make 56.0 cookies, you will need:
##1.75 cups of sugar
##1.17 cups of butter
##3.21 cups of flour


##Test run 2 for Q6
##Enter the number of cookies:36
##
##To make 36.0 cookies, you will need:
##1.12 cups of sugar
##0.75 cups of butter
##2.06 cups of flour


##Test run 3 for Q6
##Enter the number of cookies:100
##
##To make 100.0 cookies, you will need:
##3.12 cups of sugar
##2.08 cups of butter
##5.73 cups of flour
