#Program to count the frequency of a character in the string
def check(c,d):
    if(c==d):
        return True
    else:
        return False

count=0;
s=input("Enter the string : ")
d=input("Enter the character whose frequency you want to find out : ")
for ch in s:
    if(check(ch.upper(),d[0].upper())):
        count+=1

print("The count of character '{0}' in the string is = {1}\n".format(d,count))
