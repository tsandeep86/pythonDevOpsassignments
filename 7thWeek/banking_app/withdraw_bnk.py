import current_balance_bnk
def withdraw(db):
    cursor=db.cursor()
    acctno=input("Enter the account number for cash withdrawl:\n")
    w_amt=input("Enter withdrwal amount:\n")
    bal=current_balance_bnk.current_balance(db,acctno)
    if (bal - w_amt) < 0 :
        print "balance too low, cannot withdraw"
    else:
        print "withdrawing amount" 
        nbal=(bal - w_amt)
        q=("update banking.customer_details set balance={0} where account_no={1}").format(nbal,acctno)
        cursor.execute(q)
        db.commit()
        cbq=current_balance_bnk.current_balance(db,acctno)
        db.close()
        print "Current balance is: %d" % cbq
