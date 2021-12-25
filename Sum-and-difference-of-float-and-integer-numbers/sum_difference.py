#Program to find the sum and difference of integer and float numbers
print("Enter two integer numbers : ",end="")
a=int(input());
b=int(input());
print("Enter two float numbers : ",end="")
c=float(input())
d=float(input())
print("{0}+{1} = {2} \n{3}-{4} = {5}".format(a,b,a+b,a,b,a-b))
print("{0}+{1} = {2} \n{3}-{4} = {5}".format(c,d,round(c+d,1),c,d,round(c-d,1)))
