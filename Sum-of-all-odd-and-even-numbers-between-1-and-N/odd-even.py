#Program to find the sum of all odd and even numbers between 1 to N
sum_even=0
sum_odd=0
print("Enter the limit upto which you want to find the sum of odd and even numbers : ",end="")
N=int(input())
for i in range(1,N+1):
    if(i%2==0):
      sum_even+=i
    else:
      sum_odd+=i
print("Sum of odd numbers is : {}".format(sum_odd))
print("Sum of even numbers is : {}\n".format(sum_even))
