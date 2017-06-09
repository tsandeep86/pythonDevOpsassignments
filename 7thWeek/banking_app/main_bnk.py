import pymysql
import Create_acct_bnk
import current_balance_bnk
import withdraw_bnk 
import deposit_bnk
import display_accounts_bnk
import delete_account_bnk


import pymysql
db=pymysql.Connect(host='localhost', port=3306, user='root', passwd='AnjuSandy2628', db='banking')
cursor=db.cursor()


def bank_application():
    options = input('Enter your option \n1) Create Account\n2) check balance \n3) Withdrawl \n4) Deposit \n5) Display all accounts \n6) Delete account \n')
    if options == 1:
        q=Create_acct_bnk.create_account()
        cursor.execute(q)
        db.commit()
        db.close()
    elif options == 2:
        acctno=input("enter account number for balanace enquiry:\n")
        cbq=current_balance_bnk.current_balance(db,acctno) 
        print ("Balance for account number %d is %d") % (acctno,cbq)
    elif options == 3:
        withdraw_bnk.withdraw(db)
    elif options == 4:
        deposit_bnk.deposit(db)
    elif options == 5:
        display_accounts_bnk.display_accounts(db)
    elif options == 6:
        delete_account_bnk.delete_account(db)

bank_application()


    