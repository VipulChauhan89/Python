num=int(input("Enter the number upto which you want to find the sum : "))
if num < 0:
   print("Enter a positive number")
else:
    sum=0
    print("The sum of natural numbers upto",num,"is =", end=" ")
    while(num>0):
        sum+=num
        num-=1
    print(sum)
