from collections import deque


def id(mat):
    count=0
    q= deque()
    for i,item in enumerate(mat):
        for j,num in enumerate(item):
            if num == 2:
                q.append((0,(i,j)))
                count+=1
            elif num==1:
                count+=1
    n=0
    s=set()
    
    while(len(q)>0):
        a = q.popleft()
        index=a[1]
        n=a[0]
        i=index[0]
        j=index[1]
        s.add(index)
        if i-1 >= 0 and (i-1,j) not in s and mat[i-1][j]==1:
            q.append((n+1,(i-1,j)))
            mat[i-1][j]=2
        if i+1 < len(mat) and (i+1,j) not in s and mat[i+1][j]==1:
            q.append((n+1,(i+1,j)))
            mat[i+1][j]=2
        if j-1 >= 0 and (i,j-1) not in s and mat[i][j-1]==1:
            q.append((n+1,(i,j-1)))
            mat[i][j-1]=2
        if j+1 < len(mat[0]) and (i,j+1) not in s and mat[i][j+1]==1:
            q.append((n+1,(i,j+1)))
            mat[i][j+1]=2
    # for item in mat:
    #     print(item)
    if len(s) == count:
        return n
    else:
        return -1
    
mat= [ [2, 1, 0, 2, 1],
                     [1, 0, 1, 2, 1],
                     [1, 0, 0, 2, 1]]
mat =[[1,2,0,2,2],
[2,1,2,1,2],
[1,2,2,1,2],
[2,1,1,2,2],
[2,1,2,1,1],
[0,1,1,0,1]
]

print(id(mat))