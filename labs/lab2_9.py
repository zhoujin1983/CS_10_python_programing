#Lab 2 Question 9
#Jin Zhou
#1091825
#This program caculates the sum of numbers where the user will decide how many numbers to sum

#input
count = int(input("How many numbers do you want to add?"))

#initialization
total = 0

#processing and output
for x in range(count):
    num = float(input("Enter number " + str(x+1)+":"))
    total+=num
print("The total is",format(total,'.1f'))
    

##Test run 1
##How many numbers do you want to add?3
##Enter number 1:25
##Enter number 2:34
##Enter number 3:33
##The total is 92.0
##>>> 

##Test run 2
##How many numbers do you want to add?5
##Enter number 1:12
##Enter number 2:23
##Enter number 3:74
##Enter number 4:31
##Enter number 5:10
##The total is 150.0

##Test run 3
##How many numbers do you want to add?4
##Enter number 1:1
##Enter number 2:2
##Enter number 3:3
##Enter number 4:4
##The total is 10.0

##Test run 4
##How many numbers do you want to add?2
##Enter number 1:55
##Enter number 2:410
##The total is 465.0
##>>>

##Test run 5
##How many numbers do you want to add?6
##Enter number 1:10
##Enter number 2:4
##Enter number 3:6
##Enter number 4:7
##Enter number 5:13
##Enter number 6:20
##The total is 60.0
##>>> 

