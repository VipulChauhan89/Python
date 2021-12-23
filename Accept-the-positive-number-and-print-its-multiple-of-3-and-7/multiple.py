#Program to accept the positive number and print its multiple of 3 and 7.
print("Enter the number : ",end="")
num=int(input())
if(num<0):
    print("You entered the negative number .")
else:
    print("Multiple of three of number {0} is = {1}".format(num,num*3))
    print("Multiple of seven of number {0} is = {1}".format(num,num*7))
