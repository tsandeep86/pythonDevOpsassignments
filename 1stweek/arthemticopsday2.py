"""Perform arithmetic operators with following output:
Expected Input:
Enter the 1st number = 43
Enter the 2nd number = 34

Expected Output:
Results
Addition: 77
Subtraction: 9
Multiplication: 1462
Division: 1.2647058823529411"""

num1 = input('enter value for 1st number =' )
num2 = input('enter value for 2nd number =')
print "Results"
print ("Addition: %s") % (num1 + num2)
print ("Subtraction: %s") % (num1 - num2)
print ("Multiplication %s") % ( num1 * num2)
print "Division: " , float(num1) /  float(num2)


