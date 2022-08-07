#Program to find the roots of the quadratic equation
import math
print("Enter the three coefficients of the quadratic equation : ");
A=float(input())
B=float(input())
C=float(input());
print((-B+math.sqrt(B*B-4*A*C))/(2*A))
print((-B-math.sqrt(B*B-4*A*C))/(2*A));