#04-01-2017
#Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

import datetime
n=raw_input("Enter Name of the person:")
a=input("Enter age of the person:")
fy=datetime.datetime.today().year+(100-a)
print  n , "will turn 100 in the year" , fy
