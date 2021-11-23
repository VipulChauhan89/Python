num1=int(input("Enter the first number : "))
num2=int(input("Enter the second number : "))

print("\nValues before swap \nnum1 = ",num1,",num2 = ",num2)
(num1,num2)=(num2,num1)
print("\nValues after swap using tuple \nnum1 = ",num1,",num2 = ",num2)
