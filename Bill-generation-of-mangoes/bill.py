'''
  Program to calculate the bill for mangoes 
  If the customer is known for more than 3 years and the bill is more than 600 than discount of 12% is given
  and if the customer is known for more than 3 years but the bill is less than 600 than discount of 7% is given
'''

def total_bill(a,b):
   if(b>3 and a>600):
      return (a*88)/100.0;
   elif(b>3 and a<=600):
      return (a*93)/100.0;
   else:
      return a;

bill=float(input("Enter the bill amount : "))
year=float(input("Enter the number of year he is known to the seller : "))
print("The total bill is = {}\n".format(float(total_bill(bill,year))))
