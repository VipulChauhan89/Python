t=tuple()
n=int(input("Enter the number of cities you want to enter in the tuple : "))

print("Enter the ",n," cities")
for i in range(0,n):
    ch=input()
    t=t+(ch,)

print(t)
