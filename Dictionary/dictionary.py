n=int(input("Enter the number of words you want to enter in the dictionary :"))
d=dict()
print("Enter the words in the dictionary :")
lst=[]
k=1
def delete(x):
    if(type(x)==int):
        j=input("Enter 'YES' to delete it from dictionary :")
        if(j=="YES"):
            del d[m]
    elif(type(x)==str):
        for i in range(1,n+1):
            if(d[i]==x):
                break
        j=input("Enter 'YES' to delete it from dictionary :")
        if(j=="YES"):
            del d[i]
                                     
def isPresent(x):
    if(type(x)==int):
        if x in d:
            print("Found in dictionary")
            delete(x)
            print(d)
        else:
            print("No result found in the dictionary")
            print(d)
    elif(type(x)==str):
        if x in d.values():
            print("Found in dictionary")
            delete(x)
            print(d)
        else:
            print("No result found in the dictionary")
            print(d)
        
while(k<=n):
    lst.append(input("{} : ".format(k)))
    k+=1

for i in range(1,n+1):
    d[i]=lst[i-1]

st=int(input("Enter '1' to be searched by key and '2' to be searched by value :"))
if(st==1):
    m=int(input("Enter the key to be searched :"))
    isPresent(m)
elif(st==2):
    m=input("Enter the value to be searched :")
    isPresent(m)
else:
    print("You entered the wrong choice")
