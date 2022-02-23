'''
    Program to print the sum of series
    1 - 2/2! + 3/3! - 4/4! + ......Nth term
'''

def factorial(n):
    if(n==1):
        return n
    else:
        return n*factorial(n-1)

sign=-1
sum=1
N=int(input("Enter the Limit upto which you want o find out the sum of the series : "))
for i in range(2,N+1):
    sum=sum+((i/float(factorial(i)))*sign)
    sign=sign*(-1)

print("Sum of the series is = {}\n".format(sum))
