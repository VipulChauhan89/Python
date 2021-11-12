# Program to display the Fibonacci series up to n-th term
nterms=int(input("Enter the number upto which you want to find the series : "))
n1=0
n2=1
count=0
if nterms<=0:
   print("There is no fibonacci of negitive number or zero, Please enter the positive number ")
elif nterms==1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:",end=" ")
   while count<nterms:
       print(n1,end=" ")
       nth=n1+n2
       n1=n2
       n2=nth
       count+=1
