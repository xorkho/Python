#  QUESTION NO 8 Write code to add up and print all the positive values in a list of integers. For example, a list containing the elements
# [3,-3,5,2,-1,2] would evaluate to 12, since 3+5+2+2 = 12. The code prints zero if the list is empty.
# l=[3,-3,4,2,1]
# r=[x for x in l if x>0]
# total=sum((r))
# print(total)
# QUESTION 9:
# Write code that counts and prints the even numbers in a list of integers. For example, a list containing the elements
# 3;5;4;-1; and 0, would evaluate to 2, since there are only two even numbers: 4 and 0. The code prints zero if the list is empty
count=0
l=[2,4,5,7,8,0]
for x in l:
    if x%2==0:
        print(x)
        count+=1
    else:
        print()
print(f"Total Even NO:{count}")