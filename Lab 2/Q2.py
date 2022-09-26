'''
Lab 2 - Code 2 - Set Operations.
Kattamuri V S J V S Hitesh Gupta
CS20B1127

Write a python program to implement set operations using menu-driven programming. The menus to be implemented are as follows,
1) Create Empty Set
2) Insert
3) Delete
4) Search
5) Print
6) Union
7) Intersection
8) Set Difference
9) Symmetric Difference
10) Exit

'''

set_names = {} # creating an empty dictionary.

while True:
  print("\nMenu Driven Program for Set Operations : \n")
  print("   1. Create Empty Set ")
  print("   2. Insert ")
  print("   3. Delete ")
  print("   4. Search ")
  print("   5. Print ")
  print("   6. Union ")
  print("   7. Intersection ")
  print("   8. Set Difference ")
  print("   9. Symmetric Difference ")
  print("   10. Exit ")
  choice = int(input("\nEnter the choice : "))

  if choice == 1 :
    name = input("Enter the name of the set you want to create : ")
    value_set = set()
    if name not in set_names.keys() :
      set_names.update({name: value_set})
      print(set_names)
    else : 
      print("The set already exists.")

  elif choice == 2 :
    name = input("Enter the name of the set you want to insert : ")
    if name in set_names.keys() :
      num = int(input("Enter the number of values you want to enter : "))
      for i in range(0,num) :
        value = input("Enter the value : ")
        set_names[name].add(value)
    else : 
      print("The given set doesn't exists, create it using option 1.")

    print(set_names)

  elif choice == 3 :
    name = input("Enter the name of the set you want to delete : ")
    if name in set_names.keys() :
      value = input("Enter the value : ")
      set_names[name].discard(value)
    else : 
      print("The given set doesn't exists, create it using option 1.")

    print(set_names)

  elif choice == 4 :
    name = input("Enter the name of the set to be searched for : ")
    if name in set_names.keys() :
      value = input("Enter the value : ")
      if value in set_names[name] :
        print("The given value exists in the set.")
      else :
        print("The given value is not present in the set.")
    else : 
      print("The given set doesn't exists, create it using option 1.")

  elif choice == 5 : 
    name = input("Enter the name of the set you want to print : ")
    if name in set_names.keys() :
        print(set_names[name])
    else : 
      print("The given set doesn't exists, create it using option 1.")

  elif choice == 6 :
    name1 = input("Enter the name of the set 1 you want to do union : ")
    if name1 not in set_names.keys() :
      print("The set",name1,"is not present.")
      break
    name2 = input("Enter the name of the set 2 you want to do union : ")
    if name2 not in set_names.keys() :
      print("The set",name2,"is not present.")
      break
    print(set_names[name1])
    print(set_names[name2])
    print("The Union of the sets is : ", set_names[name1].union(set_names[name2]))

  elif choice == 7 :
    name1 = input("Enter the name of the set 1 you want to do intersection : ")
    name2 = input("Enter the name of the set 2 you want to do intersection : ")

    print("The Intersection of the sets is : ", set_names[name1].intersection(set_names[name2]))
    
  elif choice == 8 :
    name1 = input("Enter the name of the set 1 you want to do set difference : ")
    name2 = input("Enter the name of the set 2 you want to do set difference : ")

    print(set_names[name1])
    print(set_names[name2])
    print("The Set Difference of the sets is : ", set_names[name1].difference(set_names[name2]))

  elif choice == 9 :
    name1 = input("Enter the name of the set 1 you want to do symmetric difference : ")
    name2 = input("Enter the name of the set 2 you want to do symmetric difference : ")

    print(set_names[name1])
    print(set_names[name2])
    print("The Symmetric Difference of the sets is : ", set_names[name1].symmetric_difference(set_names[name2]))

  elif choice == 10 :
    break

  else :
    print("Wrong Choice")