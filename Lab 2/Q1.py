'''
Lab 2 - Code 1 - Student Information.
Kattamuri V S J V S Hitesh Gupta
CS20B1127

Write a python script to implement student details using a dictionary. The roll number of the student will be the key, the value will be a list containing the name, CGPA, and mobile number of the respective student. The program should be implemented as a menu-driven program with the following menus,
1) Insert
2) Delete
3) Search
4) Exit

'''

student_names = {}  # creating an empty dictionary.
value_list = []   # creating a empty list for holding the values.

while True:
  print("\nMenu Driven Program for Dictionary : \n")
  print("   1. Insert ")
  print("   2. Delete ")
  print("   3. Search ")
  print("   4. Exit ")
  choice = int(input("\nEnter the choice : "))  # taking the choice
  
  if choice == 1 :
    key = input("\nEnter the roll number of the student to be inserted : ")
    #print(key)

    if key in student_names :
      print("\n   The given roll number is already present in the dictionary!!!")
    else :
      #print("\nEnter the Name, CGPA and the Mobile number of the student : ")
      for i in range(0,3):
        if i == 0 :
          value = input("\nEnter the name of the student : ")
          value_list.append(value)
        elif i == 1 :
          value = input("Enter the CGPA of the student : ")
          value_list.append(value)
        elif i == 2 :
          value = input("Enter the mobile number of the student : ")
          value_list.append(value)

      student_names [key] = value_list
      value_list = []
      print("\nThe dictionary after insertion is : \n", student_names)
 
  elif choice == 2 :
    key = input("\nEnter the roll number of the student to be deleted : ")
    #print(key)
    
    if key in student_names :
      print("\nThe dictionary before deletion : \n", student_names)
      student_names.pop(key)
      print("\nThe given roll number is deleted from the dictionary.")
      print("\nThe dictionary after deletion: \n", student_names)
    else :
      print("\n   The given roll number is not present in the dictionary.")

  elif choice == 3 :
    key = input("\nEnter the roll number of the student to be searched : ")
    #print(key)

    if key in student_names :
      print("\n   The given roll number is present in the dictionary.")
      print("\nThe information about the roll number", key ,"is : ", student_names[key])
    else : 
      print("   The given roll number is not present in the dictionary.")
  
  elif choice == 4 :
    print("\nThank you!\n")
    break

  else :
    print("Wrong Choice. Try Again.\n")
