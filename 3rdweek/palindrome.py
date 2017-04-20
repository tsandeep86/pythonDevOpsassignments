"""
Take a string input from the user and check if its Palindrome or not.
"""
"""from binascii import rlecode_hqx

s=raw_input("Please enter a string:")

if s == ' '.join(reversed(s.split(" "))):
    print "String is palindrome"
else:
    print "oops"
    """
#################
"""Implementation by not using string methods"""
#################

s=raw_input("Enter string:")
l=[]
rl=[]
for i in s:
     l.append(i)

for j in  range(len(l)):
    
    rl.append(l.pop())

#print rl    

if s == "".join(rl)  :
#if cl == "".join(rl):
    print "palindrome"
else:
    print "oops"

