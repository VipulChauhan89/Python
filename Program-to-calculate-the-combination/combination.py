'''
  Program to calculate the combination by providing total number of objects and total number of choosing objects
'''

def factorial(n):
   if(n==1):
      return n
   else:
      return n*factorial(n-1)

n=int(input("Enter the total number of objects : "))
r=int(input("Enter the number of objects you want to choose : "))
nCr=factorial(n)/(factorial(n-r)*factorial(r))
print("The Combination is = {}\n".format(nCr))
