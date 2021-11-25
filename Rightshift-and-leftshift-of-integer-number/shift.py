#Program to rightshift and leftshift of an integer number
num=int(input("Enter the number : "))
s=int(input("Enter how many bits you want to shift : "))
rs=num>>s;
ls=num<<s;
print("Number = {0}\nRightshift = {1}\nLeftshift = {2}\n".format(num,rs,ls))
