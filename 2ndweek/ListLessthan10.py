"""
Take a list, for example
a=[1,2,2,3,4,55,65,76,78]
Write a program to return list with numbers less than 10.
Step 2:
Take the number x from user and print a new list with elements less than number x.
"""

a=[1,2,2,3,4,55,65,76,78]
for i in range(len(a)):
    if ( a[i] < 10 ):
        print "number " , a[i] , " is less than 10"
        
        

v1=input( "Please enter a number:")

x=[]

for i in range(len(a)):
    if ( a[i] < v1 ):
        print a[i]
        x.extend([a[i]])
        
print x[:]      
        