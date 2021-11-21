#accept two numbers from the user and add the number and print their sum
#function to add two numbers and return their sum
def add(a,b):
  sum=a+b
  return sum

a=int(input("Enter the first number : "))
b=int(input("Enter the second number : "))
print("{0} + {1} = {2}".format(a,b,add(a,b)))
