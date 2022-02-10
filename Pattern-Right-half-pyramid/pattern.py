'''
   Program to print the pattern of Right half pyramid
            *
          * *
        * * *
      * * * *
    * * * * *
'''

n=int(input("Enter the value of n to print the pattern : "))
for i in range(0,n):
    for j in range(0,n):
        if(i+j>=n-1):
            print(" *",end="")
        else:
            print("  ",end="")
    print()
