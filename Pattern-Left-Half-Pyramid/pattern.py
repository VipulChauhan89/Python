'''
    Program to print the pattern of Left half pyramid
    * 
    * *
    * * *
    * * * *
    * * * * *
'''

n=int(input("Enter the value of n to print the pattern : "))
for i in range(0,n):
    for j in range(0,n):
        if(j<=i):
            print("* ",end="")
        else:
            print("  ",end="")
    print()
