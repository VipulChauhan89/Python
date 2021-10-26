txt=input("Enter the text to store it in the dictionary :")
d=dict()
lst=txt.split()
def enter(x):
    count=0
    for i in x:
        count+=1
    d[x]=count
for j in lst:
    enter(j)
d=sorted(d.items(),key=lambda x:x[1],reverse=True)
for i in d:
    print("{0}:{1}".format(i[1],i[0]),end=" ")