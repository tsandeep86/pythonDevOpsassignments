import current_balance_bnk
def deposit(db):
    cursor=db.cursor()
    acctno=input("Enter the account number for cash withdrawl:\n")
    d_amt=input("Enter deposit amount:\n")
    cb=current_balance_bnk.current_balance(db,acctno)
    print "Depositing amount" 
    nbal=(cb + d_amt)
    q=("update banking.customer_details set balance={0} where account_no={1}").format(nbal,acctno)
    cursor.execute(q)
    db.commit()
    cbq=current_balance_bnk.current_balance(db,acctno)
    db.close()
    print "Current balance is: %d" % cbq

    