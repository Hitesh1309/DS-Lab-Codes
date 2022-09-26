'''
Q1) Write a python program to sort a list of ‘n’ elements using insertion sort. Do not use sort() function. Maintain proper boundary conditions.

'''

'''
Insertion Sort -

Insertion sort is the sorting mechanism where the sorted array/list is built having one item at a time.
The left side of the list/array is always sorted.

'''


x = int(input("Enter the size of the list : "))
print(x)

list1 = []

for i in range (0,x):
    print("Enter element number-", i+1 ,": ")
    value = int(input())
    list1.append(value)
print("Entered list is : ", list1)

for i in range(1,x):

  currentvalue = list1[i]
  pos = i

  while pos>0 and list1[pos-1]>currentvalue:
    list1[pos]=list1[pos-1]
    pos = pos-1  

  list1[pos]=currentvalue
  #print("\n", list1)

print("\nThe list after sorting using insertion sort is : ", list1)



'''
Example -

list = [11, 13, 5, 12, 62]

loop 1 - [11, 13, 5, 12, 62] compares - 11 and 13

loop 2 - [5, 11, 13, 12, 62] compares - 5 and 13 swaps it and then 11 and 5

loop 3 - [5, 11, 12, 13, 62] compares - 12 and 13 swaps it

loop 4 - [5, 11, 12, 13, 62] compares - 13 and 62

''' 
