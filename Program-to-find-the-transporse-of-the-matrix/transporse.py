#Program to find the transporse of the matrix
print("Enter the number of rows and number of columns of the matrix : ",end="");
n=int(input())
m=int(input())
print("Enter the {} elements :".format(n*m))
matrix=[]
for i in range(0,n):
    col=[]
    for j in range(0,m):
        num=int(input())
        col.append(num)
    matrix.append(col)
print("Entered matrix :")
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print("{} ".format(matrix[i][j]),end='')
    print()
    
print("Transpose of the above matrix :")
for i in range(len(matrix[0])):
    for j in range(len(matrix)):
        print("{} ".format(matrix[j][i]),end='')
    print()
