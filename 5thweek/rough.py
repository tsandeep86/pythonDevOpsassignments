if __name__ == '__main__':
    n = input("Input number:")
    if 1 < n < 100:
        if n % 2 != 0:
            print "Weird"
        elif n % 2 ==0 and 2 <= n <=5:
            print "Not Weird"
        elif n % 2 == 0 and 6 <= n <=20:
            print "Weird"
        elif n > 20 and n % 2 == 0:
            print "Not Weird"
    else: 
        exit
        
