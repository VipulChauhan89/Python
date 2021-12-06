#Program to find the minimum out of three numbers
print("Enter three numbers to find the minimum out of three numbers : ")
n1=int(input())
n2=int(input())
n3=int(input())
min=n1
if(n2<min):
    min=n2
if(n3<min):
    min=n3;
print("The minimum number is = {}".format(min))
