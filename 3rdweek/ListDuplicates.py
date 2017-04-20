"""04/11/2017
List duplication
Take 2 list,
a= [1,2,2,3,4,13,18,26,38,66]
b= [1,1,2,5,13,16,26,33,43,49,59,66]
Write a program to print a new list which contains only common elements from both list. List a, and list b can be of different sizes.
"""

a= [1,2,2,3,4,13,18,26,38,66]
b= [1,1,2,5,13,16,26,33,43,49,59,66]

c=[]

for i in range(len(a)):
     if a[i] in b:
            c.append(a[i])
            
print c
             
             
            
