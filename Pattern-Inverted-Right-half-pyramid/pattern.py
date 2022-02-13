'''
    Program to print the pattern of Inverted right half pyramid
    * * * * *
      * * * *
        * * *
          * *
            *
'''

n=int(input("Enter the value of n to print the pattern : "))
for i in range(0,n):
    for j in range(0,n):
        if(i<=j):
            print("* ",end="")
        else:
            print("  ",end="")
    print()
