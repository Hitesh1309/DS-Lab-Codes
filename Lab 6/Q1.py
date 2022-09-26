'''
Lab 6 - Code 1 - Pandas.
Kattamuri V S J V S Hitesh Gupta
CS20B1127

'''

import pandas as pd 

# Creating the table 1.
temp = [['Ram',9893893891,'SB',989389389173,8989839],['Sam',9893893898,'CA',989389389179,7690990],['Prabhu',9893893871,'SB',989389389159,989330],['Desai',9893893895,'SB',989389389153,83794],['Tim',9893893875,'CA',989389389191,4045371]]

index_values = [1,2,3,4,5]
column_names = ['Name','Account Number','Account Type','Aadhar Number','Balance']
table = pd.DataFrame(temp,columns=column_names )

table.set_index(pd.Index(index_values),inplace=True)
print("\n\nThe First Table is : \n")
print(table)
table.to_csv('SBIAccountHolder.csv')

df = pd.read_csv('SBIAccountHolder.csv')
# print(df.to_string())


# Creating the table 2.
temp = [['Ram',989389389173,'9840787333','12-02-1990','No 23, Kandigai, Chennai 127'],['Sam',989389389179,'9840787343','12-02-2000','No 73, Melakottaaiyu, Chennai 127'],['Prabhu',989389389159,'9840787353','12-02-2010','No 43, Anna Nagar, Chennai 102'],['Tim',989389389191,'7333124193','13-09-2001','No 53, Navalur, Chennai 127'],['Desai',989389389153,'6205839623','12-02-2015','No 93, Mambalam, Chennai 105']]

index_values = [1,2,3,4,5]

column_names = ['Name','Aadhar Number','Contact_No','DOB','Address']

new_table = pd.DataFrame(temp,columns=column_names )

new_table.set_index(pd.Index(index_values),inplace=True)
print("\n\nThe Second Table is : \n")
print(new_table)

new_table.to_csv('Aadhar_DB.csv')

df = pd.read_csv('Aadhar_DB.csv')
#print(df.to_string())


# Append in the csv file. 
def append_record() :
  global table,df

  name_list = [(input("\nEnter the Name : "))]
  try :
    accno_list = [(int(input("Enter the Account Number : ")))]
  except :
    print("Enter an Integer Value!!!")
    accno_list = [(int(input("Enter the Account Number : ")))]
  acctype_list = [(input("Enter the Account Type : "))]
  if ( acctype_list[0] != 'SB' and  acctype_list[0] != 'CA' ) :
    print("Enter a Valid Account Type!!!")
    acctype_list = [(input("Enter the Account Type : "))]
  aadharno_list = [(int(input("Enter the Aadhar Number : ")))]
  for index_val in table.index:
    if table.loc[index_val,'Aadhar Number'] == aadharno_list:
      print("Enter a Distinct Aadhar Number!!!")
      aadharno_list = [(int(input("Enter the Aadhar Number : ")))]
  try :
    balance_list = [(int(input("Enter the Balance : ")))]
  except :
    print("Enter an Integer Value!!!")
    balance_list = [(int(input("Enter the Balance : ")))]

  a = {'Name':name_list, 'Account Number':accno_list,
      'Account Type': acctype_list, 'Aadhar Number': aadharno_list,
      'Balance': balance_list
      }
  # print(a)

  temp_table = pd.DataFrame(a)
  # print(temp_table)

  table = table.append(temp_table,ignore_index=True)
  index_values.append(index_values[-1]+1)

  table.set_index(pd.Index(index_values),inplace=True)
  print("\n\nThe Table after Appending a row is : \n")
  print(table)
  table.to_csv('SBIAccountHolder.csv')

  df = pd.read_csv('SBIAccountHolder.csv')
  # print(df.to_string())


# Delete a record given the account number.
def delete_record() :
  global table,df,index_values
  count = 0
  flag = 0

  try :
    value = int(input("\nEnter the Account Number : "))

    for index_val in table.index:
      if table.loc[index_val,'Account Number'] == value :
        table = table.drop(index=index_val)
        index_values.pop()
        table.set_index(pd.Index(index_values),inplace=True)
        print("\n\nThe Updated Table after Deleting the record is : \n")
        print(table)
        flag = 1
      else :
        count = count + 1

    if count == len(index_values) and flag == 0 :
      print("\nAccount Number Not Present in the Database!!!") 
      count = 0
      
    table.to_csv('SBIAccountHolder.csv')

    df = pd.read_csv('SBIAccountHolder.csv')
    #print(df.to_string())

  except :
    print("Enter an Integer Value!!!")


# Credit given account number and amount to be credited.
def credit() :
  global table,df,index_values
  count = 0

  value = int(input("Enter the Account Number : "))
  try :
    amount_cred = int(input("Enter the Amount to be Credited : "))

    for index_val in table.index:
      if table.loc[index_val,'Account Number'] == value:
        table.loc[index_val,'Balance'] += amount_cred

        table.set_index(pd.Index(index_values),inplace=True)
        print("\n\nThe Updated Table after Crediting the Amount : \n")
        print(table)
      
      else : 
        count = count + 1
    
    if count == len(index_values) :
      print("\nAccount Number Not Present in the Database!!!")  
    
    table.to_csv('SBIAccountHolder.csv')

    df = pd.read_csv('SBIAccountHolder.csv')
    #print(df.to_string())

  except :
    print("Enter an Integer Value!!!")

  
# Debit :
def debit() :
  global table,df,index_values
  count = 0

  try :
    value = int(input("Enter the Account Number : "))
    amount_cred = int(input("Enter the Amount to be Debited : "))

    for index_val in table.index :
      if table.loc[index_val,'Account Number'] == value :
        if table.loc[index_val,'Account Type'] == 'SB' :
            table.loc[index_val,'Balance'] -= amount_cred
            table.set_index(pd.Index(index_values),inplace=True)
            print("\n\nThe Updated Table after Debiting the Amount : \n")
            print(table)
            if table.loc[index_val,'Balance'] < 0 :
                table.loc[index_val,'Balance'] += amount_cred
                print("Balance Insufficient!!!")
        elif table.loc[index_val,'Account Type'] == 'CA' :
            table.loc[index_val,'Balance'] -= amount_cred
            table.set_index(pd.Index(index_values),inplace=True)
            print("\nThe Updated Table after Debiting the Amount : ")
            print(table)
      else :
        count = count + 1

    if count == len(index_values) :
      print("\nAccount Number Not Present in the Database!!!") 

    table.to_csv('SBIAccountHolder.csv')

    df = pd.read_csv('SBIAccountHolder.csv')
    #print(df.to_string())

  except :
    print("Enter an Integer Value!!!")


# Print :
def print_account() :
  global table,df,index_values
  count = 0

  try :
    value = int(input("Enter the Account Number : "))

    for index_val in table.index :
      if table.loc[index_val,'Account Number'] == value :
        print("\n\nThe Account Details of the Requested Account Number is : \n")
        print(table.loc[[index_val]])
        # print(table)

      else :
        count = count + 1
    
    if count == len(index_values) :
      print("\nAccount Number Not Present in the Database!!!")  

    table.to_csv('SBIAccountHolder.csv')

    df = pd.read_csv('SBIAccountHolder.csv')
    #print(df.to_string())

  except :
    print("Enter an Integer Value!!!")

  
# Concat - 
def merging() :
  global table,df,new_table,index_values
  
  # temp = table.merge(new_table)
  temp = pd.merge(table,new_table,how='left')
  temp.set_index(pd.Index(index_values),inplace=True)
  print("\n\nThe Merged Table is : \n")
  print(temp)

  temp.to_csv("Merged_DB.csv")


while(1) :
  print("\n------Menu----------")
  print("1) Append Row\n2) Delete Row\n3) Credit\n4) Debit\n5) Print\n6) Merge the two Tables\n7) Exit")

  choice = int(input("Enter your choice: "))

  if choice == 1 :
    append_record()

  elif choice == 2 :
    delete_record()

  elif choice == 3  :
    credit()

  elif choice == 4 :
    debit()

  elif choice == 5 :
    print_account()

  elif choice == 6 :
    merging()

  elif choice == 7 :
    print("Exiting program")
    break

  else :
    print("\nEnter correct option...")
