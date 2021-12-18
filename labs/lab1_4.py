#Lab 1 Question 4
#Jin Zhou
#1091825
#This program caculates the area and volume of a cylinder where the radius and the length are input by user

#Constants for PI
PI = 3.141

#Input data by user
radius = float(input("Enter the radius of a cylinder:"))
length = float(input("Enter the length of a cylinder:"))

#Calculate the area of cylinder
area = radius * radius * PI

#Caculate the volume of cylinder
volume = area * length

#Output
print ("The area is", format(area, '.5f'))
print ("The volume is", format(volume, '.3f'))


##Test run 1 for Q4
##Enter the radius of the cylinder:5.5
##Enter the length of the cylinder:12
##The area is 95.01525
##The volume is 1140.183


##Test run 2 for Q4
##Enter the radius of the cylinder:14.6
##Enter the length of the cylinder:20
##The area is 669.53556
##The volume is 13390.711


##Test run 3 for Q4
##Enter the radius of the cylinder:7.6
##Enter the length of the cylinder:5
##The area is 181.42416
##The volume is 907.121
