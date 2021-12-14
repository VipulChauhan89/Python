#Program to reverse the number entered by the user
reverse=0
print("Enter the number : ",end="")
num=int(input())
temp=num
while(temp!=0):
    rem=temp%10
    reverse=reverse*10+rem
    temp//=10
print("The reverse of the number {0} is = {1}\n".format(num,reverse))
