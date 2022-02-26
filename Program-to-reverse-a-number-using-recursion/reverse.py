'''
    Program to reverse the digits of the number using recursion
'''

def revDigit(n,rev):
    if(n==0):
        return rev
    else:
        return revDigit(n/10,rev*10+n%10)

rev=0
num=int(input("Enter the number to reverse it : "))
print("Reverse of the number {0} is = {1}\n".format(num,revDigit(num,rev)))
