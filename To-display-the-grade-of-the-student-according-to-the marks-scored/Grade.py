'''
  Program to display the grade of the student according to the marks scored by the student.
  
  percentage>=80 then Grade A
  percentage>=60 and percentage<80 then Grade B
  percentage>=50 and percentage<60 then Grade C
  percentage>=40 and percentage<50 then Grade D
  percentage>=35 and percentage<40 then Grade E
  percentage<35 then Grade F
'''
n=int(input("Enter the number of subject of which you want to enter marks : "))
marks=[]
sum=0
print("Enter the marks in {} subjects : ".format(n))
for i in range(0,n):
    marks.append(float(input()))
    sum+=marks[i]
percentage=sum/n;
if(percentage>=80):
    print("Grade A.")
elif(percentage>=60 and percentage<80):
    print("Grade B.")
elif(percentage>=50 and percentage<60):
    print("Grade C.")
elif(percentage>=40 and percentage<50):
    print("Grade D.")
elif(percentage>=35 and percentage<40):
    print("Grade E.")
elif(percentage<35):
    print("Grade F.")
else:
    print("Not a valid percentage.")
