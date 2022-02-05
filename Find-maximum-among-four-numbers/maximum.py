'''
  program to find the maximum among four number by desigining a function BIG which takes two numbers as parameter and return maximum among them
'''
def BIG(a,b):
      if(a>b):
         return a;
      else:
         return b;
print("Enter four  numbers : ")
a=int(input())
b=int(input())
c=int(input())
d=int(input())
print("The maximum number is = {}\n".format(BIG(a,BIG(b,BIG(c,d)))))
