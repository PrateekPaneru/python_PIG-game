import random

def roll():
    min_val=1
    max_val=6
    roll=random.randint(min_val,max_val)

    return roll

while True:
    players= input("enter the number of players (1-4): ")
    if players.isdigit():
        players=int(players)
        if 2<=players <=4:
            break
        else:
            print("must be between 2-4 players")
    else:
        print("Invalid , Try Again (it has to be a Number)")

max_score=50
player_score=[0 for _ in range(players)]

while max(player_score) < max_score:
    for player_idx in range(players):
        print("\nplayer Number" , player_idx+1 , "turn has Started!\n")
        print("Your total score is : " , player_score[player_idx], "\n")
        current_score = 0

        while True:
            should_roll = input("would You like to roll (y/n): ")
            if should_roll.lower() != "y":
                break
                
            value=roll()
            if value == 1:
                print("You rolled a 1! Turn done")    
                current_score=0
                break
            else:
                current_score += value
                print("Your rolled : " , value)
            
            print("your Score is : " , current_score)

        player_score[player_idx] += current_score   
        print("Your Total Score is:- " , player_score[player_idx]) 

max_score=max(player_score)
player_win=player_score.index(max_score)
print("player Number" , player_win+1 , "is the winner with a score of: " , max_score)