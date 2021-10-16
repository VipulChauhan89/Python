list=[]
print('Enter numbers to check if they are prime and type "END" to display the prime numbers ')
num=input()

while(num !="END"):
    count=0
    num=int(num)
    if(num>1):
        for i in range(2,num):
            if((num%i)== 0):
                count+=1
            else:
                pass
        if(count==0):
            list.append(num)
    else:
        pass
    num=input()
       
print("Prime numbers are :",list)