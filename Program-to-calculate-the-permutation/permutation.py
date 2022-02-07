'''
  Program to calculate the permutation by providing total number of objects and number of objects selected as an input
'''

def factorial(n):
   if(n==1):
      return n
   else:
      return n*factorial(n-1)

n=int(input("Enter the total number of objects : "))
r=int(input("Enter the number of objects you want to select : "))
nPr=factorial(n)/factorial(n-r)
print("The Permutation is = {}\n".format(nPr))
