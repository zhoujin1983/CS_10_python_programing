#Lab 2 Question 10
#Jin Zhou
#1091825
#This program vonverts speed from 60kph through 130kph to mph.

#constant
CONVERSION_FACTOR = 0.6214

#print table header
print("KPH \t MPH")
print("-" * 36)

#caculation and display
for kph in range(60,140,10):
    mph = kph * CONVERSION_FACTOR
    print(kph,"\t",format(mph,'.1f'))

##Test run 1
##KPH 	 MPH
##------------------------------------
##60 	 37.3
##70 	 43.5
##80 	 49.7
##90 	 55.9
##100 	 62.1
##110 	 68.4
##120 	 74.6
##130 	 80.8
