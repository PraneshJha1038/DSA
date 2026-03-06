grid = [[8,1,6],[3,5,7],[4,9,2],[8,1,6],[3,5,7]]
row = len(grid) # 3
col = len(grid[0]) # 4
def get_magic_number(row:list,i:int,j:int):
    sum = 0
    for idx in range(i,j+1):
        sum += row[idx]
    return sum
def sum_row(start_col, array):
    for i in range(row):
        if sum(array[i][start_col:start_col + 3]) != magic_number:
            return False
    return True

def check_diagonal(i:int,array:list):
    sum = 0
    for j in range(row):
        sum += grid[j][i+j]
    return sum
def check_secondary_diagonal(i:int, array:list):
    sum = 0
    for j in range(row):
        sum += grid[j][i + row - 1 - j]
    return sum

magic_squares = 0
for i in range(0,col-row+1):
    magic_number = get_magic_number(grid[0],i,i+row-1)
    # Diagonal
    if check_diagonal(i,grid) == magic_number:
        if check_secondary_diagonal(i,grid) == magic_number:
            if sum_row(i,grid) :
                magic_squares += 1
            else:
                break
        else:
            break
    else:
        break
print(magic_squares)
