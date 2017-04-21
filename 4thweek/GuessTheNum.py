"""
Guessing Game: Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
 (_Hint: remember to use the user input lessons from the very first exercise
Extras:
Keep the game going until the user types exit
Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""
from random import randint
def rand():
    rand_num=((randint(1,9)))
    print rand_num
    return rand_num

def userinput():
    ui_num=input("Please Guess the number:")
    return ui_num

def numcomp(rand_num,ui_num):
    
    if ui_num < rand_num:
        print " Too Low "
        Flag='Y'
        return Flag
    elif ui_num > rand_num:
        print " Too High "
        Flag='Y'
        return Flag
    elif ui_num == rand_num:
        print " Hurray Right guess!!"
        Flag='N'
        return Flag

def main():
    Flag='Y'
    games = 1
    guesses = 0 
    rand_num=rand()
    agg=[]
    while (True):
        guesses +=1
        Flag=numcomp(rand_num,ui_num=userinput())
        if Flag=='Y':
            continue 
        elif Flag=='N':
            gamebreak=raw_input("Do you want to - play or exit:")
            if gamebreak == 'play':
                rand_num=rand()
                agg.append((games,guesses))
                games += 1
                guesses=0
                continue
            elif gamebreak=='exit':
                agg.append((games,guesses))
                print "Thanks for playing!"
                break
    print "Total Games played=", len(agg)
    for i in range(len(agg)):
        print "For Game %d Guesses made are %d" % (agg[i][0],agg[i][1])
main()         
        
        
        


     