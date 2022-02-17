'''
    Program to check if the number entered by the user is present in the fibonacci series or not
'''

def check(x):
    t1=0
    t2=1
    nextTerm=0
    while(nextTerm<=x):
        if(nextTerm==x):
            return True
        nextTerm=t1+t2
        t1=t2
        t2=nextTerm
    return False


num=int(input("Enter the number to find out whether it exist in fibonacci series or not : "))
if(check(num)):
    print("{} is present in the fibonacci series\n".format(num))
else:
    print("{} is not present in the fibonacci series\n".format(num))
