f=input("Enter the text to append it to the file Append.txt :")
file=open("/Users/vipulchauhan/Desktop/Python/Append.txt","a")
file.write(f)
file.close()
file=open("/Users/vipulchauhan/Desktop/Python/Append.txt","r")
f=file.read()
file.close()
print("The content of file after appending the text is : ",f)