import random
print("HELLO WE ARE HERE TO ASSIST YOU TO GENERATE YOUR OTP")
w=int(input("PLEASE ENTER THE LENGTH OF THE OTP YOU WANT:"))
u=random.random()
o=str(u)[-w:]
print(o)
