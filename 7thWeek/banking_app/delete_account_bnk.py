import current_balance_bnk
import display_accounts_bnk
def delete_account(db):
    cursor=db.cursor()
    acctno=input("Eneter account number to be deleted:\n")
    bal=current_balance_bnk.current_balance(db,acctno)
    if (bal) > 0 :
        print "account has balance and cannot be deleted. Please withdraw amount and retry"
    else:
        q=("delete from banking.customer_details where account_no={0}").format(acctno)
        cursor.execute(q)
        db.commit()
        print "Deleting account number %d" % acctno
        
        print "Listing reamining accounts"
        display_accounts_bnk.display_accounts(db)