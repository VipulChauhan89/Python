# Python Program to find the area of triangle by heron's formula
a=float(input('Enter first side: '))
b=float(input('Enter second side: '))
c=float(input('Enter third side: '))
#calculate the semiparameter of the triangle
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print('The area of the triangle is',area)
