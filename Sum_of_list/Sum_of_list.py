print("NAME- Vipul Chauhan \nSECTION- E \nSTUDENT ID- 20011016")

list=[]
sum=0
n=int(input("Enter the number of elements you want to enter in a list :"))
print("Enter the elements :")
for i in range(0,n):
    num=int(input())
    list.append(num)
    
print("List is : ",end =" ")
for i in range(0,n):
    print(list[i] , end =" ")
    sum+=list[i]

print("\nSum of the list is : ",sum)
