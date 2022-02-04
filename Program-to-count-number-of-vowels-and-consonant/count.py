#Program to count the number of vowels and consonants in the string
v_count=0
c_count=0
vowel=['a','e','i','o','u','A','E','I','O','U']
ch=input("Enter the string : ")
for i in ch:
        if i in vowel:
           v_count+=1
        elif i!=' ':
           c_count+=1
print("The number of vowels is = {0}\nThe number of consonants is = {1}\n".format(v_count,c_count))
