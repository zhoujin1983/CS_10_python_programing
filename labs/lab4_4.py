#Lab 4 Question 4
#Jin Zhou
#1091825
#Write a program using list to read a sequence of string values and prints them and
#highlighting the largest number

def readValues():
    '''create a function to read a sequence of string values'''
    data = []                                           #create a list
    value = input("Please enter values, Q to quit:\n")  #input values by user
    while value !='Q':                                  #use a while loop to create list,if enters "Q" exit the loop
        if '.' in value:                                #if there's a '.' in the value,cast it as float
            data.append(float(value))                   
        else:                                           #else cast it as integer
            data.append(int(value))
        value = input()
    return data


def findLargest(data)->float:
    '''create a function to find the largest value'''
    max_val = data[0]                                   #initialization the max value
    for i in range(1,len(data)):                        #use a for loop to find the largest value
        if data[i]>max_val:
            max_val = data[i]
    return max_val


def display(data):
    '''create a function to dispaly the list'''
    max_val=findLargest(data)                          #call the function findLargest()to find the max value
    print("Here are the numbers in the list")          #output values
    for i in data:                                     #use a for loop to check if it is the largest
        if i==max_val:
            print(i, "<== this is the largest number") #if is the largest, highlight the largest value
        else:
            print(i) 


def main():
    data = readValues()
    print()
    display(data)
    

#call the main() function
if __name__ == "__main__":
    main()


##Test run 1:
##Please enter values, Q to quit:
##34
##56.7
##4
##9
##76.9
##55.4
##Q
##
##Here are the numbers in the list
##34
##56.7
##4
##9
##76.9 <== this is the largest number
##55.4
##>>> 
