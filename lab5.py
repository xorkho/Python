n=input("Enter your ID: ")
a="*"*12
while True:
    print(f"Main Menu\n{a}\n1.Deposite Money\n2.Withdraw amount\n3.Login as different user")
    choice=int(input("Enter Your Choice: "))
    if choice==1 or choice==2 or choice==3:
        print("Your Transaction has been completed")
        c=input("Do you want to continue [y/y] (Press any key to terminate):")
        if c=="Y" or c=="y":
            pass
        else:
            break
    else:
        break   