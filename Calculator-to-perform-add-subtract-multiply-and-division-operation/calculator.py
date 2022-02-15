'''
    Program to provide the menu to perform the calculation of '+', '-', '%', '*' by making the calculator
    And take two numbers as an input and print the output.
'''
ch=input("Enter an operator ('+','-','*','/') : ")
if(ch in ("+","-","*","/")):
    num1=float(input("Enter the first number : "))
    num2=float(input("Enter the second number : "))

if(ch=="+"):
    print("{0} + {1} = {2}\n".format(num1,num2,num1+num2))
elif(ch=="-"):
    print("{0} - {1} = {2}\n".format(num1,num2,num1-num2))
elif(ch=="*"):
    print("{0} * {1} = {2}\n".format(num1,num2,num1*num2))
elif(ch=="/"):
    print("{0} + {1} = {2}\n".format(num1,num2,num1/num2))
else:
    print("Not a valid operator.")
