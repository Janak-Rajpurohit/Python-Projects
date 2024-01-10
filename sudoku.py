
"""
 9 X 9
## PUPZZLE
2 5 _ _ 3 _ 9 _ 1
_ 1 _ _ _ 4 _ _ _
4 _ 7 _ _ _ 2 _ 8
_ _ 5 2 _ _ _ _ _
_ _ _ _ 9 8 1 _ _
_ 4 _ _ _ 3 _ _ _
_ _ _ 3 6 _ _ 7 2
_ 7 _ _ _ _ _ _ 3
9 _ 3 _ _ _ 6 _ 4

## SOLUTION
2 5 8 7 3 6 9 4 1
6 1 9 8 2 4 3 5 7
4 3 7 9 1 5 2 6 8
3 9 5 2 7 1 4 8 6
7 6 2 4 9 8 1 3 5
8 4 1 6 5 3 7 2 9
1 8 4 3 6 9 5 7 2
5 7 6 1 4 2 8 9 3
9 2 3 5 8 7 6 1 4
"""




grid = [[2, 5, 0, 0, 3, 0, 9, 0, 1],
        [0, 1, 0, 0, 0, 4, 0, 0, 0],
        [4, 0, 7, 0, 0, 0, 2, 0, 8],
        [0, 0, 5, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 8, 1, 0, 0],
        [0, 4, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 3, 6, 0, 0, 7, 2],
        [0, 7, 0, 0, 0, 0, 0, 0, 3],
        [9, 0, 3, 0, 0, 0, 6, 0, 4]]


# print puzzle board
def show_puzzle():   
    print(" 2 5 _ _ 3 _ 9 _ 1 \n _ 1 _ _ _ 4 _ _ _ \n 4 _ 7 _ _ _ 2 _ 8 \n _ _ 5 2 _ _ _ _ _ \n _ _ _ _ 9 8 1 _ _ \n _ 4 _ _ _ 3 _ _ _ \n _ _ _ 3 6 _ _ 7 2 \n _ 7 _ _ _ _ _ _ 3 \n 9 _ 3 _ _ _ 6 _ 4")


def back(grid):
    e=empty(grid)
    if not e:
        return True
    else:
        row,num=e

    for i in range(1,10):
        if check_box(grid,i,(row,num)):
            grid[row][num]=i

            if  back(grid):
                return True
            grid[row][num]=0
    return False


def check_box(grid,row,num):

    ## box elements
    box_row=row//3
    box_num=num//3
    box=[]
    for k in range(box_row*3,(box_row*3)+3):
        for j in range(box_num*3,(box_num*3)+3):
            box.append(grid[k][j])
    
    ## col elements
    col=[grid[j][num] for j in range(9)]

    for i in range(1,10):   
        if i in grid[row]:    ## checking row
           continue
    
        elif i in col:        ## checking col
            continue
    
        elif i in box:        ## checking  box
            continue
        
        else:
            # print(i)
            # print(row,num)
            grid[row][num]=i
            empty(grid)
            break


def empty(grid):                              ## looking for empty 
    for row in range(len(grid)):              ## row is row index
        for num in range(len(grid[row])):     ## num is column index
            ele = grid[row][num]
            if ele==0:
                check_box(grid,row,num)
            
    return None

print("Sudoku")
show_puzzle()
back(grid)
# check_box(grid,row,num)
print("Solution")
for i in grid:
    print(i)
