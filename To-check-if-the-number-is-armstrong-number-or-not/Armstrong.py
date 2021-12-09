#Program to check if the number is armstrong number or not
num=int(input("Enter the number : "))
if(num>=100 and num<=999):
    temp=num
    sum=0
    while(temp!=0):
        s=temp%10
        sum=sum+(s**3)
        temp=temp//10
    if(sum==num):
        print("{} is an armstrong number.\n".format(num));
    else:
        print("{} is not an armstrong number.\n".format(num))
else:
    print("It is not a three digit number.\n")