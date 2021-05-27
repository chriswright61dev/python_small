import numpy as np # suduko

suduko_grid = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

print(np.matrix(suduko_grid))

def check_row(y,n):
    global suduko_grid
    for i in range(0,9) :
        if suduko_grid[y][i] == n:
            return False

def check_column(x,n):
    global suduko_grid
    for i in range(0,9) :
        if suduko_grid[i][x] == n:
            return False

def check_square(y,x,n):
    global suduko_grid
    x0 = (x//3)*3 # Floor division // returns  0 3 6
    y0 = (y//3)*3
    for i in range(0,3) : 
        for j in range(0,3) : 
            if suduko_grid[y0+i][x0+j] == n:
                return False

def is_position_valid(y,x,n):
    if check_row(y,n) == False or check_column(x,n) == False or check_square(y,x,n) == False:
        return False
    return True            

def solve():
    global suduko_grid
    for y in range(9):
        for x in range(9):
            if suduko_grid[y][x] == 0:
                for n in range (1,10):
                    if is_position_valid(y,x,n):
                       suduko_grid[y][x] = n
                       solve()
                       suduko_grid[y][x] = 0
                return   
    print('\n')
    print(np.matrix(suduko_grid))             
    input('more')



solve()



# def is_position_valid(y,x,n):
#     global suduko_grid
#     for i in range(0,9) :
#         # is thera another n in the row
#         if suduko_grid[y][i]==n:
#             return False
#     for i in range(0,9) :
#         # is thera another n in the column
#         if suduko_grid[i][x]==n:
#             return False
#     x0 = (x//3)*3 # // is Floor division - returns  0 3 6
#     y0 = (y//3)*3
#     for i in range(0,3) :  # is thera another n in the square
#         for j in range(0,3) : 
#             if suduko_grid[y0+i][x0+j] == n:
#                 return False
#     return True    
