"""
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), 
compare them, print out a message of congratulations to the winner, 
and ask if the players want to start a new game)
"""

game="Y"
while  (game == "Y" ):
    p1=raw_input("Player 1 Please Enter your choice:")
    p2=raw_input("Player 2 Please Enter your choice:")
    
    if p1 in ["rock","paper","scissors"] and p2 in ["rock","paper","scissors"]:
        p1 = p1
        p2 = p2
    else:
       print "wrong choice for player, Please choose rock or paper or scissors: "
       continue
    
    if p1 == p2:
        print "Draw"
    elif p1 == "rock" and p2 == "scissors":
        print " P1 wins"
    elif p1 == "scissors" and p2 == "paper":
        print "p1 wins"
    elif p1 == "paper" and p2 =="rock":
        print "p1 wins"
    else:
        print " p2 wins"
   
    game=raw_input("Do you wanna play another round , Enter Y or N:")
    if game==("Y"):
        continue
    else:
        print ('Thanks for playing')
        break

