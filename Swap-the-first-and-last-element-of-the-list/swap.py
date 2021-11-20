#function to swap first and last elements of the list
def swap(List):
    size=len(List)
    #swapping of first and last element
    List[0]=List[0]+List[size-1]
    List[size-1]=List[0]-List[size-1]
    List[0]=List[0]-List[size-1]
    return List
     
     
List=[]
n=int(input("Enter the number of elements you want to enter in the list :"))
print("Enter {} numbers : ".format(n))
for i in range(0,n):
    num=int(input())
    List.append(num)

print("List before swapping last and first element = ",List)
print("List after swapping last and first element = ",swap(List))
