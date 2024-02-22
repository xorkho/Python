s1=input("Enter String 1: ")
s2=input("Enter String 2: ")
for i in s1:
    if i in s2:
        if i!="":
            print(f"Common:{i}")
        else:
            pass
    else:
        print(F"uncommon:{i}")
for j in s2:
    if j not in s1:
        print(f"uncommon{j}")