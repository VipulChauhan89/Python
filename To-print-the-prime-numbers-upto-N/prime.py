#Program to print the prime numbers upto N
print("Enter the number till which you want to print the prime number : ",end="")
N=int(input())
print("Prime numbers are : ",end="")
for i in range(2,N+1):
    c=0;
    for j in range(2,i+1):
        if(i%j==0):
            c+=1
    if(c==1):
        print(i,end=" ")
