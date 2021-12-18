#Lab 3 Question 1
#Jin Zhou
#1091825
#a program to print the number of birds Texas and California has by using functions

#a. create a function texas()
def texas(birds: int)->int:
    '''return the number of birds in texas'''
    print("Texas has %d birds" % (birds))

#b. create a function California()
def California(birds: int)->int:
    print("California has %d birds" % (birds))
    '''return the number of birds in California'''
    
#c. create a function main()
def main():
    texas(5000)
    California(8000)
    

if __name__ == "__main__":
    main()
 
#Test run 1
##Texas has 5000 birds
##California has 8000 birds
##>>> 

##Test run 2
##Texas has 5000 birds
##California has 8000 birds
##>>> 

##Test run 3
##Texas has 5000 birds
##California has 8000 birds
##>>> 
