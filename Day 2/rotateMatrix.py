"""https://leetcode.com/problems/rotate-image/"""
def rotate(self, matrix) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    n= len(matrix)
    for i in range(n):
        for j in range(i,n):
            if i != j :matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    
    for a in matrix:
        a.reverse()