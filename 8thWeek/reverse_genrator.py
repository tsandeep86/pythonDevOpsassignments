



def rev():
    str='Sandeep'
    L=len(str)
    for i in range(len(str)):
        yield str[L-1]
        L -=1
        


for i in rev():
    print i