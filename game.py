# ROCK PAPER SCISSOR GAME:

import random
def decision(user_input,comp_input):
    if user_input==comp_input:
        return 0
    if user_input==1 and comp_input==3:
        return 1
    if user_input==2 and comp_input==1:
        return 1
    if user_input==3 and comp_input==2:
        return 1
    else:
        return -1
     
user_input=int(input('''Enter your choice:
                1- For Rock
                2- For Paper
                3- For Scissor\n'''))
comp_input=random.randint(1,3)
 
print("user: ", user_input)
print("computer", comp_input)

score=decision(user_input,comp_input)

if score==0:
    print("The Game is draw")
elif score==1:
    print("You Won")
elif score==-1:
    print("You Loose")     