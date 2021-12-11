#Program to find the largest number among the N numbers entered by the user
print("Enter the number of numbers you want to enter : ",end="")
N=int(input())
print("Enter {} numbers :".format(N))
for i in range(0,N):
    num=int(input())
    if(i==0):
      largest=num
    elif(num>largest):
      largest=num;
print("{} is the largest number.\n".format(largest))
