while True:
  def game():
    print("******WELCOME TO ROCK PAPER SCISSOR GAME*******")
    import random
    ls=['rock','paper','scissor']
    x=random.choice(ls)
    #print("computer choose:",x)
    s=input("your choice:")
    if s=='rock' and x=='paper' or  s=='paper' and x=='scissor' or s=='scissor' and x=='rock':
        print("YOU ARE DEAD")
    else:
        print("YOU WON")
  response=input("do you want to play game(y/n):")
  if response =='y':
       game()
  else:
      break

 


