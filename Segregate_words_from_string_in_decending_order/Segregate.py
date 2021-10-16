string=input("Enter the string to segrigate the words and display it in the decending order:")
list=[]
list=string.split(" ")
list.sort(reverse=True)
print("Words in decending order are :",list)