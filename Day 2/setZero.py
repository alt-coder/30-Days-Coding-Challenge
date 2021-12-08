'''
Each column's and row's first cell store wheather it(row or column) would be zero 
matrix[0][0] will store wheather that row is zeroth row is zero or now 
and we maintain another variable for the col
traverse from 1 col to end then traverse from first row to end
then handle matrix[0][0] case
https://leetcode.com/problems/set-matrix-zeroes/solution/
'''
def setZeros(matrix):
    iscol = False
    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            iscol = True
        for j in range(1,len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for j in range(1,len(matrix[0])):
        if matrix[0][j] == 0:
            for i in range(1,len(matrix)):
                matrix[i][j] = 0
    for i in range(1,len(matrix)):
        if matrix[i][0] ==0:
            for j in range(1,len(matrix[0])):
                matrix[i][j] =0
    if matrix[0][0] == 0:
        for j in range(1,len(matrix[0])):
                matrix[0][j] =0
    if iscol:
        for i in range(len(matrix)):
                matrix[i][0] = 0

arr  = [[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]
setZeros(arr)
print(arr)