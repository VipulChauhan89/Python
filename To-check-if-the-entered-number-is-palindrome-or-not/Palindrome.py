#To check if the entered number is palindrome or not
#Function to check the palindrome number
def palindrome(num):
    temp=num
    sum=0
    while(temp!=0):
        rem=temp%10
        sum=sum*10+rem
        temp=temp//10
    if(num==sum):
        print(num,"is a palindrome number .\n")
    else:
        print(num,"is not a palindrome number .\n")

print("Enter the number : ",end="")
num=int(input())
palindrome(num)
