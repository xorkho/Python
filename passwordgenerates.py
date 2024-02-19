from cryptography.fernet import Fernet
def write_key():
    key=Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)
def load_key():
    with open("key.key","rb") as key_file:
        key=key_file.read()
        return key

print('''1- ADD PASSWORD
2- VIEW PASSWORD
3- EXIT''')

key = load_key()
fer = Fernet(key)

def add():
    name=input("Enter Account Name: ").strip()
    password=input("Enter Your Password: ").strip()
    with open("password.txt","a") as f:
        f.write(name+"|"+fer.encrypt(password.encode()).decode()+"\n")
def view():
    with open("password.txt","r") as f:
        for line in f.readlines():
            data=line.rstrip()
            user,pwd=data.split("|")
            print("USER:",user,"|","Password:",pwd,fer.decrypt(pwd.encode()).decode()+"\n")

while True:
    mode=input('what you want to do?'  )
    if mode=="3":
        print("Thanks for using it")
        quit()
    if mode=="1":
        add()
    elif mode=="2":
        view()
    else:
        print("Invalid Choice")