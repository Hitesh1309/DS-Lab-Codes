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

temp = pd.merge(table,new_table,how='left')
temp.set_index(pd.Index(index_values),inplace=True)
print("\n\nThe Merged Table is : \n")
print(temp)

temp.to_csv("Merged_DB.csv")
