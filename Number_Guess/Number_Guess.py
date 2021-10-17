import random
print("Welcome to the Game of Number ")
num=int(input("Guess a Number (1-20):"))
lucky_num=random.randrange(1,20)
print("Computer:\n    Number:",lucky_num)
if(num==lucky_num): 
    print("    You Win")
else:
    print("    Better Luck Next Time")