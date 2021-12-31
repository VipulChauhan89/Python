'''
    Program to print the pattern by accepting the value of N from the user
    
    pattern is
    1 
    2 2 
    3 3 3 
    4 4 4 4
    5 5 5 5 5
'''
print("Enter the limit upto which you want to print the pattern : ",end="")
N=int(input())
print("pattern is\n")
for i in range(1,N+1):
    for j in range(1,i+1):
        print("{} ".format(i),end="")
    print()
