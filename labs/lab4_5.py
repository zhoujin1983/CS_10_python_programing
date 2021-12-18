#Lab 4 Question 5
#Jin Zhou
#1091825
#Write a program to create various sets


set1 = {1,2,3,4,5}
set2 = {2,4,6,8}
set3 = {1,5,9,13,17}

#a: create a new set of all elements that are in set 1 or set 2 , but not both
print("a. ", (set1^set2))

#b :create a new set of all elements that are in only one of the three sets set1,set2,set3
print("b. ", (set1|set2|set3) - (set1&set2) - (set2&set3) - (set1&set3)) 

#c :create a new set of all elements that are exactly two of the sets
all_set123 = set1&set2&set3
only_set12 = (set1&set2)-all_set123                   #the elements in only set 1 and set 2
only_set13 = (set1&set3)-all_set123                   #the elements in only set 1 and set 3
only_set23 = (set1&set2)-all_set123                   #the elements in only set 2 and set 3
print("c. ", (only_set12|only_set13|only_set23)) 

#d: create a new set of all integer elements in the range 1 to 25 that are not in set 1
new_set = set(range(1,26))                            #a set of all integer elements in the range of 1 to 25
print("d. ", new_set - set1)

#e :create a new set of all integer elements in the range 1 to 25 that are not in any of the three sets
print("e. ", new_set - (set1|set2|set3))

#f :create a new set of all integer elements in the range 1 to 25 that are not in all three sets
print("f. ", new_set - all_set123)

##Test run:
##a.  {1, 3, 5, 6, 8}
##b.  {3, 6, 8, 9, 13, 17}
##c.  {1, 2, 4, 5}
##d.  {6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}
##e.  {7, 10, 11, 12, 14, 15, 16, 18, 19, 20, 21, 22, 23, 24, 25}
##f.  {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}
