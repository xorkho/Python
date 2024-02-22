# MATH QUIZ GAME:


import random
import time

OPERATORS=["+","-","*"]
MIN_OPERANDS=3
MAX_OPERANDS=15
TOTAL_PROBLEM=10
wrong=0
def generate_problems():
    right=random.randint(MIN_OPERANDS,MAX_OPERANDS)
    left=random.randint(MIN_OPERANDS,MAX_OPERANDS)
    selected_operators=random.choice(OPERATORS)
    expression=str(left)+" "+selected_operators+" "+str(right)
    result=eval(expression)
    return expression,result
while True:
    user_input=input("Press y to start: ").lower()
    if user_input=='y':
        print("------START THE QUIZ------")
        break
    else:
        print("Invalid choice try again")

initital_time=time.time()

for i in range(TOTAL_PROBLEM):
    expression,result=generate_problems()
    while True:
        Answer=input("Problem NO#"+str(i+1)+ ":" + expression + "=")
        if Answer==str(result):
            print("Your Answer is correct")
            break
        wrong+=1
final_time=time.time()
Calculated_time=final_time-initital_time
Total_time=round(Calculated_time,2)

print("-----Quiz Ended-----")
print("Your Answered in",Total_time,"seconds!" )
