#Lab 4 Question 2
#Jin Zhou
#1091825
#Write a program remove all duplicates from a list


def createList()->list:
    '''create a function to allow users to input these values into the list'''
    data = []
    for i in range(10):     #use a for loop to create a list
        val = int(input("Enter a number to be added to a list: "))
        data.append(val)
    return data             #return list


def removeDuplicates(data)->list:
    '''create a function to remove duplicate values'''
    return list(set(data)) 


def main():
    data = createList()
    print()
    print("Original List: ", data)
    data = removeDuplicates(data)
    print("List after removing duplicates : ", data)
    
#call the main() function
if __name__ == "__main__":
    main()

##Test run 1:
##Enter a number to be added to a list: 1
##Enter a number to be added to a list: 2
##Enter a number to be added to a list: 3
##Enter a number to be added to a list: 4
##Enter a number to be added to a list: 5
##Enter a number to be added to a list: 6
##Enter a number to be added to a list: 7
##Enter a number to be added to a list: 6
##Enter a number to be added to a list: 5
##Enter a number to be added to a list: 4
##
##Original List:  [1, 2, 3, 4, 5, 6, 7, 6, 5, 4]
##List after removing duplicates :  [1, 2, 3, 4, 5, 6, 7]
##>>> 
