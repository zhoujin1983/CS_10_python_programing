#Lab 4 Question 3
#Jin Zhou
#1091825
#Write a program to create a tuple of numbers and make a new tuple that has only positive values
#then sort it in descending order.

def makeTuple()->tuple:
    '''make a function to allow user to enter10 values into tuple'''
    val = str(input("Enter the values in a tuple: "))
    data = []
    for i in val.split(","):   #split each of the numbers by the comma using .split()
        data.append(int(i))
    return tuple(data)         #convert list to tuple


def makePositive(data)->tuple:
    '''make a function to store only positive elements from the list'''
    positive = []              #create a list to store all positive elements
    for i in data:
        if i>0:
            positive.append(i) #append positive elements to the list
    return tuple(sorted(positive, reverse = True))#sort the list in descending order then covert list into tuple 


def main():
    data = makeTuple()
    print()
    print("Original Tuple:", data)
    data = makePositive(data)
    print("New Tuple with Positive numbers:", data)
    
#call the main()function
if __name__ == "__main__":
    main()

##Test run 1:
##Enter the values in a tuple: -10,1,2,-9,3,4,-8,5,6,-7
##
##Original Tuple: (-10, 1, 2, -9, 3, 4, -8, 5, 6, -7)
##New Tuple with Positive numbers: (6, 5, 4, 3, 2, 1)
##>>> 
