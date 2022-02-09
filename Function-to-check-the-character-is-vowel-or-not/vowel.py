'''
  Program to design the function to check if the character is vowel or not and then count the number of vowels in the string
'''

def is_Vowel(c):
      if(c in "AaEeIiOoUu"):
         return True
      else:
         return False
      
v_count=0
s=input("Enter the string : ")
for ch in s:
      if(is_Vowel(ch)):
         v_count+=1

print("The count of vowel in the string is = {}\n".format(v_count))
