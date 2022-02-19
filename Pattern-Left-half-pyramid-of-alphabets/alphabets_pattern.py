'''
    Program to print left half pyramid of Alphabets 
    A
    B B
    C C C
    D D D D
    E E E E E
'''
d='A'
c=input("Enter the alphabet upto which you want to print the left half pyramid :")
if((c>='A' and c<='Z') or (c>='a' and c<='z')):
        n=(ord(c[0].upper())) % 64
        for i in range(0,n):
            for j in range(0,n):
                if(j<=i):
                    print(d,end=" ")
            print()
            d=chr(ord(d)+1)
else:
    print("The entered character is not an alphabet")
