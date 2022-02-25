'''
    Program to find the sum of the digits of the number using recursion
'''
def sumofdigit(x):
    if (x==0):
        return 0
    else:
        return x%10 + sumofdigit(x//10)

num=int(input("Enter the digit to find out the sum of digit : "))
print("Sum of digit of number {0} = {1}\n".format(num,sumofdigit(num)))
