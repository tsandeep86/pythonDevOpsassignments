def display_accounts(db):
    cursor=db.cursor()
    q=("select account_no,first_name,last_name from banking.customer_details")
    cursor.execute("select account_no,first_name,last_name from banking.customer_details")
    data=cursor.fetchall()
    for i in data:
        print i[0],i[1],i[2]
        