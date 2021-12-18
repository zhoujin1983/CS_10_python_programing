#Lab 1 Question 8
#Jin Zhou
#Description of program – This program caculates the gravitional force and acceleration due to gravity of the mass input by user

#Constants for the radius and mass of the Earth, the gravitional constant
R  = 6.378e6     # meters
M1 = 5.9742e24  # kg
G  = 6.67300e-11

#input data by user
m = float(input("Enter a mass in kg:"))

#caculate the value of g
g = (G*M1*m/(R*R))/m

#Output
print("\nThe resulting value of g is",format(g,'.4f'),"which is close to the earth's gravitional force.")


##Test run 1 for Q8
##Enter a mass in kg:30
##
##The resulting value of g is 9.8001 which is close to the earth's gravitional force.
