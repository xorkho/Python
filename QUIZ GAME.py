print("Welcome To The Game")
user_input=input("press Yes to continue: ").lower()
if user_input!="yes":
    print("Thanks for using")
    quit()
print("Ok lets go")
total=0

answer=input("What is stands for CPU? ").lower()
if answer=="central processing unit":
    print("correct answer")
    total+=1
else:
    print("Incorrect answer")
    
answer=input("What is stands for OS? ").lower()
if answer=="operating system":
    print("correct answer")
    total+=1
else:
    print("Incorrect answer")
    
answer=input("What is stands for HDD? ").lower()
if answer=="hard disk drive":
    print("correct answer")
    total+=1
else:
    print("Incorrect answer")
    
answer=input("What is stands for BIOS? ").lower()
if answer=="basic input output system":
    print("correct answer")
    total+=1
else:
    print("Incorrect answer")

answer=input("What is stands for LCD? ").lower()
if answer=="liquid crystal display":
    print("correct answer")
    total+=1
else:
    print("Incorrect answer")
    
print(f'You answered {total} question correct')