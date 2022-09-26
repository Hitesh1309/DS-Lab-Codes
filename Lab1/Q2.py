'''
Q2) Write a program to search for a value ‘k’ in a list of ‘n’ elements using binary search.
sort() function can be used to sort the list. Maintain proper boundary conditions.

'''

'''
Binary Search - Binary Search is a searching algorithm used in a sorted array by repeatedly dividing the search interval in half.

'''


x = int(input("Enter the size of the list : "))
print(x)

list1 = []

for i in range (0,x):
    print("Enter element number-", i+1 ,": ")
    value = int(input())
    list1.append(value)
print("Entered list is : ", list1)

var = int(input("Enter the number to be searched : "))
#print(var)

list1.sort() #sorts the list
print("\nThe list after sorting is : ",list1)

first = 0
last = x-1
found = False

while first<=last and not found:
    pos = 0
    midpoint = (first + last)//2 #finds index of midpoint
    if list1[midpoint] == var:
        pos = midpoint
        found = True
    else:
        if var < list1[midpoint]:
            last = midpoint-1
        else:
            first = midpoint+1
            
if found == True :
    print("\nThe number is found at index : ", pos)
else:
    print("\nThe number is not found.")




'''
Example -

list = [6, 5, 4, 3, 2, 1]

val = -3

sorted list = [1, 2, 3, 4, 5, 6]

loop 1 => -3!=4 (first midpoint) and -3<4 => [1, 2, 3]

loop 2 => -3!=2 (second midpoint) and -3<2 => [1, 2]

loop 3 => -3!=1 (third midpoint) [1] and nothing left in the list so element not present in the list.

'''
