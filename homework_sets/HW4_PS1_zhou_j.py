#Homework 4 Program Set 1
#Jin Zhou
#1091825
#Program to test functions a to j.

#Define constant variables.
ONE_TEN = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]             #this is test run 1
#ONE_TEN = [12, 20, 10, 14, 54, 16, 75, 38, 79, 103]  #this is test run 2,comment
#here are 2 sample functions for item a and b         #out test run 1 and uncomment
                                                      #this line for test run 2

def swapFirstLast(data:list)->list:
    '''Function a: Swap the first and last element in a list.'''
    val = data[0]      #the temporay variable was assigned the first value of the list
    data[0] = data[-1] #the fist value of the list was replace by the last value of the list
    data[-1] = val     #the last value of the list was assined by the fist value in the temporay variable
    return data        #return the list


def shiftRight(data:list)->list:
    '''Function b: Shift the elements of list to the right.'''
    val = data[-1]     #the temporary variable was assinged the last value of the list
    for i in range(len(data)-1, 0, -1):  #use for loop to shif each elements of the list to the right
        data[i] = data[i-1]              #start from the last element
    data[0] = val                        #the first value of the list was assigned the last value of the list that was stored in the temporary variable
    return data                          #return the list


##Complete the rest of the functions from items c to j
def replaceEven(data:list)->list:
    '''Function c: replace even elements to zero.'''
    for i in range(len(data)):           #use for loop
        if data[i] % 2 == 0:             #find even numbers of the list
            data[i] = 0                  #assign zero to even numbers
    return data                          #return the list


def replaceNeighbors(data:list)->list:
    '''Function d : replace element of list with larger of its neighbor'''
    '''except 1st and last element as can see from given test run results'''
    for i in range(1, len(data)-1):      #use for loop
        if data[i-1] < data[i+1]:        #if the right neighbor is larger than the left neighbor
            data[i] = data[i+1]          #replace the element with the right neighbor
        if data[i-1] > data[i+1]:        #if the left neighbor is larger than the right neighbor
            data[i] = data[i-1]          #replace the element with the left neighbor
        if data[i-1] == data[i+1]:       #if neighbors are equal, 
            data[i] = data[i+1]          #it doesn't matter which one to replace
    return data                          #return the list


def removeMiddle(data:list)->list:
    '''Function e: remove middle elements of the data list'''
    length = len(data)                   
    if length % 2 == 0:                  #if length of list is even,
        data.remove(data[length//2])     #remove the middle two elements.
        data.remove(data[length//2-1])   
    else:                                
        data.remove(data[(length-1)//2]) #if length of list is odd,just remove the middle one.
    return data                          #return the list


def evenToFront(data:list)->list:
    '''Function f: move even elements to the front of list, while keep their order'''
    '''This is a little tricky if you want to remove several elements from the list, you need to remove from the end to start, not from start to end'''
    '''Since if you remove elements from start(left to right), then other to be deleted elements change their position '''
    '''But if you remove elements from end (right to left), then other to be deleted elements will not change their position '''
    
    odd_list = []                        # create a odd list to add odd elements
    for i in reversed(data):             # loop throuh each element in the list, from end to start
        if i%2==1:                       # if an element is odd 
            odd_list.append(i)           # add this odd element to odd list
            data.remove(i)               # remove from original list
    data += reversed(odd_list)           # append the odd list in reverse odd to the original list
    return data                          # return updated list


def secondLargest(data:list)->int:
    '''Function g: return the second largest element in the list'''

    first_largest = second_largest = data[0]         # suppose there could be negative values in list
    for i in range(1,len(data)):                     # use for loop to find the first largest element
        if data[i] > first_largest:
            first_largest = data[i]

    for i in range(len(data)):                       #use for loop to find the second largest element
        if data[i] > second_largest and data[i] != first_largest:
            second_largest = data[i]

    return second_largest


def isIncreasing(data:list)->list:
    '''Function h: check if the list is in increasing order'''
    # if the list has elements that are not strictly increasing, it will be false
    # If two consecutive elements are the same, I will not consider them are increasing.
    # If equal is also accepted, just change the <= to <
    increasing = True
    for i in range(1, len(data)):                # if the list has elements that are not strictly increasing, it will be false
        if data[i] <= data[i-1]:                 # if two consecutive elements are the same, It will not be considered as increasing.
            increasing = False                   
    return increasing                                             
            
    

def hasAdjacentDuplicate(data:list)->bool:
    '''Function i: check if elements of list has any adjacent duplicates, i.e. duplicates that next to each other'''
    has_duplicates = False
    for i in range(len(data)):
        if i == 0:
            if data[i] == data[i+1]:            # first element only has one neighbor to the right
                has_duplicates = True
        elif i == len(data)-1:
            if data[i] == data[i-1]:            # last element only has one neighbor to the left
                has_duplicates = True
        else:                                   # all other elements has one neighbor to the right and one neighbor to the left
            if data[i] == data[i+1] or data[i] == data[i-1]:
                has_duplicates = True
    return has_duplicates


def hasDuplicate(data:list)->bool:
    '''Function j: check if elements of the list has any duplicates.'''
    length_1 = len(data)
    length_2 = len(set(data))
    if length_1 == length_2:
        return False
    else:
        return True


def main():
    print("The original data for all functions is:", ONE_TEN)

    #a. Demonstrate swapping the first and last element.
    data = list(ONE_TEN)    
    swapFirstLast(data)         #call this function
    print("After swapping first and last:", data)
    
    #b. Demonstrate shifting to the right.
    data = list(ONE_TEN)
    shiftRight(data)            #call this function
    print("After shifting right:", data)

    #c. Demonstrate replacing even elements with zero.
    data = list(ONE_TEN)
    replaceEven(data)           #call this function
    print("After replacing even elements:", data)

    #d. Demonstrate replacing values with the larger of their neighbors.
    data = list(ONE_TEN)
    replaceNeighbors(data) #call this function
    print("After replacing with neighbors:", data)

    #e. Demonstrate removing the middle element.
    data = list(ONE_TEN)
    removeMiddle(data) #call this function
    print("After removing the middle element(s):", data)

    #f. Demonstrate moving even elements to the front of the list.
    data = list(ONE_TEN)
    evenToFront(data) #call this function
    print("After moving even elements:", data)

    #g. Demonstrate finding the second largest value.
    print("The second largest value is:", secondLargest(ONE_TEN))

    #h. Demonstrate testing if the list is in increasing order.
    print("The list is in increasing order:", isIncreasing(ONE_TEN))

    #i. Demonstrate testing if the list contains adjacent duplicates.
    print("The list has adjacent duplicates:", hasAdjacentDuplicate(ONE_TEN))

    #j. Demonstrate testing if the list contains duplicates.
    print("The list has duplicates:", hasDuplicate(ONE_TEN))


if __name__ == "__main__":
    main()

##Test run 1:
##The original data for all functions is: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
##After swapping first and last: [10, 2, 3, 4, 5, 6, 7, 8, 9, 1]
##After shifting right: [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
##After replacing even elements: [1, 0, 3, 0, 5, 0, 7, 0, 9, 0]
##After replacing with neighbors: [1, 3, 4, 5, 6, 7, 8, 9, 10, 10]
##After removing the middle element(s): [1, 2, 3, 4, 7, 8, 9, 10]
##After moving even elements: [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]
##The second largest value is: 9
##The list is in increasing order: True
##The list has adjacent duplicates: False
##The list has duplicates: False
##>>>

##Test run 2:
##The original data for all functions is: [12, 20, 10, 14, 54, 16, 75, 38, 79, 103]
##After swapping first and last: [103, 20, 10, 14, 54, 16, 75, 38, 79, 12]
##After shifting right: [103, 12, 20, 10, 14, 54, 16, 75, 38, 79]
##After replacing even elements: [0, 0, 0, 0, 0, 0, 75, 0, 79, 103]
##After replacing with neighbors: [12, 12, 14, 54, 54, 75, 75, 79, 103, 103]
##After removing the middle element(s): [12, 20, 10, 14, 75, 38, 79, 103]
##After moving even elements: [12, 20, 10, 14, 54, 16, 38, 75, 79, 103]
##The second largest value is: 79
##The list is in increasing order: False
##The list has adjacent duplicates: False
##The list has duplicates: False
##>>> 
    
