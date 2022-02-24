#Program to find out the sum of N natural numbers using recursion
def sum(n):
    if(n==1):
        return 1
    else:
        return n+sum(n-1)

N=int(input("Enter the limit upto which we have to find out sum : "))
print("Sum is = {}\n".format(sum(N)))
