#Program to find the factorial of the number
factorial=1
print("Enter the number to find its factorial : ",end="")
num=int(input())
for i in range(2,num+1):
    factorial*=i
print("Factorial of number {0} is = {1}\n".format(num,factorial))
