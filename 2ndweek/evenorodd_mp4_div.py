"""04/07/2017
Level 1:
Write a program asking user to enter a number, depending on whether the number is even or odd, print out an appropriate message to the user.

Level 2:
If the number is a multiple of 4, print out a different message.

Level 3:
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""


n1=input("Please enter a number:")

#print float(n1) % 2
if ( float(n1) % 2.0 == 0):
  print " Entered number is even"
else:
  print " Entered number is odd"
  

if ( n1 % 4 == 0 ):
    print "Entered number is multiplier of 4"
else:
    print "Entered number is not a multiplier of 4"
    
n2=input("Please enter a number:")
n3=input("Please enter a number:")

if ( float(n2) % float(n3) == 0):
    print "hurray"
else:
    print "oops"


