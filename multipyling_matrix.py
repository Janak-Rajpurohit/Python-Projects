## Multiplying 2 matrix



mat1=[]
mat2=[]

## input matrix 1
m1=int(input("Enter no of rows for 1 matrix >>> "))
n1=int(input("Enter no of columns for 1 matrix >>> "))

for i  in  range(1,m1+1):        
    row=input(f"Enter {i} row >>> ").split(" ")
    print(row)
    if len(row)==n1:
        mat1.append(row)
    else:
        pass

## input matrix 2
m2=int(input("Enter no of rows for 2 matrix >>> "))
n2=int(input("Enter no of columns for 2 matrix >>> "))

for i  in  range(1,m2+1):        
    row=input(f"Enter {i} row >>> ").split(" ")
    print(row)
    if len(row)==n2:
        mat2.append(row)
    else:
        pass


def change(mat2):             ## this is to change pattern of matrix2 
    # print(mat2)               ######  AWAY TO TRANSPOSE MATRIX   
    m=[]
    for col2 in range(n2):
        nrow1=[]
        for row2 in range(m2):
            print(mat2[row2][col2])
            n=mat2[row2][col2]
            nrow1.append(n)
        m.append(nrow1)
    print(m)
    return m

def multiply(mat1,m):                  ## m = matrix 2
    result=[]
    r=0
    for row1 in range(m1):
        for col1 in range(n1):
            r+=int(mat1[row1][col1])*int(m[row1][col1])
        result.append(r)
    return result



if __name__=="__main__":
    # multiply(mat1,mat2)
    m=change(mat2)
    print(multiply(mat1,m))

