# GUESS THE NUMBER GAME

import random
random_number=random.randint(1,100)
while True:
    user_input=input('Enter Number or Quit(Q): ')
    if user_input.upper() == 'Q':
              break
          
          
    user_input=int(user_input)
    if user_input==random_number:
        print(f"{user_input} is the correct guess")
        break
    elif user_input>random_number:
        print(f"{user_input}is much greater")
    elif user_input<random_number:
        print(f"{user_input}is too smaller")
print("-----GAME OVER------")