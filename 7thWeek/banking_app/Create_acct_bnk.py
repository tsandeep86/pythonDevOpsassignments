"""This module is specific for creating an banking account"""

def create_account():
    f_name=raw_input("Enter First Name of the account:\n").strip()
    while(not f_name.isalpha()):
        print" first name cannot be null or have numbers"
        f_name=raw_input("Enter First Name of the account:\n").strip()
    l_name=raw_input("Enter Last Name of the account:\n")
    while(not l_name.isalpha()):
        print" last name cannot be null or have numbers"
        l_name=raw_input("Enter Last Name of the account:\n").strip()
    acct_no=input("Enter account No:\n")
    balance=input("Enter balance:\n")
    address=raw_input("Enter address:\n")
    phone_no=input("Enter Phone no:\n")
    query="insert into banking.customer_details(first_name,last_name,account_no,balance,address,phone_no) values ('{0}','{1}',{2},{3},'{4}',{5})".format(f_name,l_name,acct_no,balance,address,phone_no)
    return query

    
