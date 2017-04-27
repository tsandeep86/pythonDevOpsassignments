"""
 Given an unsorted integer array, find the first missing positive integer.
For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.
"""

def input_numbers():
    l=list(input('Please enter list of coma seperated numbers:'))
    l.sort()
    return l

#l=[1,0,2,3,4,-1,-2]
#l.sort()

def del_neg(*l):
    
    nl=[]
    for i in range(len(l[0])):
        if l[0][i] > -1:
            nl.append(l[0][i])
    
    nl.append(nl[-1]+1)
    nl.insert(0,0)
    return nl

def find_missing(*nl):
    for i in range(len(nl[0])-1):
        if nl[0][i]+1 == nl[0][i+1]:
            result=nl[0][i]+1
        else:
            result=nl[0][i]+1
            break
            
    print "First missing positive number is:", result

def main():
    l=input_numbers()
    nl=del_neg(l)
    find_missing(nl)
main()