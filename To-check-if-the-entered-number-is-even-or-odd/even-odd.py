#program to check if the entered number is even or odd
num=int(input("Enter the number : "))
print("{} is an even number.".format(num) if (num%2==0) else "{} is an odd number.".format(num))
