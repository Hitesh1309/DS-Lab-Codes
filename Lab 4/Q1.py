'''
Lab 4 - Code 1 - Library Management System.
Kattamuri V S J V S Hitesh Gupta
CS20B1127

Write a python program to handle books in a library management system. The information available in a book are book ISSN, book title, price, edition, year, and author name. The library management system should support the following menus,
1) Write
2) Read
3) Search
4) Exit

'''

import pickle

def Writebooks():

    fhand = open("Libary_Manage.dat", "ab")  # opening file in write mode (append)

    n = int(input("\nEnter the number of books to be entered: "))
    
    for i in range(n):

        print(f"\nBook {i+1} -")
        issn = int(input("ISSN: "))
        title = input("Title: ")
        price = int(input("Price: "))
        edition = input("Edition: ")
        year = int(input("Year: "))
        author = input("Author name: ")

        lis = [issn, title, price, edition, year, author]

        pickle.dump(lis, fhand)

    print("\nWriting done.....")
    fhand.close()

def Readbooks():

    fhand = open("Libary_Manage.dat", "rb")  # opening file in read mode

    print("\nReading every entry:")
    i = 1

    while(1):

        try:  # error handling
            x = pickle.load(fhand)
            print(f"\nBook {i} -")
            
            # x in format of [issn, title, price, edition, year, author]

            print("ISSN:", x[0])
            print("Title:", x[1])
            print("Price:", x[2])
            print("Edition:", x[3])
            print("Year:", x[4])
            print("Author:", x[5])

            i += 1

        except  EOFError:  # EOFError is a keyword for finding end of file error
            print('Reading done')
            break    

    fhand.close()


def Searchbooks():

    arg = input("\nEnter the book title you want to search for: ")
    flag = 0

    fhand = open("Libary_Manage.dat", "rb")  # opening file in read mode

    while(1):

      try:  # error handling
          x = pickle.load(fhand)
          
          # x in format of [issn, title, price, edition, year, author]
         
          if(arg == x[1]):

            print("\nBook found....")
            print("ISSN:", x[0])
            print("Title:", x[1])
            print("Price:", x[2])
            print("Edition:", x[3])
            print("Year:", x[4])
            print("Author:", x[5], end = "\n\n")
            flag = 1

      except  EOFError:  # EOFError is a keyword
        if(flag == 0):
            print("\nBook not found\n")
        
        break

    fhand.close()

# Menu program below

while(1):

    print("\n------Menu----------")
    print("1) Write\n2) Read\n3) Search\n4) Exit")

    choice = int(input("Enter your choice: "))

    if(choice == 1):
        Writebooks()

    elif(choice == 2):
        Readbooks()

    elif(choice == 3):
        Searchbooks()

    elif(choice == 4):
        print("Exiting program")
        break

    else : 
        print("\nEnter correct option...")
    
