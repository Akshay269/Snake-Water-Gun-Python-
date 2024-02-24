import random


def check(comp,user):
    if comp==user:
        return 0
    elif comp==0 and user==1:
        return -1
    elif comp==1 and user==2:
        return -1
    elif comp==2 and user==0:
        return -1
    elif comp==2 and user== 0:
        return -1
    return 1
    
comp=random.randint(0,2)
user=int(input("0 for Snake, 1 for Water, -1 for Gun: "))

score=check(comp,user)
print("Your choice: ",user)
print("Computer's choice: ",comp)

if score==0:
    print("Draw")
elif score==1:
    print("You Win")
else:
    print("You Lose")


