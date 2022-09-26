'''
Lab 5 - Code 1 - Numpy Arrays.
Kattamuri V S J V S Hitesh Gupta
CS20B1127

Write a python program to perform matrix operations on an M x N matrix and solve a system of linear equations. Use inbuilt functions to implement the operations. Get two matrices from the user. The program should support the following Menus,

1) Matrix Addition
2) Matrix Subtraction
3) Scalar Matrix Multiplication
4) Elementwise Matrix Multiplication
5) Matrix Multiplication
6) Matrix Transpose
7) Trace of a Matrix
8) Solve System of Linear Equations
9) Determinant
10) Inverse
11) Singular Value Decomposition
12) Eigen Value
13) Search an Element
14) Difference of Sum of Upper and Lower Triangular Matrix
15) Exit
'''

import os
import numpy as np

# Taking input for matrix 1.
num_row1 = int(input("Enter the number of rows of first matrix : "))
num_col1 = int(input("Enter the number of columns of first matrix : "))

list1 = []
for i in range(0,(num_row1*num_col1)):
  inp = int(input("Enter the element : "))
  list1.append(inp)

# Taking input for matrix 2.
num_row2 = int(input("\nEnter the number of rows of second matrix : "))
num_col2 = int(input("Enter the number of columns of second matrix : "))

list2 = []
for i in range(0,(num_row2*num_col2)):
  inp = int(input("Enter the element : "))
  list2.append(inp)

os.system('cls')

# Changing the input into numpy arrays and reshaping them into matrices.
x1 = np.array(list1)
matrix_1 = np.reshape(x1,(num_row1,num_col1))
print("\nThe first matrix is : \n", matrix_1)

x2 = np.array(list2)
matrix_2 = np.reshape(x2,(num_row2,num_col2))
print("\nThe second matrix is : \n", matrix_2)

# Menu for the options.
while(1):

  print("\n--------------Menu---------------")
  print("1) Matrix Addition.")
  print("2) Matrix Subtraction.")
  print("3) Scalar Matrix Multiplication.")
  print("4) Elementwise Matrix Multiplication.")
  print("5) Matrix Multiplication.")
  print("6) Matrix Transpose.")
  print("7) Trace of a Matrix.")
  print("8) Solve System of Linear Equations.")
  print("9) Determinant.")
  print("10) Inverse.")
  print("11) Singular Value Decomposition.")
  print("12) Eigen Value.")
  print("13) Search an Element.")
  print("14) Difference of Sum of Upper and Lower Traingular Matrix.")
  print("15) Exit.") 

  num = int(input("Enter your choice : "))

  if num == 1 :
    os.system('cls')
    try :
      print("\nThe first matrix is : \n", matrix_1)
      print("\nThe second matrix is : \n", matrix_2)
      print("\n***********************************************")

      val1 = matrix_1+matrix_2
      print("\nThe Matrix Addition of the given matrices is : \n", val1)
      
    except :
      print("\nError!!! Check the dimensions of the matrices.")

  elif num == 2 :
    os.system('cls')
    try :
      print("\nThe first matrix is : \n", matrix_1)
      print("\nThe second matrix is : \n", matrix_2)
      print("\n***********************************************")

      val2 = matrix_1-matrix_2
      print("\nThe Matrix Subtraction of the given matrices is : \n", val2) 
    except :
      print("\nError!!! Check the dimensions of the matrices.")

  elif num == 3:
    os.system('cls')
    try :
      print("\nThe first matrix is : \n", matrix_1)
      print("\nThe second matrix is : \n", matrix_2)
      print("\n***********************************************")

      val = int(input("\nEnter the scalar value to mulitply the matrix with : "))
      choice = int(input("Enter 1 for first matrix and 2 for second matrix : "))
      if choice == 1:
        val3 = val*matrix_1
        print("\nThe Output after Scalar Multiplication is : \n",val3)
      elif choice == 2:
        val3 = val*matrix_2
        print("\nThe Output after Scalar Multiplication is : \n",val3)
      else :
        print("\nEnter a valid choice!!!")
    except :
      print("\nError!!! Please Enter an Integer Value.")
    
  elif num == 4 :
    os.system('cls')
    try :
      print("\nThe first matrix is : \n", matrix_1)
      print("\nThe second matrix is : \n", matrix_2)
      print("\n*******************************************************")
      
      val4 = matrix_1*matrix_2
      print("\nThe Output after Elementwise Matrix Multiplication is : \n",val4)
    except :
      print("Error!!! Check the dimensions of the matrices. ")
  
  elif num == 5 :
    os.system('cls')
    try :
      print("\nThe first matrix is : \n", matrix_1)
      print("\nThe second matrix is : \n", matrix_2)
      print("\n*******************************************************")
      
      val5 = matrix_1@matrix_2
      # val5 = matrix_1.dot(matrix_2)
      print("The Output after Matrix Multiplication is : \n",val5)
    except :
      print("Error!!! Check the dimensions of the matrices. ")

  elif num == 6 :
    os.system('cls')
    try :
      print("\nThe first matrix is : \n", matrix_1)
      print("\nThe second matrix is : \n", matrix_2)
      print("\n*******************************************************")

      choice = int(input("Enter 1 for first matrix and 2 for second matrix : "))
      if choice == 1:
        val6 = matrix_1.transpose()
        print("The Transpose of the Matrix 1 is : \n",val6)
      elif choice == 2:
        val6 = matrix_2.transpose()
        print("The Transpose of the Matrix 2 is : \n",val6)
      else :
        print("Enter a valid choice!!!")   
    except :
      print("Error!!!")  

  elif num == 7 :
    os.system('cls')
    try :
      print("\nThe first matrix is : \n", matrix_1)
      print("\nThe second matrix is : \n", matrix_2)
      print("\n*******************************************************")

      choice = int(input("Enter 1 for first matrix and 2 for second matrix : "))
      if choice == 1:
        val7 = matrix_1.trace()
        print("The Trace of the Matrix 1 is : ",val7)
      elif choice == 2:
        val7 = matrix_2.trace()
        print("The Trace of the Matrix 2 is : ",val7)
      else :
        print("Enter a valid choice!!!")
    except :
      print("Error!!!")

  elif num == 8 :
    os.system('cls')
    try :
      print("\nThe first matrix is : \n", matrix_1)
      print("\nThe second matrix is : \n", matrix_2)
      print("\n*******************************************************")

      val8 = np.linalg.solve(matrix_1,matrix_2)
      print("The Solution of the System of Linear Equations is : \n",val8)
    except :
      print("Error!!!") 

  elif num == 9 :
    os.system('cls')
    try :
      print("\nThe first matrix is : \n", matrix_1)
      print("\nThe second matrix is : \n", matrix_2)
      print("\n*******************************************************")

      choice = int(input("Enter 1 for first matrix and 2 for second matrix : "))
      if choice == 1:
        val9 = np.linalg.det(matrix_1)
        print("The Determinant of the Matrix 1 is : ",val9)
      elif choice == 2:
        val9 = np.linalg.det(matrix_2)
        print("The Determinant of the Matrix 2 is : ",val9)
      else :
        print("Enter a valid choice!!!")
    except :
      print("Error!!!")

  elif num == 10 :
    os.system('cls')
    try :
      print("\nThe first matrix is : \n", matrix_1)
      print("\nThe second matrix is : \n", matrix_2)
      print("\n*******************************************************")

      choice = int(input("Enter 1 for first matrix and 2 for second matrix : "))
      if choice == 1:
        val10 = np.linalg.inv(matrix_1)
        print("The Inverse of the Matrix 1 is : \n",val10)
      elif choice == 2:
        val10 = np.linalg.inv(matrix_2)
        print("The Inverse of the Matrix 2 is : \n",val10)
      else :
        print("Enter a valid choice!!!")
    except :
      print("Error!!!") 

  elif num == 11 :
    os.system('cls')
    try :
      print("\nThe first matrix is : \n", matrix_1)
      print("\nThe second matrix is : \n", matrix_2)
      print("\n*******************************************************")

      choice = int(input("Enter 1 for first matrix and 2 for second matrix : "))
      if choice == 1:
        val11 = np.linalg.svd(matrix_1)
        print("The Singular Value Decomposition of the Matrix 1 is : \n",val11)
      elif choice == 2:
        val11 = np.linalg.svd(matrix_2)
        print("The Singular Value Decomposition of the Matrix 2 is : \n",val11)
      else :
        print("Enter a valid choice!!!")
    except :
      print("Error!!!")

  elif num == 12 :
    os.system('cls')
    try :
      print("\nThe first matrix is : \n", matrix_1)
      print("\nThe second matrix is : \n", matrix_2)
      print("\n*******************************************************")

      choice = int(input("Enter 1 for first matrix and 2 for second matrix : "))
      if choice == 1:
        val12 = np.linalg.eigvals(matrix_1)
        print("The Eigen Value of the Matrix 1 is : \n",val12)
      elif choice == 2:
        val12 = np.linalg.eigvals(matrix_2)
        print("The Eigen Value of the Matrix 2 is : \n",val12)
      else :
        print("Enter a valid choice!!!")
    except :
      print("Error!!!")

  elif num == 13 :
    os.system('cls')
    try :
      print("\nThe first matrix is : \n", matrix_1)
      print("\nThe second matrix is : \n", matrix_2)
      print("\n*******************************************************")

      val = int(input("Enter the element to be searched : "))
      choice = int(input("Enter 1 for first matrix and 2 for second matrix : "))
      if choice == 1:
        val13 = np.where(matrix_1==val)
        print("The location of the Element in the Matrix 1 is : \n",val13)
      elif choice == 2:
        val13 = np.where(matrix_2==val)
        print("The location of the Element in the Matrix 2 is : \n",val13)
      else :
        print("Enter a valid choice!!!")
    except :
      print("Error!!!")    

  elif num == 14 :
    os.system('cls')
    try :
      print("\nThe first matrix is : \n", matrix_1)
      print("\nThe second matrix is : \n", matrix_2)
      print("\n*******************************************************")

      choice = int(input("Enter 1 for first matrix and 2 for second matrix : "))
      if choice == 1:
        print("The Upper Traingular Matrix Elements of the Matrix 1 (with the diagonal elements) : ")
        print(matrix_1[np.triu_indices(num_row1,k=0)]) # k=1 for excluding diagonal elements.
        print("\nThe Lower Traingular Matrix Elements of the Matrix 1 (with the diagonal elements) : ")
        print(matrix_1[np.tril_indices(num_row1,k=0)]) # k=-1 for excluding diagonal elements.
        val14 = (matrix_1[np.triu_indices(num_row1,k=0)].sum()-matrix_1[np.tril_indices(num_row1,k=0)].sum())
        print("The Difference of Sum of Upper and Lower Traingular Matrix of Matrix 1 is : ",val14)
      elif choice == 2:
        print("The Upper Traingular Matrix Elements of the Matrix 2 (with the diagonal elements) : ")
        print(matrix_2[np.triu_indices(num_row2,k=0)])
        print("\nThe Lower Traingular Matrix Elements of the Matrix 2 (with the diagonal elements) : ")
        print(matrix_2[np.tril_indices(num_row2,k=0)])
        val14 = (matrix_2[np.triu_indices(num_row2,k=0)].sum()-matrix_2[np.tril_indices(num_row2,k=0)].sum())
        print("The Difference of Sum of Upper and Lower Traingular Matrix of Matrix 2 is : ",val14)
      else :
        print("Enter a valid choice!!!")
    except :
      print("Error!!!")

  elif num == 15 :
    os.system('cls')
    print("Exiting program")
    break

  else :
    os.system('cls')
    print("Enter a valid choice!!!")
