"""
Print a list of numbers that are divisors of number num. Take input from user for num.
For example:
>>> Enter the number: 20
Divisore List = [1, 2, 4, 5, 10, 20]
"""

n1=input("Please enter the number :")

DL=[]

for i in  range (1,n1+1):
    if ( n1 % i == 0):
        DL.extend([i])
       
print DL[:]
        
        