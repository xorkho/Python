# PIG GAME ROLL DICE IF I GOT 1 IN DICE MY CURRENT SCORE WILL BECOME 0 AND THEN START WHO EVER REACHES TO MAXIMUM SCORE HE/SHE WILL WIN THE GAME
import random
def roll():
    min_roll=1
    max_roll=6
    roll=random.randint(min_roll,max_roll)
    return roll
while True:
    no_of_players=input("How Many players do you want to play with(2-4)? ")
    if no_of_players.isdigit():
        no_of_players=int(no_of_players)
        if 2<=no_of_players<=4:
            print("Lets Play The Game")
            break
        else:
            print("Invalid choice try again")
    else:
        print("Plz select a number in range(2-4)")
max_score=50
player_score=[0 for i in range(no_of_players)]


while max_score > max(player_score):
    for player_idx in range(no_of_players):
        print("\nplayer number",player_idx+1,"your turn just has started")
        print("Your total score is",player_score[player_idx],"\n")
        current_score=0
        while True:
            # for i in range(no_of_players):
                user_input=input("Enter Y for Your Turn: ").lower()
                if user_input!="y":
                    break
                user_value=roll()
                if user_value==1:
                    print("Its Done You Dice 1")
                    current_score=0
                    break
                else:
                    current_score+=user_value
                    print("You Rolled a",user_value)
                print("Your score is",current_score)
        player_score[player_idx]+=current_score
        print("Your total score is",player_score[player_idx])
        
maximum_score=max(player_score)
winning_idx=player_score.index(maximum_score)
print('The winner is player',winning_idx+1,'and his score is',maximum_score )