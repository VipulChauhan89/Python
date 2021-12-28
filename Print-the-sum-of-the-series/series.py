#program to print the pattern 1/1^2 +1/3^2 -1/5^2 +1/7^2 ......N
sign=1
sum=1
print("Enter the last limit : ",end="")
N=int(input())
for i in range(3,N+1,+2):
    sum=sum+(sign*(1/(i*i)));
    sign*=-1;
print("The sum is = {:.2f}".format(sum))
