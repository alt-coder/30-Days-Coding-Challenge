
def canplace(grid,r,c,n):
    for i in range(9):
        if grid[r][i] == n:
            return False
        if grid[i][c]==n:
            return False
    