"""A single integer, n , denoting the size of the staircase.
Print a staircase of size n using # symbols and spaces.
Input: 6 
Output:
     #
    ##
   ###
  ####
 #####
######
"""
"""
i=0
h=[' ',' ',' ',' ',' ','#']

while i < 6:
    
    print "".join(h)
    h.pop(0) 
    h.append('#')  
    i += 1
"""




l=input("Please enter the height of staircase:")
k = 1
for i in range(l):
    print " " * (l-1) + "#" *k 
    #+ "#" *(k-1)
    k +=1
    l -=1 



 
    
    