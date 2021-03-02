import pickle as p
import os as o
import random as r
import time

clrscr=lambda:o.system('cls')
#--------------------------------------------------------------------
def countdown():
    t=5
    while t:
        mins,secs=divmod(t,60)
        timer='{:02d}:{:02d}'.format(mins,secs)
        print("GAME STARTS IN:",timer,end="\r")
        time.sleep(1)
        t-=1
    print("GAME STARTS")
#--------------------------------------------------------------------
def cat(ctg):
    if ctg==1:
        l=["GOLD","BLACK","BEIGE","BLUE","BURGUNDY","LAVENDER","WHITE","GREEN"]
    elif ctg==2:
        l=["ARCHERY","SURFING","SOCCER","CRICKET","GOLF","POLO","SWIMMING","SNOWBOARDING"]
    elif ctg==3:
        l=["KIWI","GUAVA","MANGO","WATERMELON","POMEGRANATE","PINEAPPLE","ORANGE","JACKFRUIT"]
    elif ctg==4:
        l=["SEYCHELLES","AZERBAIJAN","LUXEMBOURG","ETHOPIA","MADAGASCAR","MAURITIUS","JAPAN","CAMBODIA"]
    else:
        l=["NARUTO","HAIKYUU","BLEACH","GINTAMA","POKEMON","INUYASHA","YOURNAME","ERASED"]
    w=r.choice(l)
    w=list(w)
    return(w)
#--------------------------------------------------------------------
def display(w):
    global lw
    print(*lw,sep="")
    return(lw)
#--------------------------------------------------------------------
def struct(count):
    clrscr()
    if count==0:
        print(" ___","|/   ","|   ","|   ","|   ","|   ",sep="\n")
    elif count==1:
        print(" ___","|/  |","|   ","|   ","|   ","|   ",sep="\n")
    elif count==2:
        print(" ___","|/  |","|   0","|   ","|   ","|   ",sep="\n")
    elif count==3:
        print(" ___","|/  |","|   0","|  /|\\","|   ","|   ",sep="\n")
    elif count==4:
        print(" ___","|/  |","|   0","|  /|\\","|   |","|   ",sep="\n")
    elif count==5:
        print(" ___","|/  |","|   0","|  /|\\","|   |","|  / \\",sep="\n")
#--------------------------------------------------------------------
def game(w):
    clrscr()
    count=0
    global lw
    #print(w)
    while True:
        if count==5:
            print("Lost All Lives")
            print("########################### GAME OVER ###########################")
            print("The Word Was:",*w,sep="")
            break
        print("\t\t\tTotal Lives Left:",5-count)
        lw=display(w)
        ans=input("Enter Your Answer:")
        if ans in w:
            for i in range(0,len(w)):
                if w[i]==ans:
                    lw[i]=ans
        else:
            count+=1
            print("Lost ",count,"th Life",sep="")
        struct(count)
        if w==lw:
            time.sleep(1)
            print("########################### YOU WON ###########################")
            break
#--------------------------------------------------------------------
print("-----------------------------------HANGMAN-----------------------------------")
countdown()
time.sleep(1)
print("Choose A Category From Below")
time.sleep(1)
ctg=int(input("1.Colours\n2.Sports\n3.Fruits\n4.Countries\n5.Anime"))
w=cat(ctg)
lw=["-"]*len(w)
game(w)
