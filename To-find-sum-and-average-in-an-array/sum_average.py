'''
    Program to find the sum and the average of the number in an array
'''

sum=0
n=int(input("Enter the number of elements you want to enter in an array : "))
arr=[]
average=0
for i in range(0,n):
    num=int(input())
    arr.append(num);
    sum+=arr[i]

average=sum/float(n)
print("The sum of an element in an array is = {}\n".format(sum))
print("The average of an element in an array is = {}".format(average))
