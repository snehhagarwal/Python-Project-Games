'''
 try to solve with pseudocode:
 a) Player vs. computer.
 b) An interface with options.
 c) Checking the player against the computer.
 d) Returning the winner status.
 e) Ask if the player wants to play again.'''
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

 


