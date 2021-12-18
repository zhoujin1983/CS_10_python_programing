#Lab 3 Question 3
#Jin Zhou
#1091825
#write a program to find the area of a right-angled triangle using function

#a
def getData()->(float,float):
    '''let the user input base and height of a triangle'''
    base = float(input("Enter the base of your triangle: "))
    height = float(input("Enter the height of your triangle: "))
    return base,height
#b
def trigArea(base : float,height: float)->float:
    area = 0.5*base*height
    return area
#c
def displayData(base:float, height:float, area:float)->float:
    '''dispaly the data passed into the function'''
    print("The base,height,height are",format(base,'.2f'),format(height,'.2f'),format(area,'.2f'))
#d
def main():
    base,height = getData()
    area = trigArea(base,height)
    displayData(base, height, area)

if __name__ == "__main__":
    main()
    
##Test run 1    
##Enter the base of your triangle: 10
##Enter the height of your triangle: 5
##The base,height,height are 10.00 5.00 25.00
##>>> 

##Test run 2
##Enter the base of your triangle: 2
##Enter the height of your triangle: 3
##The base,height,height are 2.00 3.00 3.00
##>>> 

##Test run 3
##Enter the base of your triangle: 4
##Enter the height of your triangle: 9
##The base,height,height are 4.00 9.00 18.00
