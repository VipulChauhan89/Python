#Program to convert the positive decimal number into octal number
def toOctal(num):
    octal=0
    i=1
    while(num!=0):
        rem=num%8
        octal=octal+rem*i
        num/=8
        i*=10
    return octal

num=int(input("Enter the decimal number to convert it into octal number : "))
print("Octal number : {}\n".format(toOctal(num)))
