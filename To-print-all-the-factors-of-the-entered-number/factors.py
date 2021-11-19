#function to print the factor of the entered number
def print_factors(x):
   print("The factors of",x,"are :",end=" ")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i,end=" ")

num=int(input("Enter the number whose factorial you want to find out : "))
print_factors(num)
