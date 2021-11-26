#program to check if the entered character is vowel or consonant
c=input("Enter the character : ")[0]
vowel=['a','A','e','E','i','I','o','O','u','U']
ch=ord(c)
if((ch>=97 and ch<=122)or(ch>=65 and ch<=90)):
    if(c in vowel):
      print("The entered character is vowel.")
    else:
      print("The entered character is consonant.")
else:
    print("The entered character is not an alphabet.")
