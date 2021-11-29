#Program to print the average of top three out of four test
print("Enter the marks in four test : ")
m1=float(input())
m2=float(input())
m3=float(input())
m4=float(input())
min=m1
if(m2<min):
    min=m2
if(m3<min):
    min=m3
if(m4<min):
    min=m4
sum=m1+m2+m3+m4-min
average=sum/3
print("The average of top three subjects is = {}\n".format(average))
