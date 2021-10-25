txt=input("Enter the text to remove punctuation from it :") 
print("The original string is : " ,txt)
punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
for c in txt:
    if c in punctuation:
        txt = txt.replace(c, "")
print("The string after removing punctuation from it is : ", txt)
