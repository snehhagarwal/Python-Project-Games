import random
def beginnerlevel():
     attempt=10
     x=random.randint(1,10)
     while attempt!=0:
           guess=int(input ("enter your guess:"))
           if guess==x:
               print("YOU WERE SUCCESSFULLY ABLE TO GUESS THE NUMBER")
               break
           elif guess>x:
               print("SORRY! YOU'RE GUESS IS GREATER THAN THE NUMBER")
           elif guess<x:
               print("SORRY YOU'RE GUESS IS SMALLER THAN THE NUMBER")
           attempt-=1
           print("NUMBER OF ATTEMPTS LEFT:",attempt)
     if attempt==9:
              print("YOU WERE ABLE TO GUESS THE NUMBER IN",attempt,"ATTEMPTS YOU HAVE GOT BRIALLIANT MIND!")
     elif 5<=attempt<=8:
              print("YOU WERE ABLE TO GUESS THE NUMBER IN",attempt,"ATTEMPTS GOOD GOING!!")
     elif 3<=attempt<=4:
              print("YOU WERE ABLE TO GUESS THE NUMBER IN",attempt,"ATTEMPTS TRY HARDER!")
     elif 1<=attempt<=2:
              print("YOU WERE ABLE TO GUESS THE NUMBER IN",attempt,"ATTEMPTS BETTER LUCK NEXT TIME")
def mediumlevel():
    attempt=15
    x=random.randint(1,100)
    while attempt!=0:
           guess=int(input ("enter your guess:"))
           if guess==x:
               print("YOU WERE SUCCESSFULLY ABLE TO GUESS THE NUMBER")
               break
           elif guess>x:
               print("SORRY! YOU'RE GUESS IS GREATER THAN THE NUMBER")
           elif guess<x:
               print("SORRY YOU'RE GUESS IS SMALLER THAN THE NUMBER")
           attempt-=1
           print("NUMBER OF ATTEMPTS LEFT:",attempt)
    if 13<=attempt<=15:
              print("YOU WERE ABLE TO GUESS THE NUMBER IN",attempt,"ATTEMPTS YOU HAVE GOT BRIALLIANT MIND!")
    elif 8<=attempt<=13:
              print("YOU WERE ABLE TO GUESS THE NUMBER IN",attempt,"ATTEMPTS GOOD GOING!!")
    elif 5<=attempt<=8:
              print("YOU WERE ABLE TO GUESS THE NUMBER IN",attempt,"ATTEMPTS TRY HARDER!")
    elif 1<=attempt<=5:
              print("YOU WERE ABLE TO GUESS THE NUMBER IN",attempt,"ATTEMPTS BETTER LUCK NEXT TIME")
def hardlevel():
    attempt=20
    x=random.randint(1,1000)
    while attempt!=0:
           guess=int(input ("enter your guess:"))
           if guess==x:
               print("YOU WERE SUCCESSFULLY ABLE TO GUESS THE NUMBER")
               break
           elif guess>x:
               print("SORRY! YOU'RE GUESS IS GREATER THAN THE NUMBER")
           elif guess<x:
               print("SORRY YOU'RE GUESS IS SMALLER THAN THE NUMBER")
           attempt-=1
           print("NUMBER OF ATTEMPTS LEFT:",attempt)
    if 15<=attempt<=20:
              print("YOU WERE ABLE TO GUESS THE NUMBER IN",attempt,"ATTEMPTS YOU HAVE GOT BRIALLIANT MIND!")
    elif 10<=attempt<=15:
              print("YOU WERE ABLE TO GUESS THE NUMBER IN",attempt,"ATTEMPTS GOOD GOING!!")
    elif 5<=attempt<=10:
              print("YOU WERE ABLE TO GUESS THE NUMBER IN",attempt,"ATTEMPTS TRY HARDER!")
    elif 1<=attempt<=5:
              print("YOU WERE ABLE TO GUESS THE NUMBER IN",attempt,"ATTEMPTS BETTER LUCK NEXT TIME")
print("********WELCOME TO GUESS THE NUMBER GAME*********")
l=int(input("ENTER THE LEVEL YOU WANT TO PLAY 1- IS FOR BEGINNER LEVEL 2-FOR MEDIUM LEVEL 3-FOR HARD LEVEL:"))
if l==1:
    beginnerlevel()
if l==2:
    mediumlevel()
if l==3:
    hardlevel()
