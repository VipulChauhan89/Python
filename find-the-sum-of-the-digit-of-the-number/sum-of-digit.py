#Program to find the sum of the digit of the number.
sum=0
print("Enter the number : ",end="")
num=int(input())
while(num>0):
    s=num%10
    sum+=s
    num//=10
print("The sum of digit is = {}\n".format(sum))
