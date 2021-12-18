#Lab 4 Question 1
#Jin Zhou
#1091825
#Write a program to create a list of numbers in the range of 1 to 10, then delete all the even numbers from the list.

def makeList()->list:
    '''function to create the list of numbers from 1 to 10'''
    data = []
    for i in range(1, 11):      #use a for loop to create the list
        data.append(i)
    return data                 #return the list


def delEven(data)->list:
    '''function to delete even numbers from list'''
    for i in data:              #use a for loop to remove the even numbers from list
        if i%2==0:
            data.remove(i)
    return data                 #return list


def main():
    data = makeList()
    print("Original List:",data)
    delEven(data)
    print("List after deleting even numbers:",data)
    
#call the main() function
if __name__ == "__main__":
    main()

##Test run 1:
##Original List: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
##List after deleting even numbers: [1, 3, 5, 7, 9]
##>>> 
