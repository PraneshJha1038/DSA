boxGrid = [["#",".","*","."],
           ["#","#","*","."]]

def rotateGrid(arr:list)->list:
    for i in range(len(arr)):
        count = 0
        for j in range(len(arr[0])-1,-1,-1):
            if arr[i][j] == ".":
                count += 1
            elif arr[i][j] == "*":
                count = 0
            else:
                arr[i][j+count] = "#"
                if (j + count != j):
                    arr[i][j] = "."
    return boxGrid

boxGrid = rotateGrid(boxGrid)

n = len(boxGrid)
m = len(boxGrid[0])
result = [["0"] * n for _ in range(m)]
for i in range(n):
    for j in range(m):
        result[j][n-1-i] = boxGrid[i][j]
print(result)