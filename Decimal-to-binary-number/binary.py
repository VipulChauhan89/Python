#Program to convert a decimal number into binary number
bin=0
i=1
deci=int(input("Enter the decimal number to convert it into binary number : "))
while(deci!=0):
    rem=deci%2
    bin=bin+(rem*i)
    deci/=2
    i*=10  

print("Binary number : {}\n".format(bin))
