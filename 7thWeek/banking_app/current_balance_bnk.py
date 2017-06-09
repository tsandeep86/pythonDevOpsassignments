def current_balance(db,acct_no):
    cursor=db.cursor()
    q=("select balance from banking.customer_details where account_no={0}").format(acct_no)
    cursor.execute(q)
    bal=cursor.fetchone()
    return bal[0]