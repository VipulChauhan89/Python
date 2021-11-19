#recursive function to print the fibonacci series
def fibonacci(n):
    if(n<=1):
        return n
    else:
        return (fibonacci(n-1)+fibonacci(n-2))

num=int(input("Enter how many fibonacci numbers you want to print : "))
if(num<=0):
    print("Please enter the positive number.")
else:
    print("Fibonacci sequence is : ",end=" ")
    for i in range(num):
        print(fibonacci(i),end=" ")
