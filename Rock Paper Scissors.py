import os as o
import random as r

clrscr=lambda:o.system('cls')
#-------------------------------------------------------------------------
def game(ans,q,b):
    print(q)
    c=l[ans-1]
    if c==q:
        print("Match Draw")
        print("Your Money Returned:",b)
    elif ans==1:
        if q=="Scissors":
            print("You Win")
            print("Bet Money Doubled:",2*b)
        else:
            print("You Lose")
            print("Bet Money Lost:",b)
    elif ans==2:
        if q=="Rock":
            print("You Win")
            print("Money Doubled:",2*b)
        else:
            print("You Lose")
            print("Bet Money Lost:",b)
    elif ans==3:
        if q=="Paper":
            print("You Win")
            print("Money Doubled:",2*b)
        else:
            print("You Lose")
            print("Bet Money Lost:",b)
    else:
        print("Invalid Input")
#-------------------------------------------------------------------------
l=["Rock","Paper","Scissors"]
while True:
    clrscr()
    b=int(input("Enter Your Bet(Min. 100):"))
    print("1.Rock\n2.Paper\n3.Scissors")
    ans=int(input())
    q=r.choice(l)
    game(ans,q,b)
    print("Do You Want To Continue(Y/N):")
    c=input()
    if c=='Y' or c=='y':
        continue
    else:
        break
