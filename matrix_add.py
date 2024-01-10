### adding two matrix of M x N 

matrix1=[]
matrix2=[]
"""~~~~~~~~~~~~INPUT CODE~~~~~~~~~~~~~"""
### for first matrix... ###
m=int(input("Enter no of rows for matrix >>> "))         ## rows from user 
n=int(input("Enter no of columns for matrix >>> "))      ## col from user
i=1
M=1
while M<=m:
    row=input(f"Enter {i} row for matrix 1 >>> ").split(" ")   ## tsking row as list
    if len(row)==n:                               ## cheking correct columns
        matrix1.append(row)
        M=M+1
    else:
        print("Pleae enter valid columns.")
        exit()
    i=i+1
### for seccond matrix... ###
i=1
M=1
while M<=m:
    row=input(f"Enter {i} row for matrix 2 >>> ").split(" ")   ## tsking row as list
    if len(row)==n:                               ## cheking correct columns
        matrix2.append(row)
        M=M+1
    else:
        print("Pleae enter valid columns.")
        exit()
    i=i+1


print("MATRIX 1")
for rows in matrix1:
    print(rows)

print("MATRIX 2")    
for rows in matrix2:
    print(rows)

"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ADDDITION CODE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
result_mat=[]
for row in range(m):
    result_mat.append(list(range(n)))   ### [[],[],[]] to assign answers
    for col in range(n):
        result_mat[row][col]=int(matrix1[row][col]) + int(matrix2[row][col])   ## adding corresponding elements and assigning to result

#### PRINTING RESULT
print("RESULT")
for rows in result_mat:
    print(rows)

