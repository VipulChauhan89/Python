#Program to check if the entered number is single digit or multidigit number
num=int(input("Enter the number : "))
if(num>=-9 and num<=9):
    print("{} is the single digit number\n".format(num))
else:
    print("{} is the multi digit number\n".format(num))
