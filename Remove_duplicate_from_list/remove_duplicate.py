list=[]
count=0
n=int(input("Enter the number of elements you want to enter in a list :"))
print("Enter the elements :")
for i in range(0,n):
    num=int(input())
    list.append(num)

print("List before removing duplicate items : ",end =" ")
for i in range(0,n):
    print(list[i] , end =" ")

list1=[]
for i in list:
    if i not in list1:
        list1.append(i)
        count+=1
    
print("\nList after removing duplicate items : ",end =" ")
for i in range(0,count):
    print(list1[i] , end =" ")
